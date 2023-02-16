# Outro codigo com ideia de criptografia de mensagens, esse utliza varias formar de obter a mensagem assim que recebe uma entrada diferente 
# (Portal, Experimento, Schembulock, Realidade). A ideia é excluir os caracteres especiais para tratar apenas caracteres alfanuméricos.
# Para mais detalhes do algoritmo checar os comentários abaixo.

mensagem_descriptografada = list()

palavra_decodificadora = str(input())

if palavra_decodificadora == 'Portal':
	palavra_codificada = str(input())
	# cria uma lista com os elementos da entrada palavra_codificada
	# ['g', '%', '!', ...,'d']
	palavra_codificada = 'g % ! % @ ! n $ % i % @ @ ! # d'
	split_p_codificada = palavra_codificada.split( )

	# cria uma lista com as letras do alfabeto
	# ['a', 'b', 'c', ...,'z']
	string_alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
	alfabeto = string_alfabeto.split( ) 

	palavra_semi_decript = []
	# por meio do for, é checado se na palavra codificada tem letras que estão in alfabeto
	# se tiver, ele da append na lista palavra_semi_decript = []
	for letra in split_p_codificada :
		if letra in alfabeto :
			palavra_semi_decript.append(letra)

	# 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
	# palavra_semi_decript = ['g', 'n', 'i', 'd']

	#Agora, o codigo irá pegar as letras pegar os indices da interação de de cada letra de palavra_semi_descript em relação a lista alfabeto
	palavra_descript_lista = list()
	for x in palavra_semi_decript:
		indice_alfabeto = alfabeto.index(x)
		letra_seguinte = alfabeto[indice_alfabeto+1] # Depois de achar o index de g, n, i, d no alfabeto, é adicionado 1 no index, ou seja, é armazenado na variavel a letra seguinte da que era antes
		palavra_descript_lista.append(letra_seguinte) # Depois a letra seguinte vai sofrer append e armazenada na lista
		palavra_descript = ''.join(palavra_descript_lista) # Com o join a gente consegue unir todos os valores da lista pra formar uma palavra

	mensagem_descriptografada.append(palavra_descript)



elif (palavra_decodificadora == 'Experimento'):
    palavra_codificada = str(input())



elif (palavra_decodificadora == 'Schembulock '):
    palavra_codificada = str(input())



elif (palavra_decodificadora == 'Realidade'):
    palavra_codificada = str(input())



elif (palavra_decodificadora == ' '):
    pass