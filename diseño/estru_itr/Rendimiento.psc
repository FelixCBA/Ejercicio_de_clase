Algoritmo Rendimiento
	Definir estudiantes, suma, promedio, nota Como Real
	
	Escribir 'Ingrese la cantidad de estudiantes que han rendido: '
	Leer estudiantes
	Para i = 1 Hasta estudiantes Hacer
		Escribir 'Ingrese la nota del estudiante n° ', i
		Leer nota
		suma = suma + nota
	FinPara
	
	promedio = suma / estudiantes
	si promedio > 8 Entonces
		Escribir 'El rendimiento ha sido elevado'
	FinSi
	si promedio < 8 y promedio > 6 Entonces
		Escribir 'El rendimiento ha sido aceptable'
	FinSi
	si promedio < 6 Entonces
		Escribir 'El rendimiento ha sido lamentable'
	FinSi
	
FinAlgoritmo
