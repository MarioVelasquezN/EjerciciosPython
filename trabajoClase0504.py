#crear un menu que ofrezca un saludo y dos opciones al usuario (1 y 2)
#si el usuario ingresa 1, el programa debe realizar conversiones de temperatura
#si el usuario ingresa 2, el programa debe realizar calculo de dimensiones en un cubo

print("Bienvenido al programa de conversiones de temperatura y calculo de dimensiones en un cubo\n")
print("1) Conversiones de temperatura")
print("2) Calculo de dimensiones en un cubo\n")
print("3) Salir\n")
opcion = int(input("Ingrese la opcion que desea realizar: "))

if opcion == 1:
    print("Bienvenido al programa de conversiones de temperatura\n")
    print("1) Celsius a Fahrenheit")
    print("2) Fahrenheit a Celsius\n")
    print("3) Kelvin a Celsius\n")
    print("4) Celsius a Kelvin\n")
    print("5) Kelvin a Fahrenheit\n")
    print("6) Fahrenheit a Kelvin\n")
    opcion1 = int(input("Ingrese la opcion que desea realizar: "))

    if opcion1 == 1:
        print("Bienvenido al programa de conversion de Celsius a Fahrenheit\n")
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("La temperatura en grados Fahrenheit es: ", fahrenheit)

    elif opcion1 == 2:
        print("Bienvenido al programa de conversion de Fahrenheit a Celsius\n")
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("La temperatura en grados Celsius es: ", celsius)
    
    elif opcion1 == 3:
        print("Bienvenido al programa de conversion de Kelvin a Celsius\n")
        kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
        celsius = kelvin - 273.15
        print("La temperatura en grados Celsius es: ", celsius)

    elif opcion1 == 4:
        print("Bienvenido al programa de conversion de Celsius a Kelvin\n")
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        kelvin = celsius + 273.15
        print("La temperatura en grados Kelvin es: ", kelvin)
    
    elif opcion1 == 5:
        print("Bienvenido al programa de conversion de Kelvin a Fahrenheit\n")
        kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print("La temperatura en grados Fahrenheit es: ", fahrenheit)

    elif opcion1 == 6:
        print("Bienvenido al programa de conversion de Fahrenheit a Kelvin\n")
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print("La temperatura en grados Kelvin es: ", kelvin)

    else:
        print("Favor ingrese una de las opciones desplegadas!\n")

elif opcion == 2:
    print("Bienvenido al programa de calculo de dimensiones en un cubo\n")
    print("1) Calcular el area de un cubo")
    print("2) Calcular el volumen de un cubo\n")
    print("3) calcular el perimetro de un cubo\n")
    print("4) calcular la diagonal de un cubo\n")
    opcion2 = int(input("Ingrese la opcion que desea realizar: "))

    if opcion2 == 1:
        print("Bienvenido al programa de calculo del area de un cubo\n")
        lado = float(input("Ingrese el valor del lado del cubo: "))
        area = 6 * (lado * lado)
        print("El area del cubo es: ", area)

    elif opcion2 == 2:
        print("Bienvenido al programa de calculo del volumen de un cubo\n")
        lado = float(input("Ingrese el valor del lado del cubo: "))
        width = float(input("Ingrese el valor del ancho del cubo: "))
        height = float(input("Ingrese el valor de la altura del cubo: "))
        volumen = lado * width * height
        print("El volumen del cubo es: ", volumen)
    
    elif opcion2 == 3:
        print("Bienvenido al programa de calculo del perimetro de un cubo\n")
        lado = float(input("Ingrese el valor del lado del cubo: "))
        width = float(input("Ingrese el valor del ancho del cubo: "))
        perimetro = lado + width + lado + width
        print("El perimetro del cubo es: ", perimetro)
    
    elif opcion2 == 4:
        print("Bienvenido al programa de calculo de la diagonal de un cubo\n")
        lado = float(input("Ingrese el valor del lado del cubo: "))
        width= float(input("Ingrese el valor del ancho del cubo: "))
        height = float(input("Ingrese el valor de la altura del cubo: "))
        diagonal = (lado *width*2)+(lado*height*2)+(width*height*2)
        print("La diagonal del cubo es: ", diagonal)

    else:
        print("Favor ingrese una de las opciones desplegadas!\n")

elif opcion == 3:
    print("Gracias por utilizar el programa!")

