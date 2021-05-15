import csv
import os
import glob

from matplotlib import pyplot as plt
def pede_pasta():
    user_input = input("Enter the path of your file: ")
    os.chdir(user_input)
    return user_input
def faz_calculos():
    dic_info = {}
    lista_ficheiros = os.listdir()

    for ficheiro in lista_ficheiros:
        filename, file_extension = os.path.splitext(ficheiro)
        tamanho = os.path.getsize(ficheiro)

        dic_info[file_extension] = {}
        dic_info[file_extension]['volume'] = tamanho
        counter = len(glob.glob1(os.path.abspath(os.getcwd()), f"*{file_extension}"))
        dic_info[file_extension]['quantidade'] = counter
    print(dic_info)
    return dic_info

def guarda_resultados(dic_info):
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dic_info.items():
            writer.writerow([key, value])


def faz_grafico_queijos(dic_info):
    lista_valores = dic_info.items
    lista_chaves = dic_info.keys
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("grafico queijos")
    plt.show()

def faz_grafico_barras(dic_info):
    lista_valores = dic_info.items
    lista_chaves = dic_info.keys
    plt.bar(lista_chaves, lista_valores)
    plt.title("grafico barras")
    plt.show()