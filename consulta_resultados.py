import connect
conn = connect.connectar()
meucursor = conn.cursor()
def find_results():
    meucursor.execute(
        "SELECT BL_01, BL_02, BL_03, BL_04, BL_05,"+ 
        "BL_06, BL_07, BL_08, BL_09, BL_10,"+ 
        "BL_11, BL_12, BL_13, BL_14, BL_15 FROM LTFC LIMIT 10"
    )
    resultado = meucursor.fetchall()
    for linha in resultado:
        print(linha)
def find_results_compare(lista):
    contador = 0
    conta_jogos = 0
    collection = []
    meucursor.execute(
        "SELECT BL_01, BL_02, BL_03, BL_04, BL_05, BL_06, BL_07, BL_08, BL_09, BL_10,"+ 
        "BL_11, BL_12, BL_13, BL_14, BL_15 FROM LTFC"
    )
    resultado = meucursor.fetchall()
    #Carrega resultados dos jogos para a Coleção.
    for linha in resultado:
        jogo = sorted(linha)
        collection.append(jogo)
    #Verre cada linha da listagem passada e verifica se já foi sorteado.
    for i in collection:
        if contador >= 13:
            conta_jogos += 1
            print("Jogo com " + str(contador) + " pontos")
            print("--------------------------------")
        contador = 0
        for num in i:
            if num in lista:
                contador += 1
    if conta_jogos >= 1:
        print("Jogos Premiados: " + str(conta_jogos))
    else:
        print("Nenhum Premiado.")

listagem = [2,3,4,5,6,7,8,10,12,13,14,18,20,21,24]
find_results_compare(listagem)
