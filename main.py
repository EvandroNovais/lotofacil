#Importar modulos
import combina as cmb
#Inserir numeros
numeros = []
def carregar():
    arq = open("files\\sorteado.txt", "r")
    linha = arq.readline()
    for x in linha.split(","):
        numeros.append(int(x))
    arq.close()
#Gerar numeros
carregar()
cmb.gerar_dados(numeros)
print("Execução Concluída!")