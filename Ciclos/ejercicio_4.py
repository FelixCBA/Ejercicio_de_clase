alumnos = int(input('Ingrese la cantidad de alumnos: '))
sumatoria_notas = 0

for i in range(1, alumnos + 1):
    sumatoria_notas += int(input(f'Ingrese la nota n° {i}: '))

promedio = sumatoria_notas / alumnos

if promedio > 8:
    print(f'\nCon un promedio de {promedio}, el rendimiento ha sido elevado.')
elif 6 <= promedio <= 8:
    print(f'\nCon un promedio de {promedio}, el rendimiento ha sido aceptable.')
else:
    print(f'\nCon un promedio de {promedio}, el rendimiento ha sido bajo.')