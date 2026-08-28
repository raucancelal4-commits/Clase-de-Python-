'''Ejercicio 1 del la temperatura:
(EPS).- Entrada es la temperatura en celsius, proceso es la formula para convertir en fahrenheit es F=celsius*9/5+32 y la salida es el fahrenheit,
(Bosquejo).- celsius=25, F=25*9/5+32=> F=77.0°F
En codigo es 👇'''
Celsius=float(input("Ingrese la temperatura en Celsius:"))
F=Celsius * 9/5 + 32
print(f"La temperatura en Fahrenheit es:{F:.1f} °F") 

'''Ejercicio 2 del la segundos totales:
(EPS).- Entrada es el total de segundos, proceso es uan division entera // y sacar el residuo % y la salida es en hh:mm:ss
(Bosquejo).- total=3850,[horas=3850//3600=>horas=1, resto:3850%3600=250, minutos:250//60=4, segundos:250%60=10]
En codigo es 👇'''
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")

'''Ejercicio 3 del la cambio de a,b=b,a:
(EPS).- Entrada es de a y b, proceso es que a valga b y b valga a y la salida sera el resultado de a=b y el de b=a,
(Bosquejo).- a=10 y b=50, [a,b=b,a], a= b y b=a 
En codigo es 👇'''
a=int (input("a:"))
b=int (input("b:"))
a , b = b , a
print(f"a:{a} y b:{b}")

'''Ejercicio 4 del Iva:
(EPS).- Entrada precio del producto sin iva , proceso es la formula iva=precio*0.15 y la salida es total:iva+precio,
(Bosquejo).- precio=25, iva=25*0.15 y total es 28.75
En codigo es 👇'''
precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva
print(f"IVA:   {iva:.2f}")
print(f"Total: {total:.2f}")