# GovDesk

Sistema web de **chamados de RH e onboarding**, desenvolvido em Python com Flask para a disciplina *Gestão e Governança de TI* (ITI004, Fatec). O projeto une uma aplicação funcional a uma governança documentada: estratégia (PETI), privacidade (LGPD), responsabilidades (RACI), processo (BPMN), mudanças e melhoria contínua.

## O que o sistema faz

- **Abrir chamado** com validação (cliente e servidor), aviso de privacidade LGPD, ciência obrigatória e bloqueio de CPF no texto
- **Fila de chamados** ordenada por prioridade, com filtros por status e prioridade
- **Avançar status**: Aberto → Em andamento → Concluído, com **histórico** de cada mudança
- **Indicadores**: tempo médio de atendimento (MTTR) contra a meta de 24 h, taxa de conclusão, pendentes e gráficos por status e prioridade
- **Governança**: página que liga cada documento à função no sistema

> Os dados de exemplo são fictícios e ficam em memória: ao reiniciar o servidor a fila volta ao estado inicial.

## Como rodar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS

# instalar dependências
python -m pip install -r requirements.txt

# rodar a aplicação
python app.py
```

Abra `http://127.0.0.1:5000`.

## Integrantes e papéis

| Papel | Integrante | Responsabilidades |
|-------|------------|-------------------|
| **Dev Lead** | Raiza Antoneli | Arquitetura, código da aplicação, revisão de PRs, resolução de impedimentos técnicos |
| **Product Owner / CIO** | Guilherme Souto | Requisitos, backlog, priorização, aprovação de mudanças e aceite |
| **QA / Auditoria** | Enrico do Carmo | Testes, registro de bugs, auditoria LGPD e go/no-go |
| **UX/UI Designer** | Luana Alcântara | Fluxos, protótipos, design system, acessibilidade e fidelidade visual |
| **DevOps / Infraestrutura** | Marcus Aurélios | Ambiente, dependências, pipeline, backup e segurança de acesso |

## Documentação (`docs/`)

| Documento | Conteúdo |
|-----------|----------|
| [peti.md](docs/peti.md) | Plano estratégico de TI, objetivos e indicadores |
| [lgpd.md](docs/lgpd.md) | Mapeamento de dados, bases legais e controles |
| [raci.md](docs/raci.md) | Matriz de responsabilidades (um único A por atividade) |
| [processo-chamados.md](docs/processo-chamados.md) | Processo AS-IS e TO-BE em BPMN, com raias iguais aos papéis do RACI |
| [template-mudanca.md](docs/template-mudanca.md) | Solicitações de mudança |
| [backlog.md](docs/backlog.md) | Histórias entregues e backlog futuro |
| [wbs.md](docs/wbs.md) | Estrutura analítica do projeto |
| [melhoria-continua.md](docs/melhoria-continua.md) | BSC, não conformidades, maturidade e roadmap |
| [testes.md](docs/testes.md) | Checklist de testes manuais |
| [encerramento.md](docs/encerramento.md) | Termo de encerramento |
| [licoes-aprendidas.md](docs/licoes-aprendidas.md) | Lições aprendidas |
| [roteiro-apresentacao.md](docs/roteiro-apresentacao.md) | Roteiro da apresentação e go/no-go |

## Backlog futuro

Banco de dados persistente, autenticação e perfis, atribuição automática, notificações, medição de FCR, fluxo restrito para dados de saúde, CI com testes e anonimização por retenção. Detalhes em [docs/backlog.md](docs/backlog.md).

## Fluxo de trabalho

1. O **PO** cria a issue com a funcionalidade e os critérios de aceite.
2. O **UX/UI** desenha o fluxo e valida com o PO.
3. O **Dev Lead** define a abordagem técnica.
4. O desenvolvimento acontece em branch separada (`feat/nome-da-funcionalidade`).
5. O **DevOps** garante build e testes na branch.
6. O **QA** testa a branch e aponta ajustes.
7. O **UX/UI** confere a fidelidade ao protótipo.
8. O **Dev Lead** revisa e aprova o Pull Request.
9. O merge na `main` só acontece após revisão e teste.
10. O **DevOps** publica e monitora.

## Convenção de commits

[Conventional Commits](https://www.conventionalcommits.org/pt-br/): `<tipo>(<escopo>): <descrição>`, com os tipos `feat`, `fix`, `docs`, `style`, `refactor`, `test` e `chore`.

## Estrutura

```
GovDesk/
├── app.py                 # rotas, regras e indicadores
├── requirements.txt
├── static/css/govdesk.css # design system
├── templates/             # base, index, novo, detalhe, indicadores, governanca, sobre, 404
└── docs/                  # governança documentada
```
