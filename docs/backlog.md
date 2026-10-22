# Backlog do GovDesk

| ID | Épico | História | Critério de aceite | Prioridade | Responsável | Sprint |
|----|-------|----------|--------------------|------------|-------------|--------|
| H1 | Cadastro | Como solicitante, quero abrir um chamado, para registrar meu problema. | Formulário em /novo grava o chamado com status "Aberto" e ele aparece na lista inicial. | Alta | Dev Lead | 1 |
| H2 | Cadastro | Como solicitante, quero ser avisado sobre dados sensíveis, para respeitar a LGPD. | Aviso de privacidade visível junto ao campo descrição. | Alta | QA | 1 |
| H3 | Cadastro | Como solicitante, quero ver erro se faltar o título ou o solicitante, para corrigir o formulário. | Título ou solicitante em branco: mensagem de erro, dados digitados mantidos e nenhum chamado criado. | Alta | Dev Lead | 1 |
| H4 | Acompanhamento | Como técnico, quero ver a prioridade e o status, para atender o mais urgente. | Lista exibe as colunas Prioridade e Status, ordenadas da mais alta para a mais baixa. | Média | Dev Lead | 1 |
| H5 | Acompanhamento | Como solicitante, quero chegar ao formulário a partir do menu e da lista, para abrir um chamado sem digitar a URL. | Link "Novo chamado" no menu e "+ Novo chamado" na página inicial levam a /novo. | Média | UX/UI | 1 |
| H6 | Governança | Como gestor, quero o RACI no repositório, para saber quem responde. | docs/raci.md com um único "A" por atividade. | Alta | PO | 1 |
| H7 | Governança | Como auditor, quero o backlog versionado, para rastrear decisões. | backlog.md com histórico de commits. | Média | PO | 1 |
| H8 | Governança | Como gestor, quero o WBS do MVP no repositório, para ver como o trabalho foi dividido. | docs/wbs.md com até 3 níveis a partir de "GovDesk — MVP". | Média | PO | 1 |
| H9 | Governança | Como equipe, quero as dependências instaladas com um comando, para rodar o projeto em qualquer máquina. | `pip install -r requirements.txt` instala o Flask sem erro. | Baixa | DevOps | 1 |
| H10 | Acompanhamento | Como técnico, quero alterar o status de um chamado, para mostrar o andamento ao solicitante. | Botão ou campo na lista muda o status entre Aberto, Em andamento e Concluído. | Média | Dev Lead | 2 |
