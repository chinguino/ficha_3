

def calcula_linhas(nome):
    with open(nome) as f:
        lines = 0
        for line in f:
            lines += 1
    return lines


def calcula_carateres(nome):
    with open(nome) as f:
        characters = 0
        for line in f:
            characters += sum(len(word) for word in f)
    return characters

def calcula_palavra_comprida(nome):
    with open(nome, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

def calcula_ocorrencia_de_letras(nome):
    freqs = {}
    with open(nome) as f:
        for line in f:
            for char in line:
                freqs.setdefault(char, 0)
                freqs[char] += 1
    return freqs