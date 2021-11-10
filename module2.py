import math 
import amsos 

print("""
                                          _                  _ _             
         __ _ _ __ ___  ___     ___ __ _| | ___ _   _  __ _| | |_ ___  _ __ 
       / _` | '_ ` _ \/ __|   / __/ _` | |/ __| | | |/ _` | | __/ _ \| '__|
      | (_| | | | | | \__ \  | (_| (_| | | (__| |_| | (_| | | || (_) | |   
      \__,_|_| |_| |_|___/    \___\__,_|_|\___|\__,_|\__,_|_|\__\___/|_|   
_________________________________________________________________________________

1.- Suma 
2.- Resta
3.- Multiplicación 
4.- División
5.- Arco Coseno
6.- Coseno hiperbólico inverso
7.- Raiz cuadrada
exit.- Salir de la calculadora 

""")



def calculator():
    answ = input("Seleccione una función:")

    if answ == "1":
       suma1 = int(input("Primer número: "))
       suma2 = int(input("Segundo número: "))
       print('{} + {} = '.format(suma1, suma2))
       print(suma1 + suma2)
       calculator()

    if answ == "2":
        resta1 = int(input("Primer número: "))
        resta2 = int(input("Segundo número: "))
        print('{} - {} = '.format(resta1, resta2))
        print(resta1 - resta2 )
        calculator()

    if answ == "3":
        mult1 = int(input("Primer número: "))
        mult2 = int(input("Segundo número: "))
        print('{} * {} = '.format(mult1, mult2))
        print(mult1 * mult2 )
        calculator()
    
    if answ == "4":
        div1 = int(input("Primer número: "))
        div2 = int(input("Segundo número: "))
        print('{} / {} = '.format(div1, div2))
        print(div1 / div2 )
        calculator()

    if answ == "5":
        arcos = int(input("Introduzca el número a convertir: "))
        print('El arco coseno de {}='.format(arcos))
        print( math.acos( arcos ) )
        calculator()

    if answ == "6":
        coship = int(input("Introduzca el número a convertir: "))
        print("El coseno hiperbólico inverso de {}= ". format(coship))
        print( math.acosh( coship ) )
        calculator()
 
    if answ == "7":
        raiz2 = int(input("Introduzca el número a convertir: "))
        print("La raiz cuadrada de {} =".format(raiz2))
        print( math.sqrt( raiz2 ) )
        calculator()

    if answ == "exit":
        amsos

    else:
        print("Sintax error: función no encontrada")  
        calculator() 


calculator()