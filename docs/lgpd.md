# Checklist e mapeamento LGPD — GovDesk

## 1. Objetivo
Mostrar como o **GovDesk** cuida dos dados pessoais dos colaboradores. Como o sistema automatiza processos de RH e suporte interno, as informações precisam ser tratadas com transparência, segurança e respeito à LGPD (Lei 13.709/2018). Regra básica: **o dado só é acessado por quem precisa dele para resolver o chamado** (princípios da finalidade, necessidade e segurança, Art. 6º).

## 2. Mapeamento dos dados pessoais

| Dado pessoal | Finalidade | Base legal | Quem acessa | Retenção |
|--------------|------------|------------|-------------|----------|
| Nome do solicitante (e e-mail corporativo, em evolução futura) | Identificar o autor do chamado e avisar sobre o andamento | Art. 7º, V — execução de contrato | Analistas de RH, suporte de TI e gestor direto | Durante o contrato de trabalho e até 5 anos após a saída, para histórico trabalhista |
| Cargo e setor *(evolução futura)* | Encaminhar o chamado automaticamente | Art. 7º, IX — legítimo interesse | Sistema e analistas de RH | Mesmo prazo do nome |
| CPF ou matrícula *(evolução futura, para login)* | Login seguro e vínculo ao cadastro correto | Art. 7º, V — execução de contrato | Administradores e RH sênior | Mesmo prazo do nome |

> **Na versão entregue** o sistema coleta apenas o **nome do solicitante** e o texto do chamado. CPF e demais dados ficam fora do escopo atual (minimização, Art. 6º, III).

## 3. Dados sensíveis
**Dado sensível identificado:** informações de saúde (atestados, condições especiais, justificativas), Art. 5º, II.

**Contexto:** pedidos de justificativa de falta ou licença médica podem trazer CID ou estado de saúde.

**Medidas de proteção:**
- **Apoio legal:** tratamento apenas para cumprir obrigação trabalhista (Art. 11, II, "a" e "f").
- **Acesso restrito:** chamado com dado de saúde **não** entra na fila geral; é liberado apenas ao Departamento Médico ou ao RH autorizado (etapa "Checar dado sensível" do [processo](processo-chamados.md)).

## 4. Como o sistema aplica a LGPD (privacy by design)

| Controle | Implementação | Teste |
|----------|---------------|-------|
| Aviso de privacidade visível no formulário | Caixa de aviso junto ao campo descrição | [testes.md](testes.md) |
| Ciência obrigatória | Checkbox exigido no cliente e no servidor | Enviar sem marcar mostra erro |
| Bloqueio de CPF no texto | Validação no servidor rejeita padrão de CPF | Digitar `123.456.789-09` na descrição |
| Dados de exemplo | Todos os nomes e chamados são fictícios | Revisão no go/no-go |
| Rastreabilidade | Histórico com data e hora de cada mudança de status | Detalhe do chamado |

## 5. Direitos dos titulares (Art. 18) e limitações atuais

| Direito | Situação |
|---------|----------|
| Confirmação e acesso | Via RH, por solicitação. Tela própria no backlog futuro |
| Correção e eliminação | Via RH. Sem exclusão no sistema (dados em memória; reiniciar limpa tudo) |
| Informação sobre compartilhamento | Não há compartilhamento com terceiros |

**Risco residual:** a versão atual não tem autenticação nem perfis de acesso; por isso só pode operar com dados fictícios. Controle de acesso está no backlog e em [template-mudanca.md](template-mudanca.md) (mudança 2).
