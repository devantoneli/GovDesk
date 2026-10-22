# Checklist de testes manuais — GovDesk

Roteiro que o QA executa antes de cada entrega (teste de regressão) e antes do merge de uma branch na `main`. Cada caso aponta a história do [backlog](backlog.md) que ele cobre.

## Como executar

1. Suba a aplicação seguindo o [README](../README.md) e acesse `http://127.0.0.1:5000`.
2. Teste em dois tamanhos de tela: desktop (janela cheia) e celular (DevTools, largura de 375 px).
3. Preencha a coluna **Resultado** com `OK`, `Falhou` ou `N/A` (funcionalidade ainda não entregue).
4. Todo caso que falhar vira issue com passos de reprodução, resultado esperado e resultado obtido.

**Data da execução:** ____/____/______  **Branch / commit:** ____________  **Executado por:** ____________

## 1. Navegação (H5)

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| N1 | Abrir `/` | Página "Chamados — GovDesk" carrega sem erro, com cabeçalho e menu. | |
| N2 | Clicar em "Sobre o projeto" no menu | Abre `/sobre`; o item fica marcado como página atual. | |
| N3 | Clicar em "Chamados" no menu | Volta para `/`; o item fica marcado como página atual. | |
| N4 | Clicar em "Novo chamado" no menu | Abre o formulário em `/novo`. | |
| N5 | Clicar em "+ Novo chamado" na página inicial | Abre o formulário em `/novo`. | |
| N6 | Acessar uma URL inexistente (ex.: `/xyz`) | Retorna página 404, sem stack trace do Flask. | |
| N7 | Navegar por todo o menu só com `Tab` e `Enter` | Todos os links recebem foco visível e funcionam pelo teclado. | |

## 2. Lista de chamados (H4)

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| L1 | Abrir `/` sem filtros | Tabela mostra as colunas ID, Chamado, Prioridade, Status e Aberto em. | |
| L2 | Conferir a ordem das linhas | Alta antes de Média antes de Baixa; dentro da mesma prioridade, o ID maior (mais recente) vem primeiro. | |
| L3 | Conferir o resumo acima dos filtros | "N chamados na fila, M ainda sem primeira resposta" bate com o total e com a quantidade de status "Aberto". | |
| L4 | Conferir as etiquetas de status | Aberto, Em andamento e Concluído aparecem coloridos (vermelho, âmbar, verde). Nenhuma etiqueta sem cor. | |
| L5 | Conferir a faixa à esquerda de cada linha | A cor da faixa corresponde à prioridade do chamado. | |
| L6 | Reduzir a tela para 375 px | Coluna "Aberto em" some; tabela continua legível, sem rolagem horizontal da página. | |

## 3. Filtros

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| F1 | Clicar em cada status (Aberto, Em andamento, Concluído) | Só aparecem chamados daquele status; o chip fica destacado; a contagem no chip bate com as linhas. | |
| F2 | Clicar em cada prioridade (Alta, Média, Baixa) | Só aparecem chamados daquela prioridade; o chip fica destacado. | |
| F3 | Combinar um status com uma prioridade | Os dois filtros valem ao mesmo tempo; trocar um mantém o outro na URL. | |
| F4 | Clicar em "Todos" / "Todas" | Remove apenas o filtro daquele grupo. | |
| F5 | Combinar filtros sem resultado (ex.: Concluído + Alta) | Aparece "Nenhum chamado com esses filtros" com link para ver a fila inteira. | |
| F6 | Acessar `/?status=qualquer-coisa` | Página não quebra; mostra o estado vazio. | |

## 4. Abertura de chamado (H1)

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| C1 | Abrir `/novo` | Formulário com os campos título, solicitante, prioridade e descrição. | |
| C2 | Preencher todos os campos e enviar | Redireciona para a lista; o novo chamado aparece com status "Aberto". | |
| C3 | Conferir o chamado criado | Título, solicitante e prioridade iguais aos digitados; ID maior que o último existente; data de abertura preenchida. | |
| C4 | Criar um chamado de prioridade Alta | Ele aparece no topo da lista, antes dos outros de prioridade Alta. | |
| C5 | Atualizar a página (F5) logo depois de enviar | O chamado não é criado em duplicidade. | |
| C6 | Digitar `<script>alert(1)</script>` no título | O texto aparece escrito na lista; nenhum alerta é executado. | |

