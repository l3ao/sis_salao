import json


def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)
