# GovDesk

Aplicação web desenvolvida em Python com Flask como projeto acadêmico da Fatec.

## Stack

- Python 3
- Flask
- HTML / CSS / JavaScript (templates Jinja2)

## Como executar

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

A aplicação sobe por padrão em `http://127.0.0.1:5000`.

## Equipe e papéis

## Equipe e papéis

| Papel | Quem assume | O que faz |
|-------|-------------|-----------|
| **Dev Lead** | Raiza Antoneli | Define a arquitetura e os padrões de código, desenvolve o núcleo da aplicação, revisa os Pull Requests e resolve impedimentos técnicos |
| **Product Owner / CIO** | Guilherme Souto | Levanta os requisitos, prioriza o backlog, valida as entregas e faz a ponte com as partes interessadas |
| **QA / Auditoria** | Enrico do Carmo | Elabora e executa os testes, registra bugs, faz testes de regressão e audita o cumprimento dos padrões definidos |
| **UX/UI Designer** | Luana Alcântara | Desenha os fluxos de navegação e os protótipos das telas, mantém o design system, cuida da acessibilidade e acompanha a fidelidade da implementação |
| **DevOps / Infraestrutura** | Marcus Aurélios | Configura os ambientes e o pipeline de CI/CD, automatiza builds e deploys, monitora a aplicação e cuida de backups e segurança de acesso |

### Raiza Antoneli — Dev Lead

Responsável técnica pelo projeto. Define a arquitetura da aplicação, a organização de pastas e os padrões de código que o time segue.

- Decide a estrutura do projeto (rotas, templates, camadas, banco de dados)
- Escreve e revisa o código principal da aplicação
- Faz o code review dos Pull Requests antes do merge na `main`
- Mantém o `requirements.txt` e o ambiente de desenvolvimento
- Resolve impedimentos técnicos e apoia os demais integrantes

### Guilherme Souto — Product Owner / CIO

Responsável pelo produto e pela visão de negócio. Define **o que** será construído e em que ordem.

- Levanta e escreve os requisitos e as histórias de usuário
- Prioriza o backlog e define o escopo de cada entrega
- Valida se as funcionalidades entregues atendem ao que foi pedido
- Faz a ponte entre a equipe e as partes interessadas (professor, cliente, banca)
- Cuida da documentação de produto e da apresentação do projeto

### Enrico do Carmo — QA / Auditoria

Responsável pela qualidade e pela conformidade do que é entregue.

- Elabora e executa os casos de teste de cada funcionalidade
- Registra bugs com passos de reprodução, resultado esperado e obtido
- Testa a aplicação antes de cada entrega (testes de regressão)
- Audita se o código segue os padrões definidos pelo Dev Lead
- Verifica requisitos não funcionais: segurança básica, validação de formulários, tratamento de erros

## Fluxo de trabalho

1. O **PO** cria a issue descrevendo a funcionalidade e os critérios de aceite.
2. O **UX/UI Designer** desenha o fluxo e o protótipo da tela, anexa o material na issue e valida com o PO.
3. O **Dev Lead** distribui a issue e define a abordagem técnica.
4. O desenvolvimento acontece em uma branch separada (`feat/nome-da-funcionalidade`).
5. O **DevOps** garante que o pipeline rode na branch (build, lint e testes automatizados) e publica a versão no ambiente de homologação.
6. O **QA** testa a branch em homologação e aponta ajustes, se houver.
7. O **UX/UI Designer** confere a fidelidade da implementação em relação ao protótipo.
8. O **Dev Lead** revisa e aprova o Pull Request.
9. O merge é feito na `main` apenas após revisão e teste.
10. O **DevOps** executa o deploy da `main` e monitora a aplicação após a publicação.

## Convenção de commits

O projeto segue o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/):

```
<tipo>(<escopo opcional>): <descrição no imperativo>
```

| Tipo | Uso |
|------|-----|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação |
| `style` | Formatação, sem alterar a lógica |
| `refactor` | Reestruturação de código |
| `test` | Testes |
| `chore` | Configuração, dependências, build |

Exemplos:

```
feat: cria estrutura base da aplicação Flask
feat(templates): adiciona layout base e página inicial
fix: corrige validação do formulário de cadastro
docs: atualiza README com instruções de execução
```

## Estrutura do projeto

```
GovDesk/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   ├── css/
│   └── js/
└── templates/
```