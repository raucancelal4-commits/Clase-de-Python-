#Presentar nombre y edad 
nombre = input ("¿Cómo te llamas: ")                           #
edad = int (input("¿Cuántos años tienes: ?"))                   #
print(f"Hola mi nombre es {nombre} y tengo {edad} años ")       #

#Promedio de 3 notas 
nota1 = float (input ("Ingrese la primera nota:"))
nota2 = float (input ("Ingrese la primera nota:"))
nota3 = float (input ("Ingrese la primera nota:"))
prom=(nota1 + nota2 + nota3)/3
print(f"El promedio es {prom:.1f}")
if prom >= 7:
    print(f"Aprobado")
else:
    print(f"Reprobado")

#base del triangulo 
base = 10