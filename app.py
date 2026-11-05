import os
import re
import unicodedata
from datetime import datetime, timedelta

from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
# Só para assinar as mensagens flash; em produção vem de variável de ambiente.
app.secret_key = os.environ.get("GOVDESK_SECRET", "govdesk-dev")


@app.template_filter("slug")
def slug(valor):
    """Transforma 'Em andamento' em 'em-andamento' e 'Concluído' em 'concluido'."""
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = texto.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")


@app.template_filter("dia")
def dia(valor):
    return valor.strftime("%d/%m")


@app.template_filter("datahora")
def datahora(valor):
    return valor.strftime("%d/%m/%Y %H:%M")


STATUS = ["Aberto", "Em andamento", "Concluído"]
PRIORIDADES = ["Alta", "Média", "Baixa"]
PESO_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}
# Fluxo do processo (ver docs/processo-chamados.md): cada passo leva ao seguinte.
PROXIMO_STATUS = {"Aberto": "Em andamento", "Em andamento": "Concluído"}
ACAO_STATUS = {"Aberto": "Iniciar atendimento", "Em andamento": "Concluir"}

META_MTTR_HORAS = 24  # meta do PETI: tempo médio de atendimento < 24 h
LIMITE_PRAZO_HORAS = 24

TAM_TITULO, TAM_SOLICITANTE, TAM_DESCRICAO = 120, 80, 600

# CPF com ou sem pontuação. O sistema não precisa dele para atender um chamado.
PADRAO_CPF = re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b")


def _agora():
    return datetime.now().replace(second=0, microsecond=0)


def _semente():
    """Dados fictícios, datados em relação a agora para a demonstração ficar viva."""
    agora = _agora()

    def h(horas):
        return agora - timedelta(hours=horas)

    def chamado(id_, titulo, solicitante, prioridade, status, aberto_h, descricao, andamento_h=None, concluido_h=None):
        historico = [(h(aberto_h), "Chamado aberto")]
        if andamento_h is not None:
            historico.append((h(andamento_h), "Status alterado para Em andamento"))
        if concluido_h is not None:
            historico.append((h(concluido_h), "Status alterado para Concluído"))
        return {
            "id": id_,
            "titulo": titulo,
            "solicitante": solicitante,
            "prioridade": prioridade,
            "status": status,
            "descricao": descricao,
            "aberto_em": h(aberto_h),
            "concluido_em": h(concluido_h) if concluido_h is not None else None,
            "historico": historico,
        }

    return [
        chamado(1041, "Acessos para a nova analista de folha", "Marina Alves", "Alta", "Aberto", 5,
                "Liberar acesso aos sistemas de folha e ponto antes do primeiro dia."),
        chamado(1040, "Notebook e crachá para o time de campo", "Rafael Nunes", "Alta", "Em andamento", 30,
                "Equipamentos para três novos colaboradores do time de campo.", andamento_h=26),
        chamado(1039, "Correção de dados no holerite de agosto", "Juliana Prado", "Média", "Em andamento", 20,
                "Divergência no valor de um adicional informado no holerite.", andamento_h=14),
        chamado(1038, "Inclusão de dependente no plano de saúde", "Carlos Menezes", "Média", "Aberto", 28,
                "Solicitação de inclusão no plano; documentos serão entregues presencialmente."),
        chamado(1037, "Declaração de vínculo empregatício", "Ana Beatriz Rocha", "Baixa", "Concluído", 70,
                "Declaração para apresentação em instituição financeira.", andamento_h=64, concluido_h=52),
        chamado(1036, "Agendamento do exame periódico", "Diego Farias", "Baixa", "Concluído", 96,
                "Agendar exame periódico anual.", andamento_h=90, concluido_h=74),
    ]


# A fila ainda mora em memória: reiniciar o servidor volta aos dados de exemplo.
CHAMADOS = _semente()


def ordenar(chamados):
    """Prioridade alta primeiro; dentro do mesmo peso, o mais recente na frente."""
    return sorted(chamados, key=lambda c: (PESO_PRIORIDADE[c["prioridade"]], -c["id"]))


def _buscar(id_):
    for c in CHAMADOS:
        if c["id"] == id_:
            return c
    abort(404)


def _destino_seguro(destino):
    """Aceita só caminhos internos, para o 'voltar' não virar redirecionamento aberto."""
    if destino and destino.startswith("/") and not destino.startswith("//"):
        return destino
    return url_for("index")


