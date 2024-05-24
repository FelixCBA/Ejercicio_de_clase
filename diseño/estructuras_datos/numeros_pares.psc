Algoritmo numeros_pares
	Definir n, i, cont, j Como Entero
	
	Escribir 'Ingrese un numero '
	Leer n 
	cont = 0
	i = 0
	Mientras i <= n Hacer
		si i MOD 2 = 0 Entonces
			cont = 1 + cont
		FinSi
		i = i + 1
	FinMientras
	
	i = 0
	j = 0
	Dimension tupla[cont]
	Mientras i <= n Hacer
		si i MOD 2 = 0 Entonces
			tupla[j] = i
			j = j + 1
		FinSi
		i = i + 1
	FinMientras
	

	para _ = 0 Hasta cont - 1 Hacer
		Escribir tupla[_]
	FinPara
FinAlgoritmo
