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
def find_results_compare(listagem):
    lista = []
    listagem = str(listagem).replace(" ","")
    for dez in listagem.split(","):
        lista.append(str(dez))
    contador = 0
    conta_jogos = 0
    collection = []
    onz_pt = 0
    doz_pt = 0
    trz_pt = 0
    qtz_pt = 0
    quz_pt = 0
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
        if contador == 11:
            onz_pt += 0
        if contador == 12:
            doz_pt += 1
        if contador == 13:
            trz_pt += 1
        if contador == 1:
            qtz_pt += 1
        if contador == 15:
            quz_pt += 1
        contador = 0
        for num in i:
            if num in lista:
                contador += 1
    if quz_pt == 0 and qtz_pt == 0 and trz_pt == 0 and doz_pt ==0:
        return True
    else:
        return False
    """
    print("Jogos com 11 pontos: " + str(onz_pt))
    print("--------------------------------")
    print("Jogos com 12 pontos: " + str(doz_pt))
    print("--------------------------------")
    print("Jogos com 13 pontos: " + str(trz_pt))
    print("--------------------------------")
    print("Jogos com 14 pontos: " + str(qtz_pt))
    print("--------------------------------")
    print("Jogos com 15 pontos: " + str(quz_pt))
    print("--------------------------------")
    conta_jogos = 0
    """
#listagem = [1, 2, 3, 5, 7, 9, 12 , 13, 16, 17, 18, 20, 21, 23, 25]
#find_results_compare(listagem)
