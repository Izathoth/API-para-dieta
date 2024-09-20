# API de Dieta

Esta é uma API simples para gerenciar diferentes tipos de dietas, construída usando o framework Flask e utilizando arrays como banco de dados em memória. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em uma coleção de dietas, fornecendo funcionalidades para adicionar novas dietas, atualizar informações de dietas existentes, excluir dietas e obter a lista completa ou individual de dietas.

## Funcionalidades

- **Listar Dietas**: Retorna todas as dietas cadastradas.
- **Consultar Dieta por ID**: Busca uma dieta específica pelo seu ID.
- **Adicionar Dieta**: Permite inserir uma nova dieta ao banco de dados.
- **Atualizar Dieta**: Atualiza os dados de uma dieta existente.
- **Deletar Dieta**: Remove uma dieta com base no ID.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **Arrays**: Usados como banco de dados em memória.

## Endpoints

- **GET /dietas**: Retorna todas as dietas.
- **GET /dietas/{id}**: Retorna uma dieta específica pelo ID.
- **POST /dietas**: Adiciona uma nova dieta.
- **PUT /dietas/{id}**: Atualiza uma dieta existente.
- **DELETE /dietas/{id}**: Deleta uma dieta pelo ID.
