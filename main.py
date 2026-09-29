import requests

def obter_taxas():
    url =  "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def converter(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valori = valor / taxa_origem
        valorc = valori * taxa_destino
        return valorc
    else:
        return None
i = 0
while i <= 0:
 taxa_cambio = obter_taxas()
 try:
  valor = float(input("Valor Para Converter: "))
  if valor is not None:
    i =+ 1
 except ValueError as error:
   print("Digite Apenas Números, Sem Texto Ou Caracteres Especiais")
   
try: 
 print("Digite Apenas A Sigla" 
 "Exemplo: " 
 "BRL - Real" 
 "USD - Dólar")
 moeda_origem = str(input("Moeda Origem: ")).upper()
 moeda_destino = str(input("Moeda Destino: ")).upper()
except ValueError as error:
   print("Por Favor, Digite Moedas Válidas")

try:
 valorc = converter(
   valor, moeda_origem, moeda_destino, taxa_cambio)

 if valorc is not None:
   print(f'\n{valor:.2f} {moeda_origem} "Equivale a: " {valorc:.2f} {moeda_destino}"')
 else:
   print("Moedas Inválidas")

except:
   print("Lembre-se de Preencher Todos os Campos")
