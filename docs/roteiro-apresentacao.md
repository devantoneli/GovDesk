# Roteiro da apresentação (8 min + 2 min de perguntas)

Antes de começar: `python app.py`, abrir `http://127.0.0.1:5000` e conferir que a lista carrega (o servidor reinicia com os dados de exemplo).

| Tempo | Quem | O que falar e mostrar |
|-------|------|------------------------|
| 0:00–2:00 | PO — Guilherme | Problema (RH no e-mail), usuários e a jornada de governança. Mostrar a página **Sobre** e **Governança**. |
| 2:00–4:00 | Dev — Raiza | Demonstração: abrir chamado em **Novo chamado** (primeiro enviar vazio para mostrar a validação, depois testar CPF na descrição), ver na fila, clicar em **Iniciar atendimento** e **Concluir**, abrir o detalhe (histórico) e a página **Indicadores**. |
| 4:00–6:00 | QA — Enrico | Como PETI, LGPD, RACI e BPMN se conectam: meta de 24 h → indicador; aviso e bloqueio → LGPD; raias do BPMN = papéis do RACI. Mostrar o go/no-go. |
| 6:00–8:00 | PO + QA | Melhoria: BSC, não conformidades (NC1 a NC5), maturidade antes/agora e roadmap. |
| 8:00–10:00 | Todos | Uma lição por integrante (Raiza, Guilherme, Enrico, Luana, Marcus) e o que fariam diferente. Perguntas. |

## Checklist go/no-go final (QA)

- [ ] O app inicia com `python app.py` sem erro
- [ ] Fluxo completo: abrir chamado, validar, avançar status
- [ ] Aviso LGPD visível e nenhum dado pessoal real nos exemplos
- [ ] RACI com um único "A" por atividade
- [ ] backlog.md, wbs.md e Kanban coerentes
- [ ] BPMN TO-BE com raias iguais aos papéis do RACI
- [ ] melhoria-continua.md atualizado após a Semana 9
- [ ] encerramento.md e licoes-aprendidas.md concluídos
- [ ] README explica como rodar e quem faz o quê
- [ ] Link do repositório enviado
