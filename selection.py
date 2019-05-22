#Teste Comparação de listas.
collection = []
numeros = []
componente = []

#Lendo arquivo
with open("files\\gerados.txt", "r") as arquivo:
	for linha in arquivo:
		for num in linha.split(","):
			numeros.append(int(num))	
		collection.append(numeros)
		numeros = []
	arquivo.close()
		
#Listas de comparação
mirror01 = [1, 2, 3]
mirror02 = [2, 3, 4]
mirror03 = [4, 5, 3]
mirror04 = [6, 5, 7]
mirror05 = [8, 7, 9]
mirror06 = [9, 10, 11]
mirror07 = [11, 12, 13]
mirror08 = [14, 13, 12]
mirror09 = [15, 14, 16]
mirror10 = [16, 17, 18]
mirror11 = [19, 18, 17]
mirror12 = [20, 21, 19]
mirror13 = [22, 21, 23]
mirror14 = [24, 23, 22]
mirror15 = [25, 24, 23]

def selecionar():
	arq = open("files\\selecionados.csv", "w")
	conta_lista = 0
	conta_num = 0
	ruim = 0
	bom = 0
	for lista in collection:
		componente = lista
		conta_lista += 1
		#Percorre o componente	
		for item in componente:
			conta_num += 1
			#Verifica bl01
			if conta_num == 1:
				if item in mirror01:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl02
			elif conta_num == 2:
				if item in mirror02:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl03
			elif conta_num == 3:
				if item in mirror03:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl04
			elif conta_num == 4:
				if item in mirror04:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl05
			elif conta_num == 5:
				if item in mirror05:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl06
			elif conta_num == 6:
				if item in mirror06:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl07
			elif conta_num == 7:
				if item in mirror07:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl08
			elif conta_num == 8:
				if item in mirror08:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl09
			elif conta_num == 9:
				if item in mirror09:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl10
			elif conta_num == 10:
				if item in mirror10:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl11
			elif conta_num == 11:
				if item in mirror11:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl12
			elif conta_num == 12:
				if item in mirror12:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl13
			elif conta_num == 13:
				if item in mirror13:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl14
			elif conta_num == 14:
				if item in mirror14:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
			#Verifica bl15
			elif conta_num == 15:
				if item in mirror15:
					#print(item)
					bom += 1
				else:
					#print(item)
					ruim += 1
		if bom > 14:
			arq.write("Jogo "  + str(conta_lista) + ", " + str(componente).replace("[", "").replace("]", "") + "\n")
			#print(componente)
			#print("Ruim: " + str(ruim))
			#print("Bom: " + str(bom))
		bom = 0
		ruim = 0
		conta_num = 0
	arq.close()
	print("Contagem de Listas: " + str(conta_lista))