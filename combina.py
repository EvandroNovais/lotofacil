#Importa biblioteca de itertools
from itertools import combinations as cmb
import gera_arquivo as arquivo
#Coleção com as novas combinações.
gerados = []
#Função para gerar as combinações
def gerar_dados(numeros):
    try:
        #lista de numeros
        for x in cmb(numeros, 15):
            gerados.append(x)
        #Salva no arquivo.
        arquivo.gravar(gerados)
    except:
        print("Ocorreu um erro ao gerar os dados, tente novamente!")
