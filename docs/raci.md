# Matriz RACI — GovDesk

**R** = Responsible (executa) · **A** = Accountable (responde pelo resultado; **um único A por atividade**) · **C** = Consulted · **I** = Informed

| Atividade | PO / CIO<br>Guilherme Souto | Dev Lead<br>Raiza Antoneli | QA / Auditoria<br>Enrico do Carmo | UX/UI<br>Luana Alcântara | DevOps<br>Marcus Aurélios |
|-----------|:---:|:---:|:---:|:---:|:---:|
| Definir escopo e priorizar o backlog | A/R | C | C | C | I |
| Mapear o processo de chamados (AS-IS e TO-BE em BPMN) | A/R | C | C | C | I |
| Desenhar fluxos e protótipos das telas | C | C | I | A/R | I |
| Desenvolver o sistema (rotas, validação, status, indicadores) | C | A/R | C | C | I |
| Conferir fidelidade visual e acessibilidade | I | R | C | A/R | I |
| Testar e dar o go/no-go da entrega | I | R | A/R | C | I |
| Auditar conformidade LGPD e validações | C | C | A/R | I | C |
| Configurar ambiente, execução e backup | I | C | I | I | A/R |
| Aprovar solicitações de mudança | A/R | C | C | I | C |
| Encerrar o projeto e registrar o aceite | A/R | C | C | I | I |

## Regras de leitura

- Cada linha tem exatamente um **A** (conferido na revisão final do QA).
- Os cinco papéis das colunas são as **raias** do processo em [processo-chamados.md](processo-chamados.md); se um papel mudar aqui, o BPMN deve mudar junto (revisão cruzada a cada entrega).
- O **Product Owner** é quem aprova mudanças e dá o aceite final do projeto.
