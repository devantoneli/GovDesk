# Termo de Encerramento — GovDesk

## Escopo

**Planejado:** sistema web de chamados de RH com abertura e validação, aviso LGPD, lista com filtros por status e prioridade, avanço de status e indicadores; documentação de governança (PETI, LGPD, RACI, template de mudança, backlog, WBS, processo BPMN e melhoria contínua).

**Entregue:**

| Item | Situação |
|------|----------|
| Abertura de chamado com validação (cliente e servidor) | Entregue |
| Aviso LGPD com ciência obrigatória e bloqueio de CPF | Entregue |
| Lista ordenada por prioridade, com filtros | Entregue |
| Avanço de status (Aberto → Em andamento → Concluído) com histórico | Entregue |
| Indicadores (MTTR, taxa de conclusão, pendentes, por status e prioridade) | Entregue |
| Página de governança e página 404 | Entregue (extra) |
| docs/: PETI, LGPD, RACI, template de mudança, backlog, WBS, processo (BPMN), melhoria contínua | Entregue |
| Persistência em banco de dados | **Não entregue** (dados em memória) |
| Autenticação e perfis de acesso | **Não entregue** |
| Atribuição automática e notificações | **Não entregue** |
| Indicador FCR | **Não entregue** |

## Resultados e indicadores
- Backlog entregue: **14 histórias** (H1 a H14); 8 itens futuros (F1 a F8) registrados.
- Fluxo completo funcionando: abrir, validar, avançar status, ver indicadores e histórico.
- MTTR: calculado a partir dos chamados concluídos e comparado à meta de **24 h** na página Indicadores.
- Não conformidades: 4 corrigidas, 1 pendente de configuração do repositório e 1 risco aceito (ver [melhoria-continua.md](melhoria-continua.md)).
- Lições aprendidas: 6 registradas, com ao menos uma por integrante ([licoes-aprendidas.md](licoes-aprendidas.md)).

## Pendências e riscos residuais

| Item | Impacto | Plano |
|------|---------|-------|
| Dados em memória: reiniciar o servidor apaga os chamados | Perda de histórico; sistema não serve para operação real | F1: banco SQLite |
| Sem autenticação nem perfis | Qualquer pessoa vê e altera a fila; só pode operar com dados fictícios (LGPD) | F2: login e perfis |
| `main` sem proteção de branch | Risco de repetir commits sem revisão | Ativar proteção e PR obrigatório (NC2) |
| FCR não medido | Meta de 80% do PETI sem evidência | F5: registrar retornos |
| Chamados com dado de saúde sem fluxo restrito | Risco LGPD, Art. 11 | F6: fluxo restrito |
| Sem testes automatizados | Regressões dependem do checklist manual | F7: CI |

## Sustentação
**Dono do sistema:** Guilherme Souto (PO/CIO) · **Suporte:** Raiza Antoneli (Dev Lead) e Marcus Aurélios (DevOps) · **Aprovador de mudanças:** Guilherme Souto, via [template-mudanca.md](template-mudanca.md)

Nível de serviço sugerido: correção de falhas que impeçam abrir chamados em até 1 dia útil; demais melhorias via backlog.

## Aceite
Product Owner: Guilherme Souto   Data: ____/____/______   Assinatura: ______________________
