#Importa biblioteca de itertools
from itertools import combinations as cmb
import gera_arquivo as arquivo
#Coleção com as novas combinações.
gerados = []
def gerar_dados(numeros):
    try:
        #lista de numeros
        #numeros = [1, 2, 3, 5, 7, 9, 10, 11, 12, 13, 15, 16, 17, 19, 21, 23, 24, 25]
        for x in cmb(numeros, 15):
            gerados.append(x)
        #Salva no arquivo.
        arquivo.gravar(gerados)
    except:
        print("Ocooreu um erro ao gerar os dados, tente novamente!")
