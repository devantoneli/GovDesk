# Processo de chamados — AS-IS e TO-BE (BPMN)

Os diagramas abaixo usam a notação BPMN (eventos de início/fim, tarefas, gateways e raias) escritos em Mermaid, que o GitHub renderiza direto neste arquivo. As **raias do TO-BE são exatamente os papéis da [matriz RACI](raci.md)**.

## AS-IS — como era (e-mail e mensagens avulsas)

```mermaid
flowchart LR
    I((Início)) --> A[Colaborador envia e-mail ou mensagem ao RH]
    A --> B[Quem vê primeiro responde, se lembrar]
    B --> C{Resolveu?}
    C -- Não --> D[Pedido se perde na caixa de entrada]
    D --> E[Colaborador cobra por mensagem]
    E --> B
    C -- Sim --> F[Resposta informal, sem registro]
    F --> Z((Fim))
```

**Dores:** sem fila visível, sem prioridade, sem responsável definido, sem registro nem medição de prazo, dados pessoais soltos em e-mails.

## TO-BE — como fica com o GovDesk

```mermaid
flowchart LR
    S((Solicitante<br/>abre chamado)) --> FORM

    subgraph PO["PO / CIO"]
        direction LR
        PRI[Priorizar e aprovar mudanças<br/>quando o pedido exige mudança]
        ACE[Acompanhar indicadores<br/>e dar o aceite]
    end

    subgraph DEV["Dev Lead"]
        direction LR
        FORM[Validar formulário e registrar<br/>status Aberto]
        TRI[Triar por prioridade e<br/>atribuir atendimento]
        ATD[Atender e avançar status<br/>Em andamento]
        TIPO{Exige acesso<br/>ou infra?}
    end

    subgraph DOPS["DevOps"]
        direction LR
        INFRA[Liberar acesso ou<br/>equipamento]
    end

    subgraph QA["QA / Auditoria"]
        direction LR
        LGPD{Contém dado<br/>sensível?}
        BLQ[Bloquear da fila geral e<br/>encaminhar ao RH autorizado]
        VAL[Validar resolução<br/>e conformidade]
    end

    subgraph UX["UX/UI"]
        direction LR
        FB[Registrar feedback de<br/>usabilidade do solicitante]
    end

    FORM --> LGPD
    LGPD -- Sim --> BLQ --> F1((Fim: fluxo restrito))
    LGPD -- Não --> TRI
    TRI --> PRI
    PRI --> ATD
    ATD --> TIPO
    TIPO -- Sim --> INFRA --> VAL
    TIPO -- Não --> VAL
    VAL -- Reprovado --> ATD
    VAL -- Aprovado --> CON[Concluir chamado<br/>e registrar no histórico]
    CON --> FB
    FB --> ACE
    ACE --> F2((Fim))
```

### Etapas e donos

| # | Etapa | Raia (papel RACI) | Onde aparece no sistema |
|---|-------|-------------------|--------------------------|
| 1 | Abrir chamado com validação e aviso LGPD | Dev Lead (sistema) | Formulário `/novo` |
| 2 | Checar dado sensível | QA / Auditoria | Aviso, ciência obrigatória e bloqueio de CPF |
| 3 | Triar por prioridade | Dev Lead | Lista ordenada por prioridade |
| 4 | Priorizar / aprovar mudança, se houver | PO / CIO | [template-mudanca.md](template-mudanca.md) |
| 5 | Atender (status **Em andamento**) | Dev Lead | Botão "Iniciar atendimento" |
| 6 | Acesso ou infraestrutura, se necessário | DevOps | — |
| 7 | Validar resolução | QA / Auditoria | Botão "Concluir" só após validação |
| 8 | Concluir e registrar histórico | Dev Lead | Status **Concluído** + histórico do chamado |
| 9 | Feedback de usabilidade | UX/UI | Backlog de melhorias |
| 10 | Acompanhar indicadores e aceite | PO / CIO | Página **Indicadores** |

**Ganhos esperados:** fila única e visível, prioridade explícita, responsável por etapa, histórico auditável e MTTR medido (meta &lt; 24 h, ver [peti.md](peti.md)).
