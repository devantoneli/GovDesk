# Melhoria contínua — GovDesk

*Atualizado após a Semana 9 e na entrega final (Semana 10).*

Ciclo adotado: **PDCA** — Planejar (backlog e PETI) → Fazer (sprint) → Checar (testes, go/no-go e indicadores) → Agir (lições aprendidas e roadmap).

## 1. Balanced Scorecard (BSC)

| Perspectiva | Objetivo | Indicador | Meta | Situação |
|-------------|----------|-----------|------|----------|
| **Clientes** (colaboradores) | Atendimento rápido e previsível | MTTR | < 24 h | Medido na página Indicadores |
| **Clientes** | Resolver sem idas e voltas | FCR | > 80% | Ainda não medido (F5) |
| **Processos internos** | Fila priorizada e sem pedidos esquecidos | Chamados pendentes há mais de 24 h | 0 | Medido |
| **Processos internos** | Mudanças controladas | Mudanças com aprovação do PO | 100% | 5 solicitações documentadas |
| **Aprendizado e crescimento** | Equipe aprende e documenta | Lições aprendidas registradas, com ao menos 1 por integrante | ≥ 5 | 5 registradas |
| **Finanças / valor** | Reduzir retrabalho de RH | Chamados fora do e-mail | 100% dos novos | Fila única entregue |

## 2. Não conformidades

| # | Não conformidade | Norma ou prática violada | Ação corretiva | Responsável | Situação |
|---|------------------|--------------------------|----------------|-------------|----------|
| NC1 | Links do menu apontavam para `index.html`, `sobre.html` e `novo.html`, páginas que não existem no Flask | Fluxo de trabalho do README (QA testa antes do merge) | Links trocados por `url_for`; teste de navegação (N1 a N5) antes de cada merge | Dev Lead | Corrigida |
| NC2 | Commits direto na `main`, com mensagens genéricas ("Update base.html") | Convenção de commits e revisão por PR | Proteger a `main` e exigir PR com revisão | DevOps | Pendente (ação de configuração do repositório) |
| NC3 | RACI com atividades de outro projeto ("multi-tenant") e tabela quebrada | Coerência entre documentos | RACI reescrito com atividades do GovDesk e papéis iguais às raias do BPMN | PO | Corrigida |
| NC4 | Arquivo de teste solto (`teste.py`) e `__pycache__` versionados | Higiene do repositório | Removidos e `.gitignore` criado | DevOps | Corrigida |
| NC5 | Sem autenticação nem perfis de acesso | LGPD, Art. 6º, VII (segurança) | Operar só com dados fictícios; F2 no backlog | Dev Lead | Risco aceito e registrado |

## 3. Maturidade do processo

Escala inspirada no CMMI/COBIT (0 a 5).

| Domínio | Antes (Semana 1) | Agora | Meta do próximo ciclo | Evidência |
|---------|:---:|:---:|:---:|-----------|
| Gestão de chamados | 1 — ad hoc (e-mail) | 3 — definido | 4 — medido | Processo BPMN, status e indicadores |
| Privacidade (LGPD) | 0 — inexistente | 2 — repetível | 3 — definido | Mapeamento, aviso e bloqueio de CPF |
| Gestão de mudanças | 0 | 2 — repetível | 3 | Template com 5 solicitações |
| Papéis e responsabilidades | 1 | 3 — definido | 3 | RACI com um único A |
| Qualidade / testes | 1 | 2 — repetível | 3 — automatizado | Checklist manual; CI no backlog |
| Segurança de acesso | 0 | 1 — inicial | 3 | Sem login (NC5) |

## 4. Roadmap

| Horizonte | Entregas | Ligação |
|-----------|----------|---------|
| **Curto prazo** (próxima sprint) | Proteger a `main` (NC2); banco SQLite (F1); medir FCR (F5) | NC2, BSC clientes |
| **Médio prazo** (1 a 2 meses) | Autenticação e perfis (F2); fluxo restrito para dado de saúde (F6); notificações (F4) | LGPD, NC5 |
| **Longo prazo** (3 meses ou mais) | Atribuição automática (F3); CI com testes (F7); anonimização por retenção (F8) | Maturidade nível 4 |

O detalhamento das histórias está em [backlog.md](backlog.md).

## 5. Revisão
A cada ciclo, o QA revisa este documento junto com o RACI e o BPMN (revisão cruzada) e o PO aprova as prioridades do roadmap.
