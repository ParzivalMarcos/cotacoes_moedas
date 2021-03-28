import requests
import json


class Cotacoes():

    def todas_moedas(self):
        cotacao = requests.get("https://economia.awesomeapi.com.br/json/all")

        if cotacao.status_code == 200:
            return cotacao.json()
    


    def moeda_especifica(self, moeda):
        cotacao = requests.get(f"https://economia.awesomeapi.com.br/json/all/{moeda}")

        if cotacao.status_code == 200:    
            return cotacao.json()
