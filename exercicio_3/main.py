import os

lista_ficheiros = os.listdir()
print(lista_ficheiros)
soma = 0
for ficheiro in lista_ficheiros:
    filename, file_extension = os.path.splitext(ficheiro)
    tamanho = os.path.getsize(ficheiro)
    soma += tamanho
print(soma)