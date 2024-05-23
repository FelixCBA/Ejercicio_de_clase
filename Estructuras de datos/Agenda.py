agenda = {}

while True:
    print('=' * 30)
    print('Gestor de agenda telefonica.')
    print('=' * 30)
    print('\nOpciones: ')
    print('\n1- Agregar persona.')
    print('2- Modificar persona.')
    print('3- Eliminar persona.')
    print('4- Mostrar todos los contactos.')
    print('5- Salir.\n')
    opcion = int(input('Ingrese la opcion deseada: '))

#Copiar estructura de la opcion dos para resolver la opcion 1

    if opcion == 1:
        contacto = dict()
        contacto['nombre'] = (input('\nIngrese el nombre: '))
        contacto['apellido'] = (input('\nIngrese el apellido: '))
        contacto['dni'] = int(input('\nIngrese el dni: '))
        contacto['e-mail'] = (input('\nIngrese el e-mail: '))
        contacto['telefono'] = int(input('\nIngrese el telefono: '))
        agenda[str(contacto['dni'])] = contacto

    elif opcion == 2:

        dni = input('Ingrese el dni del contacto a modificar: ')

        for dato in agenda[dni].keys():
            cambiar = input(f'Desea modificar el {dato} del contacto: ')
            if cambiar.lower() == 'si':
                agenda[dni][dato] = input(f'Ingrese el nuevo {dato} del contacto: ')

    elif opcion == 3:
        dni = input('Ingrese el dni de la persona que quiere eliminar: ')
        agenda.pop(dni)
        print('Contacto eliminado.')

    elif opcion == 4:
        print(agenda)

    elif opcion == 5:
        break

    else:
        print('Opcion incorrecta.')
