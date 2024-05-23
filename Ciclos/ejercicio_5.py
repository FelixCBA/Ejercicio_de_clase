
n = int(input('Ingrese el numero del cual se desea generar la tabla: '))
for_o_while = int(input('\nIngrese 0 o 1: '))

if for_o_while == 0:
    cont = 1
    while cont <= 10:
        print(f'\n{n} x {cont} = {n * cont}')
        cont += 1
else:
    for i in range(1, 10 + 1):
        print(f'\n{n} x {i} = {n * i}')