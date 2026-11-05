# Backlog do GovDesk

## Entregue

| ID | Épico | História | Critério de aceite | Prioridade | Responsável | Sprint | Situação |
|----|-------|----------|--------------------|------------|-------------|--------|----------|
| H1 | Cadastro | Como solicitante, quero abrir um chamado, para registrar meu problema. | Formulário em /novo grava o chamado com status "Aberto" e ele aparece na lista inicial. | Alta | Dev Lead | 1 | Feito |
| H2 | Cadastro | Como solicitante, quero ser avisado sobre dados sensíveis, para respeitar a LGPD. | Aviso de privacidade visível junto ao campo descrição, com ciência obrigatória. | Alta | QA | 1 | Feito |
| H3 | Cadastro | Como solicitante, quero ver erro se faltar o título ou o solicitante, para corrigir o formulário. | Campo em branco: mensagem de erro, dados digitados mantidos e nenhum chamado criado. | Alta | Dev Lead | 1 | Feito |
| H4 | Acompanhamento | Como técnico, quero ver a prioridade e o status, para atender o mais urgente. | Lista com colunas Prioridade e Status, da mais alta para a mais baixa. | Média | Dev Lead | 1 | Feito |
| H5 | Acompanhamento | Como solicitante, quero chegar ao formulário a partir do menu e da lista, para abrir um chamado sem digitar a URL. | Link "Novo chamado" no menu e "+ Novo chamado" na lista levam a /novo. | Média | UX/UI | 1 | Feito |
| H6 | Governança | Como gestor, quero o RACI no repositório, para saber quem responde. | docs/raci.md com um único "A" por atividade. | Alta | PO | 1 | Feito |
| H7 | Governança | Como auditor, quero o backlog versionado, para rastrear decisões. | backlog.md com histórico de commits. | Média | PO | 1 | Feito |
| H8 | Governança | Como gestor, quero o WBS do MVP no repositório, para ver como o trabalho foi dividido. | docs/wbs.md com até 3 níveis a partir de "GovDesk — MVP". | Média | PO | 1 | Feito |
| H9 | Governança | Como equipe, quero as dependências instaladas com um comando, para rodar o projeto em qualquer máquina. | `pip install -r requirements.txt` instala o Flask sem erro. | Baixa | DevOps | 1 | Feito |
| H10 | Acompanhamento | Como técnico, quero alterar o status de um chamado, para mostrar o andamento ao solicitante. | Botão na lista e no detalhe avança Aberto → Em andamento → Concluído. | Média | Dev Lead | 2 | Feito |
| H11 | Acompanhamento | Como auditor, quero o histórico de cada chamado, para rastrear quem mudou o quê e quando. | Detalhe mostra linha do tempo com data e hora de cada evento. | Média | Dev Lead | 2 | Feito |
| H12 | Indicadores | Como gestor, quero ver MTTR e conclusão, para saber se a meta do PETI é atingida. | Página /indicadores com MTTR vs. meta de 24 h, taxa de conclusão e pendentes. | Alta | PO | 2 | Feito |
| H13 | Governança | Como gestor, quero o processo em BPMN, para ver responsáveis por etapa. | docs/processo-chamados.md com raias iguais aos papéis do RACI. | Alta | PO | 2 | Feito |
| H14 | Governança | Como equipe, quero melhoria contínua documentada, para planejar o próximo ciclo. | docs/melhoria-continua.md com BSC, não conformidades, maturidade e roadmap. | Média | QA | 2 | Feito |

## Backlog futuro

| ID | História | Prioridade | Ligação com governança |
|----|----------|------------|------------------------|
| F1 | Banco de dados persistente (SQLite) no lugar da lista em memória | Alta | Disponibilidade e integridade |
| F2 | Autenticação e perfis de acesso (solicitante, técnico, gestor) | Alta | LGPD / controle de acesso (mudança 2) |
| F3 | Atribuição automática de responsável por categoria | Média | PETI (objetivo de TI) |
| F4 | Notificação ao solicitante quando o status muda | Média | PETI (objetivo de TI) |
| F5 | Registro de retorno do solicitante para medir FCR | Média | Indicador do PETI |
| F6 | Fluxo restrito para chamados com dado de saúde | Alta | LGPD, Art. 11 |
| F7 | Pipeline de CI com testes automatizados | Média | Qualidade / DevOps |
| F8 | Exclusão e anonimização de chamados antigos | Média | LGPD, retenção |
