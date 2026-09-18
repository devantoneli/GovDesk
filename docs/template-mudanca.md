# Template de Solicitação de Mudança - Projeto GovDesk

------------------------------------------------
## 1. Cadastro de dados pessoais e sensíveis
## O que muda 
Adicionar ao sistema uma classificação dos dados dos funcionários entre dados pessoais, dados pessoais sensíveis e dados não pessoais.
## Por que 
Facilitar a identificação e o tratamento adequado das informações armazenadas no sistema, aumentando a segurança dos dados dos funcionários.
## Quem solicita 
DevOps / Infraestrutura	- Marcus Aurélios
## Quem aprova 
Dono do Produto / CIO - Guilherme Souto
## Impacto / Risco 
Pode ocorrer classificação incorreta de algum dado ou acesso indevido às informações. Serão realizados testes de classificação e de permissões antes da implantação.

------------------------------------------------

## 2. Controle de acesso dos funcionários
## O que muda 
Implementar diferentes níveis de acesso no sistema, permitindo que funcionários, gestores e administradores visualizem apenas as informações necessárias para suas funções.
## Por que 
Reduzir o risco de acesso indevido a informações dos funcionários, principalmente dados pessoais e sensíveis.
## Quem solicita  
DevOps / Infraestrutura	- Marcus Aurélios
## Quem aprova 
Dono do Produto / CIO - Guilherme Souto
## Impacto / Risco 
Uma configuração incorreta pode impedir usuários autorizados de acessar informações necessárias ou permitir acesso indevido. Serão realizados testes com diferentes perfis de usuário antes da implantação.

------------------------------------------------

## 3. Alteração do cadastro de funcionários
## O que muda 
Adicionar novos campos ao cadastro de funcionários, como telefone, endereço, cargo, departamento e data de admissão
## Por que 
Permitir que o sistema armazene informações necessárias para melhorar o gerenciamento dos funcionários e facilitar os processos administrativos do RH.
## Quem solicita 
Controle de Qualidade / Auditório - Enrico do Carmo
## Quem aprova 
Dono do Produto / CIO - Guilherme Souto
## Impacto / Risco 
A inclusão dos novos campos pode causar problemas de validação ou inconsistências nos cadastros existentes. Serão realizados testes de cadastro, edição e consulta antes da implantação.

------------------------------------------------

## 4. Relatório de funcionários
## O que muda 
Criar um novo relatório que apresente informações agregadas sobre os funcionários, como quantidade de funcionários por departamento, cargos e quantidade de admissões e desligamentos.
## Por que 
Facilitar a análise das informações do quadro de funcionários e auxiliar o RH na tomada de decisões administrativas.
## Quem solicita 
Controle de Qualidade / Auditório - Enrico do Carmo
## Quem aprova 
Dono do Produto / CIO - Guilherme Souto
## Impacto / Risco 
O relatório pode apresentar informações incorretas caso os dados utilizados estejam desatualizados ou sejam processados incorretamente. Serão comparados os resultados do relatório com os dados cadastrados no sistema antes da implantação.

------------------------------------------------

## 5. Registro de alterações no sistema
## O que muda 
Implementar um registro de auditoria para armazenar informações sobre alterações realizadas nos dados dos funcionários, incluindo usuário responsável, data, horário e tipo de alteração.
## Por que 
Aumentar a rastreabilidade das operações realizadas no sistema e permitir a identificação de alterações indevidas ou não autorizadas.
## Quem solicita 
Controle de Qualidade / Auditório - Enrico do Carmo
## Quem aprova 
Dono do Produto / CIO - Guilherme Souto
## Impacto / Risco 
O armazenamento dos registros de auditoria pode aumentar o volume de dados do sistema. Também existe o risco de registros incompletos. Serão realizados testes de inclusão, alteração e exclusão de dados para verificar se as operações estão sendo registradas corretamente.