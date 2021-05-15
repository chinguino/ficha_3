import os
import glob
import csv
from matplotlib import pyplot as plt

dic_info = {}
lista_ficheiros = os.listdir()
print(lista_ficheiros)

for ficheiro in lista_ficheiros:
    filename, file_extension = os.path.splitext(ficheiro)
    tamanho = os.path.getsize(ficheiro)

    dic_info[file_extension] = {}
    dic_info[file_extension]['volume'] = tamanho
    tifCounter = len(glob.glob1(os.path.abspath(os.getcwd()), f"*{file_extension}"))
    dic_info[file_extension]['quantidade'] = tifCounter

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dic_info.items():
        writer.writerow([key, value])


lista_valores = dic_info.items
lista_chaves = dic_info.keys
plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
plt.title("grafico queijos")
plt.show()

print(dic_info)
