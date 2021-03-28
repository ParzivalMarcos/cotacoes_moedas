from requisicoes import Cotacoes

obj = Cotacoes()

moeda_especifica = obj.moeda_especifica("EUR")

print(moeda_especifica['EUR']['bid'])
