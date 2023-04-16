# DEX Avenue

Ambiente de pesquisa, desenvolvimento e playground para implementação
de modelos de data science.

## Sobre

A Avenue é uma corretora de valores americana com a sede em Miami e com escritório em São Paulo, mas com o objetivo 100% focada em clientes que moram no Brasil com o perfil de varejo de alta renda (pessoa que já investe em bolsa de valores, mas que desejam começar a investir no mercado financeiro americano) e com a maior lista de opção de ativos. 

A empresa vem crescendo em um ritmo acelerado e já tem mais de 600 mil clientes investidores. A plataforma que funciona tanto na versão Web/Desktop quanto na versão mobile (APP) foi pioneira em investir em recursos que melhoram o acesso do investidor comum à bolsa de valores norte-americana.

### Objetivo

Desenvolver um algoritmo/modelo de Machine Learning que realize recomendação (quem comprou X comprou tambem...) de Shares (ações) e ETFs (fundos de investimentos), baseado na última compra do cliente e, caso o cliente não tenha realizado nenhuma compra ou o produto comprado não tenha nenhuma relação com outros produtos, será apresentada a lista dos produtos mais comprados pelos clientes de forma geral.

## Glossário

### Playground

Ambiente visual, amigável ao usuário para exploração e interação com o modelo implementado.

## Demo

- [Playground](https://brunoht-dex-avenue-apphome-3nxg0e.streamlit.app/)
- [API](#Demo)

## Créditos

- [Bruno Henrique Trindade](https://www.linkedin.com/in/brunoht/)
- [Marcos Vinícios de Oliveira](https://www.linkedin.com/in/marcos-vi-de-oliveira/)

## Requisitos

- Python 3
- Anaconda
- VSCode

## Comandos

### Install

Realiza a instalação do ambiente Python localmente

```bash
bash install
```

### Run

Inicia o playground

```bash
bash dev run
```

### Build

Cria o binário do modelo implementado

```bash
bash dev build
```

## Estrutura do Projeto

- .docs: reúne todos os documentos, manuais, anotações referentes às implementações do projeto
- app: arquivos do Streamlit
    - Home: página principal do Playground
- config: configurações utilizadas para a fase de desenvolvimento do projeto
- data: diretório reservado para armazenar os arquivos de datasets utilizados pela ML
- models: binários do modelo implementado
- notebooks: reservado para pesquisa e estudo dos dados
- src: código fonte do modelo final (que será a base dos modelos binários)
    - Builder: implementa o código que será rodado para buildar o binário do modelo final
    - Recommender: classe base do modelo
    - Utils: funções úteis compartilhadas para toda a aplicação
- tests: reservado para arquivos de testes unitários e automatizados
- .env: arquivo que armazena variáveis do ambiente local onde a aplicação em tempo de desenvolvimento está sendo executada
- dev: arquivo em lote que reune os comandos (atalhos) utilizados para desenvolvimento
- install: arquivo em lote que reúne os comandos utilizados para instalar o ambiente de desenvolvimento
- readme.md: arquivo com informações sobre o projeto
- requirements.txt: utilizado para preparar o ambiente virtual do Python, instalando as bibliotecas necessárias para implementação do código fonte e para o uso nos notebooks

## Metodologias

- [CRISP-DM](https://www.escoladnc.com.br/blog/data-science/metodologia-crisp-dm/)
- [GitFlow](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=O%20que%20%C3%A9%20o%20Gitflow,por%20Vincent%20Driessen%20no%20nvie.)


