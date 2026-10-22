# Checklist de testes manuais — GovDesk

Este é o roteiro que eu (QA) sigo antes de cada entrega e antes de qualquer merge na `main`. A ideia é simples: passar pelo sistema como um usuário de verdade passaria e garantir que nada quebrou no caminho. Cada bloco indica a história do [backlog](backlog.md) que está sendo conferida, para facilitar a rastreabilidade.

## Antes de começar

- Suba a aplicação do jeito que está no [README](../README.md) e abra `http://127.0.0.1:5000`.
- Teste em duas telas: no computador, com a janela cheia, e simulando um celular (no DevTools, com 375 px de largura).
- Na coluna **Resultado**, anote `OK`, `Falhou` ou `N/A`, para o que ainda não foi entregue.
- Achou algo errado? Abra uma issue contando o que você fez, o que esperava que acontecesse e o que aconteceu de fato. Um print ajuda muito.

**Data:** ____/____/______  **Branch / commit:** ____________  **Quem testou:** ____________

## 1. Navegação (H5)

Primeiro, o básico: dá para andar pelo sistema sem se perder e sem digitar URL na mão?

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| N1 | Abrir a página inicial (`/`) | A página de chamados carrega normalmente, com o cabeçalho e o menu. | |
| N2 | Clicar em "Sobre o projeto" | Abre a página Sobre, e o item do menu fica marcado. | |
| N3 | Clicar em "Chamados" | Volta para a lista, e o item do menu fica marcado. | |
| N4 | Clicar em "Novo chamado" no menu | Abre o formulário em `/novo`. | |
| N5 | Clicar em "+ Novo chamado" na página inicial | Também abre o formulário em `/novo`. | |
| N6 | Digitar um endereço que não existe, como `/xyz` | Aparece uma página de "não encontrado", e não uma tela de erro técnico do Flask. | |
| N7 | Navegar pelo menu usando só o teclado (`Tab` e `Enter`) | Dá para ver onde está o foco, e todos os links funcionam. | |

## 2. Lista de chamados (H4)

Quem atende precisa bater o olho e saber o que é mais urgente. É isso que estamos conferindo aqui.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| L1 | Abrir a lista sem nenhum filtro | Aparecem as colunas ID, Chamado, Prioridade, Status e Aberto em. | |
| L2 | Olhar a ordem dos chamados | Primeiro os de prioridade Alta, depois Média, depois Baixa. Entre os de mesma prioridade, o mais recente fica em cima. | |
| L3 | Ler a frase acima dos filtros | Os números de "X chamados na fila, Y ainda sem primeira resposta" batem com o que está na tabela. | |
| L4 | Olhar as etiquetas de status | Cada status tem sua cor: Aberto em vermelho, Em andamento em âmbar, Concluído em verde. Nenhuma etiqueta fica sem cor. | |
| L5 | Olhar a faixinha colorida à esquerda de cada linha | A cor combina com a prioridade do chamado. | |
| L6 | Ver a lista no tamanho de celular | A coluna "Aberto em" some, e a tabela continua fácil de ler, sem a página rolar para o lado. | |

## 3. Filtros

Os filtros precisam mostrar exatamente o que prometem, nem mais nem menos.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| F1 | Clicar em cada status, um de cada vez | Só aparecem chamados daquele status, o botão fica destacado e o número dentro dele bate com as linhas. | |
| F2 | Clicar em cada prioridade, uma de cada vez | Só aparecem chamados daquela prioridade, e o botão fica destacado. | |
| F3 | Escolher um status e uma prioridade juntos | Os dois filtros funcionam ao mesmo tempo. Trocar um não apaga o outro. | |
| F4 | Clicar em "Todos" ou "Todas" | Só aquele grupo de filtro é limpo, e o outro continua valendo. | |
| F5 | Combinar filtros que não têm resultado, como Concluído + Alta | Aparece a mensagem "Nenhum chamado com esses filtros", com um link para voltar à fila inteira. | |
| F6 | Colocar um valor inventado na URL, como `/?status=qualquer-coisa` | A página não quebra, só mostra a mensagem de lista vazia. | |

## 4. Abrir um chamado (H1)

Aqui é onde o solicitante realmente usa o sistema, então vale testar com calma.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| C1 | Abrir `/novo` | O formulário mostra os campos título, solicitante, prioridade e descrição. | |
| C2 | Preencher tudo e enviar | Você volta para a lista, e o chamado novo aparece com o status "Aberto". | |
| C3 | Conferir o chamado que acabou de ser criado | Título, solicitante e prioridade estão como você digitou. O ID é o próximo da sequência, e a data de abertura está preenchida. | |
| C4 | Criar um chamado com prioridade Alta | Ele aparece no topo, à frente dos outros chamados de prioridade Alta. | |
| C5 | Apertar F5 logo depois de enviar | O chamado não é criado duas vezes. | |
| C6 | Escrever `<script>alert(1)</script>` no título | O texto aparece escrito na lista, do jeito que foi digitado, e nenhum alerta pula na tela. | |

## 5. Erros no formulário (H3)

