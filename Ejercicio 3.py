# Entrada

partidos_perdidos =  int(input('Ingrese la cantidad de partidos perdidos: '))
partidos_empatados = int(input('Ingrese la cantidad de partidos empatados: '))
partidos_ganados = int(input('Ingrese la cantidad de partidos ganados: '))

# Proceso

total_de_puntos = partidos_ganados * 3 + partidos_empatados

# Salida

print(f'La cantidad total de puntos acumulados en el campeonato  \nque su equipo lleva son: {total_de_puntos}')