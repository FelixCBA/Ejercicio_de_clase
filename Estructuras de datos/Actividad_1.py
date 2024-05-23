print('\nIngrese 10 nombres de personas(Que no se repitan)\n')
nombres = []
n = 0
while n < 10:
    nombre = input('Ingrese un nombre: ')
    if nombre in nombres:
        print('El nombre ya esta en la lista, ingrese otro nombre\n')
        continue
    nombres.append(nombre)
    n += 1

for name in nombres:
    print(name)

nombres.pop(2)
nombres.sort()
print(nombres)

datos_personales = {'nombre': 'felix',
                    'apellido': 'tapia',
                    'email': 'felix@gmail',
                    'dni': 343543545,
                    'fecha': 231099}
