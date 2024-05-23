# Entradas

unidades = int(input('Ingrese la cantidad de envases de leche que quiere comprar:  '))
jubilado = input('¿Es jubilado? (Respuesta con Si o No)').upper()

# Proceso

monto_sin_descuento = unidades * 1000
descuento = 1

if 12 < unidades <= 24:
    descuento -= 0.10
elif unidades > 24:
    descuento -= 0.15
if jubilado == 'SI':
    descuento -= 0.10

monto_total = monto_sin_descuento * descuento

# Salida

print(f'El monto total de su compra sin descuento es: {monto_sin_descuento}$ y con descuento es: {monto_total}')
