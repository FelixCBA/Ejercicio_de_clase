Algoritmo almacen
	Definir descuento, total, unidades, total_desc, precio_un, es_jubilado Como Real
	
	precio_un = 1000
	Escribir 'Ingrese la cantidad de leches que va a comprar' 
	Leer unidades
	Escribir 'Ingrese si es jubilado o no (1 = si, 0 = no)'
	Leer es_jubilado
	total = unidades * precio_un
	descuento = 1
	
	si (12 < unidades y unidades <= 24) Entonces
		descuento = descuento - 0.10
	FinSi
	si unidades > 24 Entonces
		descuento = descuento - 0.15
	FinSi
	si es_jubilado = 1 Entonces
		descuento = descuento - 0.10
	FinSi
	
	total_desc = total * descuento
	Escribir 'El total sin descuento es ', total
	Escribir 'El total con descuento es ', total_desc
	
	
FinAlgoritmo
