import json

def pede_nome(nome):
    while True:
        try: 
            with open(nome) as f:
                return f"{nome}"
                break
        except OSError:
            print("Não consegui abrir o ficheiro:", nome)

def gera_nome(nome):
    with open(nome, 'w') as json_file:
        json.dump(nome, json_file)
    return json_file



