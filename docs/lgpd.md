# Checklist e Mapeamento LGPD - Projeto GovDesk

## 1. Nosso Objetivo
O objetivo deste documento é mostrar como o **GovDesk** cuida dos dados pessoais dos colaboradores. Como nosso sistema automatiza processos de RH e suporte interno, precisamos garantir que as informações de todos sejam tratadas com transparência, segurança e respeito à LGPD (Lei 13.709/2018). A regra básica aplicada é: o dado só é acessado por quem realmente precisa dele para resolver o chamado.

## 2. Quais dados coletamos e por quê?
Abaixo detalhamos as informações pessoais necessárias para fazer o sistema de atendimento funcionar:

**a** Dado Pessoal **b** Para que usamos? (Finalidade) **c** Base Legal (LGPD) **d** Quem pode acessar? **e** Por quanto tempo guardamos?

**a** Nome e E-mail Corporativo
**b** Para identificar o autor do chamado e enviar notificações sobre o andamento do pedido em tempo real.
**c** Art. 7º, V - Execução de contrato.
**d** Analistas de RH, Suporte de TI e Gestores diretos.
**e** Durante o contrato de trabalho (e até 5 anos após a saída, para histórico trabalhista). |

**a** Cargo e Setor
**b** Para que o sistema saiba para quem encaminhar o ticket de forma automática.
**c** Art. 7º, IX - Legítimo Interesse (otimizar processos).
**d** Sistema automatizado e Analistas de RH.
**e** O mesmo tempo do Nome e E-mail.

**a** CPF ou Matrícula
**b** Para garantir o login seguro no painel e vincular a solicitação ao prontuário correto do funcionário.
**c** Art. 7º, V - Execução de contrato.
**d** Apenas Administradores do sistema e RH Sênior.
**e** O mesmo tempo do Nome e E-mail.

## 3. Como lidamos com Dados Sensíveis?

O Dado Sensível Identificado: Informações de Saúde (Atestados médicos, condições especiais e  justificativas).

*O Contexto no Sistema:*
Nosso sistema tem um fluxo para justificar faltas ou pedir licença médica, onde o colaborador faz o upload de um atestado. Como esse documento geralmente contém o CID (código da doença) ou o estado de saúde, a LGPD considera isso um dado estritamente sensível (Art. 5º, II).

**Nossas medidas de proteção (Como mitigamos os riscos):**
* **Apoio Legal:** Fazemos esse tratamento exclusivamente para cumprir obrigações trabalhistas (Art. 11, II, 'a' e 'f' da LGPD).
* **Acesso Restrito:** Diferente de um chamado comum (ex: "meu monitor quebrou"), um ticket com atestado médico **não** cai na fila geral de atendimento. Ele é bloqueado e liberado *apenas* para o Departamento Médico ou profissionais de RH autorizados.