#Importar modulos
import combina as cmb
import selection as sel
#Inserir numeros
numeros = []
def carregar():
    arq = open("files\\sorteado.txt", "r")
    linha = arq.readline()
    for x in linha.split(","):
        numeros.append(int(x))
    arq.close()
#Chama a função para gerar numeros.
carregar()
cmb.gerar_dados(numeros)
#Inicia a seleção dos melhores.
sel.selecionar()
print("Execução Concluída!")