def indicadores():
    agora = _agora()
    total = len(CHAMADOS)
    por_status = {s: sum(1 for c in CHAMADOS if c["status"] == s) for s in STATUS}
    por_prioridade = {p: sum(1 for c in CHAMADOS if c["prioridade"] == p) for p in PRIORIDADES}

    concluidos = [c for c in CHAMADOS if c["concluido_em"]]
    mttr = None
    if concluidos:
        mttr = sum((c["concluido_em"] - c["aberto_em"]).total_seconds() for c in concluidos) / len(concluidos) / 3600

    pendentes = [c for c in CHAMADOS if c["status"] != "Concluído"]
    fora_prazo = [c for c in pendentes if (agora - c["aberto_em"]).total_seconds() / 3600 > LIMITE_PRAZO_HORAS]

    return {
        "total": total,
        "por_status": por_status,
        "por_prioridade": por_prioridade,
        "taxa_conclusao": round(100 * por_status["Concluído"] / total) if total else 0,
        "mttr": mttr,
        "mttr_ok": mttr is not None and mttr < META_MTTR_HORAS,
        "pendentes": len(pendentes),
        "alta_pendente": sum(1 for c in pendentes if c["prioridade"] == "Alta"),
        "fora_prazo": len(fora_prazo),
    }


@app.route("/")
def index():
    status_atual = request.args.get("status", "")
    prioridade_atual = request.args.get("prioridade", "")

    visiveis = [
        c
        for c in CHAMADOS
        if (not status_atual or slug(c["status"]) == status_atual)
        and (not prioridade_atual or slug(c["prioridade"]) == prioridade_atual)
    ]

    return render_template(
        "index.html",
        chamados=ordenar(visiveis),
        total=len(CHAMADOS),
        abertos=sum(1 for c in CHAMADOS if c["status"] == "Aberto"),
        status_lista=STATUS,
        prioridade_lista=PRIORIDADES,
        contagem_status={s: sum(1 for c in CHAMADOS if c["status"] == s) for s in STATUS},
        contagem_prioridade={p: sum(1 for c in CHAMADOS if c["prioridade"] == p) for p in PRIORIDADES},
        status_atual=status_atual,
        prioridade_atual=prioridade_atual,
        acoes=ACAO_STATUS,
    )


@app.route("/novo", methods=["GET", "POST"])
def novo():
    erros = {}
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        solicitante = request.form.get("solicitante", "").strip()
        prioridade = request.form.get("prioridade", "Média")
        ciente = request.form.get("lgpd") == "on"

        if not titulo:
            erros["titulo"] = "Informe o título do chamado."
        elif len(titulo) > TAM_TITULO:
            erros["titulo"] = f"O título pode ter no máximo {TAM_TITULO} caracteres."
        if not solicitante:
            erros["solicitante"] = "Informe o nome do solicitante."
        elif len(solicitante) > TAM_SOLICITANTE:
            erros["solicitante"] = f"O nome pode ter no máximo {TAM_SOLICITANTE} caracteres."
        if len(descricao) > TAM_DESCRICAO:
            erros["descricao"] = f"A descrição pode ter no máximo {TAM_DESCRICAO} caracteres."
        elif PADRAO_CPF.search(titulo) or PADRAO_CPF.search(descricao):
            erros["descricao"] = "Parece haver um CPF no texto. Remova-o: o atendimento não precisa desse dado (LGPD)."
        if prioridade not in PRIORIDADES:
            erros["prioridade"] = "Escolha uma prioridade válida."
        if not ciente:
            erros["lgpd"] = "Confirme que leu o aviso de privacidade."

        if not erros:
            agora = _agora()
            novo_id = max((c["id"] for c in CHAMADOS), default=1000) + 1
            CHAMADOS.append(
                {
                    "id": novo_id,
                    "titulo": titulo,
                    "descricao": descricao,
                    "solicitante": solicitante,
                    "prioridade": prioridade,
                    "status": "Aberto",
                    "aberto_em": agora,
                    "concluido_em": None,
                    "historico": [(agora, "Chamado aberto")],
                }
            )
            flash(f"Chamado #{novo_id} aberto com sucesso.")
            return redirect(url_for("index"))

    return render_template(
        "novo.html",
        erros=erros,
        prioridades=PRIORIDADES,
        dados=request.form,
        limites={"titulo": TAM_TITULO, "solicitante": TAM_SOLICITANTE, "descricao": TAM_DESCRICAO},
    )


@app.route("/chamados/<int:id_>")
def detalhe(id_):
    return render_template("detalhe.html", c=_buscar(id_), acoes=ACAO_STATUS)


@app.route("/chamados/<int:id_>/avancar", methods=["POST"])
def avancar(id_):
    c = _buscar(id_)
    proximo = PROXIMO_STATUS.get(c["status"])
    if proximo is None:
        flash(f"O chamado #{id_} já está concluído.")
    else:
        agora = _agora()
        c["status"] = proximo
        c["historico"].append((agora, f"Status alterado para {proximo}"))
        if proximo == "Concluído":
            c["concluido_em"] = agora
        flash(f"Chamado #{id_} agora está “{proximo}”.")
    return redirect(_destino_seguro(request.form.get("voltar")))


@app.route("/indicadores")
def painel():
    return render_template("indicadores.html", i=indicadores(), meta=META_MTTR_HORAS, status_lista=STATUS, prioridade_lista=PRIORIDADES)


@app.route("/governanca")
def governanca():
    return render_template("governanca.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.errorhandler(404)
def nao_encontrado(_erro):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