Quando a pessoa esquece algo, o sistema deve avisar com clareza e não fazê-la perder o que já digitou.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| V1 | Enviar sem título | Aparece um aviso dizendo que falta o título, e nenhum chamado é criado. | |
| V2 | Enviar sem solicitante | Aparece um aviso dizendo que falta o solicitante, e nenhum chamado é criado. | |
| V3 | Enviar sem os dois | Os dois avisos aparecem juntos. | |
| V4 | Preencher o título só com espaços | O sistema entende o campo como vazio. | |
| V5 | Depois de um erro, olhar os campos | Tudo o que já tinha sido digitado continua lá, inclusive a descrição. | |
| V6 | Depois de um erro, voltar para a lista | O número de chamados não mudou. | |

## 6. Conferência do aviso LGPD (H2)

Essa parte merece atenção especial. Chamados comuns caem na fila geral e qualquer pessoa do atendimento consegue ver. Por isso o aviso existe: para que ninguém escreva ali, sem perceber, um dado sensível, principalmente de saúde, como um atestado ou um CID. O que está sendo conferido aqui segue o que definimos em [docs/lgpd.md](lgpd.md).

### O aviso está no lugar certo?

| # | O que conferir | O que deve acontecer | Resultado |
|---|----------------|----------------------|-----------|
| P1 | Abrir `/novo` | O aviso está **colado no campo descrição**, logo acima ou logo abaixo dele, e não perdido no rodapé ou em outra página. | |
| P2 | Ver o formulário no computador | Dá para ver o aviso e o campo descrição ao mesmo tempo, sem rolar a página. | |
| P3 | Ver o formulário no tamanho de celular | O aviso continua perto do campo, inteiro e legível. | |
| P4 | Provocar um erro de validação (como no V1) | O aviso continua aparecendo quando o formulário volta. | |
| P5 | Ver se o aviso exige algum clique | Ele fica sempre à vista, e não escondido atrás de um ícone, tooltip ou "saiba mais". | |

### O aviso diz o que precisa dizer?

| # | O que conferir | O que deve acontecer | Resultado |
|---|----------------|----------------------|-----------|
| T1 | O que não deve ser escrito | O aviso cita dados de saúde: atestado, CID, diagnóstico, condição médica. | |
| T2 | Documentos pessoais | O aviso pede para não colocar CPF, RG ou dados bancários na descrição. | |
| T3 | Para onde ir | O aviso explica que atestados e assuntos de saúde têm um caminho próprio, restrito ao Departamento Médico ou ao RH autorizado, e não a fila geral. | |
| T4 | Jeito de falar | É uma frase curta e direta, que qualquer colaborador entende sem saber o que é LGPD. | |
| T5 | Coerência | Nada no aviso contradiz o que está em `docs/lgpd.md`. | |
| T6 | Revisão | Não há erro de digitação nem de acentuação. | |

### Todo mundo consegue ler?

| # | O que conferir | O que deve acontecer | Resultado |
|---|----------------|----------------------|-----------|
| A1 | Contraste | O texto tem contraste de pelo menos 4,5:1 com o fundo (dá para medir no DevTools). | |
| A2 | Cor | O aviso não depende só da cor para chamar atenção: tem texto claro ou um ícone com rótulo. | |
| A3 | Leitor de tela | O campo descrição está ligado ao aviso (`aria-describedby`), então quem usa leitor de tela ouve o aviso ao entrar no campo. | |
| A4 | Zoom de 200% | O aviso continua inteiro e legível. | |

### E os dados em si?

| # | O que conferir | O que deve acontecer | Resultado |
|---|----------------|----------------------|-----------|
| D1 | Campos do formulário | O formulário de chamado comum não tem campo para anexar atestado nem para digitar CPF. | |
| D2 | Dados de exemplo no `app.py` | Os chamados de exemplo usam nomes inventados e não têm nenhuma informação de saúde, CPF ou outro dado real. | |
| D3 | O que a lista mostra | A fila geral mostra só título, solicitante, prioridade, status e data. A descrição não aparece ali. | |

**Minha avaliação do aviso LGPD:** ☐ Aprovado  ☐ Aprovado com ressalvas  ☐ Reprovado

O que observei: ______________________________________________

## 7. Página Sobre

Uma conferida rápida para garantir que a página conta a história certa do projeto.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| S1 | Abrir `/sobre` | Aparecem as seções "O problema", "O que o sistema faz", "Como saberemos se deu certo" e "Entrega desta semana". | |
| S2 | Ler as metas | Aparecem "Menos de 24 horas" e "Acima de 80%", cada uma com sua explicação. | |
| S3 | Ler o texto da entrega | Ele descreve o que de fato foi entregue nesta semana. Lembrete: atualizar a cada sprint. | |

## 8. Ambiente (H9)

Por fim, conferimos se qualquer pessoa do time consegue rodar o projeto do zero.

| # | O que fazer | O que deve acontecer | Resultado |
|---|-------------|----------------------|-----------|
| E1 | Criar um ambiente virtual novo e rodar `pip install -r requirements.txt` | O Flask é instalado sem erro. | |
| E2 | Rodar `python app.py` | A aplicação sobe em `http://127.0.0.1:5000` sem nenhum erro no terminal. | |
| E3 | Ficar de olho no terminal durante todos os testes | Nenhum erro 500 ou exceção aparece enquanto você navega. | |

---

Terminou? Se tudo deu `OK`, é só avisar o Dev Lead na issue ou no PR que a branch está liberada. Se algo falhou, a issue aberta já serve de ponto de partida para a correção.
