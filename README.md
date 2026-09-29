# Conversor de Moedas

Este projeto consiste em um conversor de moedas desenvolvido em Python. Ele utiliza a ExchangeRate-API para obter as taxas de câmbio e realizar conversões entre diferentes moedas de forma simples e prática.

## Funcionalidades

* Conversão entre diferentes moedas a partir de suas siglas.
* Consulta de taxas de câmbio por meio de uma API.
* Validação dos valores inseridos pelo usuário.
* Verificação da validade das moedas informadas.
* Exibição do resultado com duas casas decimais.

## Tecnologias utilizadas

* **Python:** linguagem utilizada para desenvolver o programa.
* **Requests:** biblioteca utilizada para realizar requisições HTTP.
* **ExchangeRate-API:** serviço responsável por fornecer as taxas de câmbio.

## Instalação

Para executar o projeto, é necessário ter o Python instalado e a biblioteca Requests.

Instale a dependência utilizando o seguinte comando:

```bash
pip install requests
```

## Como utilizar

1. Execute o arquivo Python do projeto.
2. Informe o valor que deseja converter.
3. Digite a sigla da moeda de origem.
4. Digite a sigla da moeda de destino.
5. O programa apresentará o valor convertido.

As moedas devem ser informadas por suas siglas internacionais, como BRL para o real brasileiro, USD para o dólar americano e EUR para o euro.

## Como funciona

O programa realiza uma requisição à ExchangeRate-API para obter as taxas de câmbio disponíveis, utilizando o dólar americano como moeda-base.

A função `obter_taxas()` é responsável por consultar a API e retornar as taxas recebidas.

Já a função `converter()` utiliza essas taxas para calcular o valor correspondente à moeda desejada. Primeiro, o valor informado é convertido para dólares e, em seguida, transformado na moeda de destino.

Caso as moedas informadas não estejam disponíveis, o programa retorna uma indicação de que a conversão não pode ser realizada.

## Observações

O funcionamento do conversor depende de uma conexão com a internet para consultar as taxas de câmbio. Como os valores das moedas variam, o resultado pode ser diferente em consultas realizadas em momentos distintos.

O programa utiliza as taxas fornecidas pela API e não considera eventuais tarifas, impostos ou encargos cobrados por instituições financeiras.

## Autor

Desenvolvido por Cutcharro.