## 5. Validação do formulário (H3)

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| V1 | Enviar com o título em branco | Mensagem de erro indicando o título; nenhum chamado criado. | |
| V2 | Enviar com o solicitante em branco | Mensagem de erro indicando o solicitante; nenhum chamado criado. | |
| V3 | Enviar com os dois em branco | As duas mensagens aparecem juntas. | |
| V4 | Enviar só com espaços no título | Tratado como campo em branco. | |
| V5 | Após um erro, conferir os campos | O que já tinha sido digitado (inclusive a descrição) continua preenchido. | |
| V6 | Após um erro, voltar à lista | O total de chamados não mudou. | |

## 6. Conferência do aviso LGPD (H2)

Referência: [docs/lgpd.md](lgpd.md). O aviso existe para que o solicitante não coloque dados sensíveis (principalmente de saúde, Art. 5º, II) num chamado comum, que cai na fila geral e é visto por todo o atendimento.

### 6.1 Presença e posição

| # | Item conferido | Resultado esperado | Resultado |
|---|----------------|--------------------|-----------|
| P1 | Abrir `/novo` | O aviso aparece **junto ao campo descrição** (logo acima ou logo abaixo), não no rodapé nem em outra página. | |
| P2 | Ver o formulário no desktop | O aviso fica visível ao mesmo tempo que o campo descrição, sem precisar rolar. | |
| P3 | Ver o formulário a 375 px | O aviso continua junto ao campo e legível, sem cortar o texto. | |
| P4 | Provocar um erro de validação (V1) | O aviso continua aparecendo na página reexibida. | |
| P5 | Conferir se o aviso depende de clique | Fica sempre visível; não está escondido atrás de ícone, tooltip ou "saiba mais". | |

### 6.2 Conteúdo

| # | Item conferido | Resultado esperado | Resultado |
|---|----------------|--------------------|-----------|
| T1 | O aviso diz o que **não** escrever | Cita dados de saúde: atestado, CID, diagnóstico, condição médica. | |
| T2 | O aviso cobre documentos pessoais | Orienta a não digitar CPF, RG ou dados bancários na descrição. | |
| T3 | O aviso diz o caminho certo | Informa que atestados e assuntos de saúde vão pelo fluxo restrito ao Departamento Médico / RH autorizado, e não pela fila geral. | |
| T4 | Linguagem | Frase curta, em português simples, sem jargão jurídico; dá para entender sem conhecer a LGPD. | |
| T5 | Coerência com a documentação | Nada no aviso contradiz o que está em `docs/lgpd.md` (finalidade, quem acessa, dado sensível). | |
| T6 | Ortografia | Sem erros de digitação ou acentuação. | |

### 6.3 Acessibilidade

| # | Item conferido | Resultado esperado | Resultado |
|---|----------------|--------------------|-----------|
| A1 | Contraste | Texto do aviso com contraste mínimo de 4,5:1 contra o fundo (conferir no DevTools). | |
| A2 | Não depende só de cor | O aviso é identificável por texto ou ícone com rótulo, não apenas pela cor de fundo. | |
| A3 | Leitor de tela | O campo descrição está ligado ao aviso (`aria-describedby`), então o aviso é lido ao focar o campo. | |
| A4 | Zoom de 200% | O aviso continua inteiro e legível. | |

### 6.4 Tratamento dos dados

| # | Item conferido | Resultado esperado | Resultado |
|---|----------------|--------------------|-----------|
| D1 | Formulário de chamado comum | Não existe campo de upload de atestado nem campo de CPF no formulário de `/novo`. | |
| D2 | Dados de exemplo em `app.py` | Os chamados de exemplo usam nomes fictícios e não contêm dados de saúde, CPF ou outros dados reais. | |
| D3 | Lista de chamados | A lista mostra só título, solicitante, prioridade, status e data; a descrição não aparece na fila geral. | |

**Parecer do QA sobre o aviso LGPD:** ☐ Aprovado  ☐ Aprovado com ressalvas  ☐ Reprovado

Observações: ______________________________________________

## 7. Página Sobre

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| S1 | Abrir `/sobre` | Seções "O problema", "O que o sistema faz", "Como saberemos se deu certo" e "Entrega desta semana". | |
| S2 | Conferir as metas | Aparecem "Menos de 24 horas" e "Acima de 80%" com as descrições. | |
| S3 | Conferir o texto da entrega | Descreve o que de fato foi entregue na semana (atualizar a cada sprint). | |

## 8. Ambiente (H9)

| # | Passo | Resultado esperado | Resultado |
|---|-------|--------------------|-----------|
| E1 | Criar um ambiente virtual novo e rodar `pip install -r requirements.txt` | Instala o Flask sem erro. | |
| E2 | Rodar `python app.py` | A aplicação sobe em `http://127.0.0.1:5000` sem erro no terminal. | |
| E3 | Conferir o terminal enquanto navega | Nenhum erro 500 nem exceção registrada durante os testes acima. | |
