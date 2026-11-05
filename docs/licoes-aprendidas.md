# Lições Aprendidas — GovDesk

Foco em processos, não em culpados. Cada lição vem de algo que o histórico do repositório mostra.

| # | Situação | Causa | Ação recomendada | Responsável |
|---|----------|-------|------------------|-------------|
| 1 | Na primeira apresentação o menu apontava para páginas inexistentes e o sistema exibiu erros (links `index.html`, `sobre.html`, `novo.html` num app Flask). | Alterações de template editadas e enviadas direto à `main`, sem PR, sem revisão e sem rodar o app. | Proteger a `main`, exigir PR revisado e rodar o checklist de navegação antes de cada merge. | Dev Lead (Raiza Antoneli) |
| 2 | RACI e documentos tinham atividades de outro contexto ("multi-tenant") e tabela quebrada. | Documentos escritos em momentos diferentes e sem revisão cruzada. | Revisão cruzada RACI ↔ BPMN ↔ backlog a cada entrega. | PO (Guilherme Souto) |
| 3 | A checagem de qualidade só aconteceu no fim, e achou erros que já estavam na `main`. | O checklist de testes existia, mas não era um portão obrigatório antes do merge. | Tornar o checklist e o go/no-go condição de merge, registrados no PR. | QA (Enrico do Carmo) |
| 4 | Telas feitas por partes ficaram inconsistentes: estilos soltos no HTML e botões sem estilo. | O design system não estava centralizado; cada alteração mexia em estilo diferente. | Concentrar o design system num único CSS e validar fidelidade visual em cada PR. | UX/UI (Luana Alcântara) |
| 5 | O arquivo `requirements.txt` foi renomeado duas vezes por erro de digitação; `teste.py` e `__pycache__` foram versionados. | Sem `.gitignore` e sem checagem automática do repositório. | Criar `.gitignore` desde o início e um pipeline de CI que instale as dependências e suba o app. | DevOps (Marcus Aurélios) |
| 6 | Várias mensagens de commit eram "Update base.html", sem dizer o que mudou. | Edição pela interface web do GitHub, fora da convenção do README. | Seguir Conventional Commits também nas edições web e revisar mensagens no PR. | Dev Lead (Raiza Antoneli) |

## O que funcionou
- **Papéis claros no README e no RACI**: cada pessoa sabia o que lhe cabia.
- **Backlog com critérios de aceite**: facilitou testar e saber quando algo estava pronto.
- **Documentar a governança desde cedo** (PETI, LGPD, RACI, template de mudança) e depois ligar tudo ao sistema.
- **Checklist de testes manuais** do QA, com rastreio às histórias do backlog.

## O que não funcionou
- Commits direto na `main`, sem revisão.
- Documentos desencontrados (RACI, BPMN e backlog) por falta de revisão cruzada.
- Pouco tempo de ensaio da demonstração antes de apresentar.

## O que mudaríamos
- Proteger a `main` e trabalhar sempre com PR desde a primeira semana.
- Ensaiar a apresentação em outra máquina, a partir do repositório limpo, um dia antes.
- Medir o FCR desde o início, e não só o MTTR.
- Ligar cada documento de governança a uma função visível no sistema, para a banca enxergar a conexão.
