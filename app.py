import re
import unicodedata
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.template_filter("slug")
def slug(valor):
    """Transforma 'Em andamento' em 'em-andamento' e 'Concluído' em 'concluido'.

    O `replace(' ', '-')` do template antigo não dava conta: ele mantinha as
    maiúsculas e os acentos, então a classe gerada nunca batia com o CSS.
    """
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = texto.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")


STATUS = ["Aberto", "Em andamento", "Concluído"]
PRIORIDADES = ["Alta", "Média", "Baixa"]
PESO_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}

# Semana 1: a fila ainda mora aqui. Na semana 2 isso vira banco de dados.
CHAMADOS = [
    {
        "id": 1041,
        "titulo": "Acessos para a nova analista de folha",
        "solicitante": "Marina Alves",
        "status": "Aberto",
        "prioridade": "Alta",
        "aberto_em": "02/09",
    },
    {
        "id": 1040,
        "titulo": "Notebook e crachá para o time de campo",
        "solicitante": "Rafael Nunes",
        "status": "Em andamento",
        "prioridade": "Alta",
        "aberto_em": "02/09",
    },
    {
        "id": 1039,
        "titulo": "Correção de dados no holerite de agosto",
        "solicitante": "Juliana Prado",
        "status": "Em andamento",
        "prioridade": "Média",
        "aberto_em": "01/09",
    },
    {
        "id": 1038,
        "titulo": "Inclusão de dependente no plano de saúde",
        "solicitante": "Carlos Menezes",
        "status": "Aberto",
        "prioridade": "Média",
        "aberto_em": "01/09",
    },
    {
        "id": 1037,
        "titulo": "Declaração de vínculo empregatício",
        "solicitante": "Ana Beatriz Rocha",
        "status": "Concluído",
        "prioridade": "Baixa",
        "aberto_em": "28/08",
    },
    {
        "id": 1036,
        "titulo": "Agendamento do exame periódico",
        "solicitante": "Diego Farias",
        "status": "Concluído",
        "prioridade": "Baixa",
        "aberto_em": "27/08",
    },
]


def ordenar(chamados):
    """Prioridade alta primeiro; dentro do mesmo peso, o mais recente na frente."""
    return sorted(chamados, key=lambda c: (PESO_PRIORIDADE[c["prioridade"]], -c["id"]))


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
    )


@app.route("/novo", methods=["GET", "POST"])
def novo():
    erro = None
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        solicitante = request.form.get("solicitante", "").strip()
        prioridade = request.form.get("prioridade", "Média")

        if not titulo or not solicitante:
            erro = "Preencha o título e o nome do solicitante."
        elif prioridade not in PRIORIDADES:
            erro = "Prioridade inválida."
        else:
            novo_id = max((c["id"] for c in CHAMADOS), default=0) + 1
            CHAMADOS.append(
                {
                    "id": novo_id,
                    "titulo": titulo,
                    "descricao": descricao,
                    "solicitante": solicitante,
                    "prioridade": prioridade,
                    "status": "Aberto",
                    "aberto_em": datetime.now().strftime("%d/%m"),
                }
            )
            return redirect(url_for("index"))

    return render_template("novo.html", erro=erro, prioridades=PRIORIDADES, dados=request.form)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
