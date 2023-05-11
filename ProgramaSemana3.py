from pathlib import Path
import random
import math

print("\t\tBienvenido al Programa Semana 3 de 1214 Sistemas Inteligentes!\n\n")

while True:

    print("Favor Seleccione la opcion de codigo que desea ejecutar:\n")
    print("1) Math Module\n")
    print("2) Random Module\n")
    print("3)Exit\n")
    ncodigo = int(input("Numero de codigo: "))


    if ncodigo == 1: 
        print("MENU Math Module\n")
        print("1)Diseñar una calculadora de posibles combinaciones y permutaciones\n")
        print("2) Crear un menu para calculos matematicos carios\n")
        print("Seleccione la opcion que desea realizar:")
        opcion = int(input("Numero de opcion: "))

        if opcion == 1:
            print("Bienvenido al programa de calculo de combinaciones y permutaciones sin repeticion\n")
            print("1) Combinaciones")
            print("2) Permutaciones\n")
            print("3) Salir\n")
            opcion1 = int(input("Ingrese la opcion que desea realizar: "))

            if opcion1 == 1:
                print("Bienvenido al programa de calculo de combinaciones\n")
                n = int(input("Ingrese el numero de items disponibles para seleccion: "))
                k = int(input("Ingrese el numero de items a seleccionar: "))
                combinaciones = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
                print("El numero de combinaciones posibles es: ", combinaciones)
            
            elif opcion1 == 2:
                print("Bienvenido al programa de calculo de permutaciones\n")
                n = int(input("Ingrese el numero de items disponibles para seleccion: "))
                k = int(input("Ingrese el numero de items a seleccionar: "))
                permutaciones = math.factorial(n)/math.factorial(n-k)
                print("El numero de permutaciones posibles es: ", permutaciones)

        elif opcion == 2:
            print("Bienvenido al programa de calculos matematicos varios\n")
            print("1) Conversión de Grados a Radianes")
            print("2) Conversión de Radianes a Grados")
            print("3) Producto (con tuples)")
            print("4) Raíz cuadrada de un numero")
            print("5) Seno, Coseno y tangente de un numero\n")
            print("6) Salir\n")
            opcion2 = int(input("Ingrese la opcion que desea realizar: "))

            if opcion2 == 1:
                print("Bienvenido al programa de conversion de grados a radianes\n")
                grados = float(input("Ingrese el numero de grados: "))
                radianes = math.radians(grados)
                print("El numero de grados en radianes es: ", radianes)
            elif opcion2 == 2:
                print("Bienvenido al programa de conversion de radianes a grados\n")
                radianes = float(input("Ingrese el numero de radianes: "))
                grados = math.degrees(radianes)
                print("El numero de radianes en grados es: ", grados)
            elif opcion2 == 3:
                print("Bienvenido al programa de producto (con tuples)\n")
                x = int(input("Ingrese el primer numero: "))
                y = int(input("Ingrese el segundo numero: "))
                producto = math.prod([x,y])
                print("El producto de los numeros ingresados es: ", producto)
            elif opcion2 == 4:
                print("Bienvenido al programa de raiz cuadrada de un numero\n")
                x = int(input("Ingrese el numero: "))
                raiz = math.sqrt(x)
                print("La raiz cuadrada del numero ingresado es: ", raiz)
            elif opcion2 == 5:
                print("Bienvenido al programa de seno, coseno y tangente de un numero\n")
                x = int(input("Ingrese el numero: "))
                seno = math.sin(x)
                coseno = math.cos(x)
                tangente = math.tan(x)
                print("El seno del numero ingresado es: ", seno)
                print("El coseno del numero ingresado es: ", coseno)
                print("La tangente del numero ingresado es: ", tangente)
            elif opcion2 == 6:
                break
            else:
                print("Favor ingrese una de las opciones desplegadas!\n")

    elif ncodigo == 2:
        print("MENU Random Module\n")
        print("1) Generar un numero aleatorio que represente su probabilidad de aprobar la clase, debe ser un valor porcentual entre 0 y 100\n")
        print("2)Se tiene un punto de batidos saludables que está ofreciendo combinaciones aleatorios ")
        print("3) Salir\n")
        opcion = int(input("Numero de opcion: "))

        if opcion == 1:
            print("Bienvenido al programa de generacion de numero aleatorio\n")
            probabilidad = random.randint(0,100)
            print("Su probabilidad de aprobar la clase es: ", probabilidad, "%")
        elif opcion == 2:
            print("Bienvenido al programa de generacion de combinaciones aleatorias de batidos\n")
            fruits = ["apple", "banana", "orange", "strawberry", "cherry", "mango"]
            complements = ["tofu", "yogurt", "ice cream", "peanut butter", "protein powder"]
            liquids = ["apple juice", "milk", "soy milk", "coconut milk", "rice milk", "orange juice", "pineapple juice"]
            random.shuffle(fruits)
            random.shuffle(complements)
            random.shuffle(liquids)
            print("Su batido es: ")
            print("Fruit 1: ", fruits[0])
            print("Fruit 2: ", fruits[1])
            print("Complement: ", complements[0])
            print("Liquid: ", liquids[0])
        elif opcion == 3:
            break
        else:
            print("Favor ingrese una de las opciones desplegadas!\n")
    
    elif ncodigo == "Exit" or ncodigo == "exit" or ncodigo == "Salir" or  ncodigo == "salir":
        break

    else: 
        print('''Hello World!
            My name is James and 
            I am 20 years old''')
        
        print("Favor ingrese una de las opciones desplegadas!\n")