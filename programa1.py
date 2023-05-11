from pathlib import Path
import random

print("\t\tBienvenido al Programa 1 de 1214 Sistemas Inteligentes!\n\n")

while True:

    print("Favor Seleccione la opcion de codigo que desea ejecutar:\n\n1) Bases de la funcion Print\n2) Formateo de Strings\n3) Leer Archivo: Prueba1.txt\n4) Operaciones Matematicas Basicas\n5) Registro de Finanzas Personales\n6) Calculo de Estado de Resultado\n7) Calculo de Promedio Trimestral\n\nPara salir del programa favor escribir: Exit\n")
    ncodigo = int(input("Numero de codigo: "))
    #val_float = float(ncodigo)

    #Sintaxis Si <CONDICION>:

    if ncodigo == 1: 

        print("\n\tHola Mundo, mi nombre es Delond!\n")

        fruta1 = "Manzana"
        fruta2 = 'Banano'
        fruta3 = "Durazno"

        print(fruta1, ", ", fruta2, ", ", fruta3, end="\t")
        #print()
        print(fruta1, ", ", fruta2, ", ", fruta3, sep = "", end= ("\t"))
        #print()
        print(fruta1, fruta2, fruta3, sep = ", ", end="\t")
        #print()

        nombre = "Delond"
        apellido = "Jimenez"

        nombre_completo = nombre + " " + apellido

        print(nombre_completo, "\n")

    elif ncodigo == 2:

        print()
        nombre = input("Favor ingrese su nombre: ")
        apellido = input("Favor ingrese su apellido: ")

        print("Posicion 1 {}, Posicion 2: {}".format(nombre, apellido))
        print("Posicion 1 {1:.6f}, Posicion 2: {0:,d}".format(2040505, 12.23456787654))

        print("\nLos datos ingresados son: Nombre = %s, Apellido = %s.\n"%(nombre, apellido), file=(open("Prueba1.csv","a")))
        print("\nLos datos ingresados son: Nombre = %s, Apellido = %s.\n"%(nombre, apellido), file=(open("Prueba1.docx","w")))

    elif ncodigo == 3: 

        print(open("Prueba1.txt").read())

    #operaciones Matematicas basicas
    elif ncodigo == 4:

        numero1 = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese un numero: "))

        #print("String que describa o indique lo que se {} tratando".format(esto))
        suma = numero1 + numero2
        print("la suma de {} + {} es igual a: {}".format(numero1, numero2, suma))
        print("la resta de {} - {} es igual a: {}".format(numero1, numero2, numero1-numero2))
        print("la multi de {} * {} es igual a: {}".format(numero1, numero2, numero1*numero2))
        print("la div de {} / {} es igual a: {}".format(numero1, numero2, numero1/numero2))
        print("la div piso de {} // {} es igual a: {}".format(numero1, numero2, numero1//numero2))
        #print("la resta de {} + {} es igual a: {}".format(numero1, numero2, numero1-numero2))

    elif ncodigo == 5:

        ingreso_mensual = float(input("\ningrese su el monto de su ingreso mensual(HNL): "))

        print("\n\nSeleccione el plan que desea utilizar para el manejo de sus ingresos mensuales:\n\n1)Plan Arbitrario\n2)Plan Leo\n3)Plan Marco")

        ncodigo_a = int(input("\nOpcion deseada: "))

        if ncodigo_a == 1:

            path_file = Path("RegistroFinanzasPersonales.txt")
            porcentaje = 0

            mes = input("\nIngrese el mes actual: ")

            while True:

                inversion = (float(input("\nDefine el porcentaje destinado a Inversion: ")))/100
                ahorro = (float(input("Define el porcentaje destinado a Ahorro: ")))/100
                gastos = (float(input("Define el porcentaje destinado a Gastos: ")))/100
                personal = (float(input("Define el porcentaje destinado a Uso Personal: ")))/100
                remesas = (float(input("Define el porcentaje destinado a Remesas o Envios Familiares: ")))/100

                porcentaje = inversion + ahorro + gastos + personal + remesas
                print(porcentaje)

                if porcentaje == 1: 
                    break
                else: 
                    continue

            if Path.is_file(path_file):

                print("------------------------------------------------------------------------------------------------------------------------", file=(open("RegistroFinanzasPersonales.txt","a")))
                print("Ingreso mensual: {0:,.2f}".format(ingreso_mensual),file=(open("RegistroFinanzasPersonales.txt","a")))
                print("Actualizacion: {:s}\nInversion = HNL {:,.2f} |Ahorro = HNL {:,.2f} |Gastos = HNL {:,.2f} |Personal = HNL {:,.2f} |Remesas = HNL {:,.2f}".format(mes, ingreso_mensual*inversion, ingreso_mensual*ahorro, ingreso_mensual*gastos, ingreso_mensual*personal,ingreso_mensual*remesas), file=(open("RegistroFinanzasPersonales.txt","a")))
                #print("Anexado")
            else: 

                print("Ingreso mensual: {0:,.2f}".format(ingreso_mensual),file=(open("RegistroFinanzasPersonales.txt","a")))
                print("Actualizacion: {:s}\nInversion = HNL {:,.2f} |Ahorro = HNL {:,.2f} |Gastos = HNL {:,.2f} |Personal = HNL {:,.2f} |Remesas = HNL {:,.2f}".format(mes, ingreso_mensual*inversion, ingreso_mensual*ahorro, ingreso_mensual*gastos, ingreso_mensual*personal,ingreso_mensual*remesas), file=(open("RegistroFinanzasPersonales.txt","w")))
                #print("Creado")
            print()

        else:

            print("Favor ingrese una de las opciones desplegadas!\n")

    elif ncodigo == 6:
         #calcular de manera eficiente la utilidad o la perdida neta de una empresa
         # 1) Ingresar el valor de las ventas
         # 2) Ingresar el valor de los costos
         # 3) Ingresar el valor de los gastos
         # 4) Calcular la utilidad o perdida neta
         # 5) Imprimir el resultado
         # 6) Imprimir el resultado en un archivo de texto

        print("Bienvenido al programa de calculo de utilidad o perdida neta de una empresa\n")

        ventas = float(input("Ingrese el valor de las ventas: "))
        costos = float(input("Ingrese el valor de los costos: "))
        gastos = float(input("Ingrese el valor de los gastos: "))
        otrosgastos = float(input("Ingrese el valor de otros gastos: "))
        utilidad = ventas - costos - gastos- otrosgastos

        #if utilidad > 0:
         #   print("La empresa obtuvo una utilidad neta de: HNL {:,.2f}".format(utilidad))
        #elif utilidad < 0:
          #  print("La empresa obtuvo una perdida neta de: HNL {:,.2f}".format(utilidad))
       
        print("La empresa obtuvo una utilidad neta de: HNL {:,.2f}".format(utilidad), file=(open("UtilidadPerdidaNeta.txt","w")))

    elif ncodigo == 7:
        #programa que calcule la nota d eun alumno, si esta aprueba o reprueba
        # ingresar la bienvenida al programa
        # ingresar el nombre del alumno
        # ingresar la nota del alumno
        # calcular la nota del alumno
        # imprimir el resultado

        # print("Bienvenido al programa de calculo de nota de un alumno\n")
        # nombre = input("Ingrese el nombre del alumno: ")
        # no_clases = int(input("Ingrese el numero de clases registradas en el periodo: "))
        # notas={}
        # while no_clases > 0:
        #     nombre_clase = input("Ingrese el nombre de la clase: ")
        #     nota_clase= float(input("Ingrese la nota de la clase: "))
        #     notas[nombre_clase]=nota_clase
        #     #calcular promedio
        #     nota_final = sum(notas.values())/len(notas)
        #     no_clases-=1
        # else:
        #     print("Ha realizado de forma exitosa su calculo de promedio trimestral\n")

        # print("El promedio del alumno es: ", nota_final)
        # print(notas)

        # mejor_nota = max(notas.values())
        # print("La mejor nota del alumno es: ", mejor_nota)

        print("\n--- CALCULADORA DE PROMEDIO TRIMESTRAL ---\n")
        no_clases = int(input("Ingrese el número de clases registradas en el periodo: "))
        
        clase_notas = {}
        classes = []
        notas = []

        while no_clases > 0:

            nombre_clase = input("Ingrese el nombre de clase: ")
            classes.append(nombre_clase)
            nota_clase = float(input("ingrese la nota de clase: "))
            notas.append(nota_clase)
            clase_notas[nombre_clase] = nota_clase
            no_clases -= 1
        
        else: 
            
            print("Ha realizado de forma exitosa su calculo de promedio trimestral")

        promedio = (sum(notas))/len(notas)
        mejor_nota = max(notas)

        index_val = 0

        for i, nota in enumerate(notas):

            if nota == mejor_nota:

                index_val = i

            else: 
                continue

        clase_mejor_nota = classes[index_val]


        print(clase_notas)
        print(classes)
        print(notas)
        print("Promedio: {0:.2f}".format(promedio))
        print("Promedio: {0:.2f}".format(mejor_nota))
        print("Promedio: {0:s}".format(clase_mejor_nota))

        if promedio >= 60 and promedio < 70:
            print("El alumno ha aprobado el trimestre con un promedio de: {0:.2f}".format(promedio))
        elif promedio >=70 and promedio < 80:
            print("El alumno ha aprobado el trimestre con un promedio de: {0:.2f}".format(promedio))
        elif promedio >= 80 and promedio < 90:
            print("El alumno ha aprobado el trimestre con un promedio de: {0:.2f}".format(promedio))
        elif promedio >= 90 and promedio <= 100:
            print("El alumno ha aprobado el trimestre con un promedio de: {0:.2f}".format(promedio))
        else:
            print("El alumno ha reprobado el trimestre con un promedio de: {0:.2f}".format(promedio))

    elif ncodigo == 8:

        print("Valor aleatorio={}",format(random.ranndom()))

        listaA=["Karol", "Miguel", "Juan", "Pedro", "Maria", "Jose"]
        print(listaA)
        random.shuffle(listaA)
        print(listaA)

        val=1
        while val <= 4:
            print(listaA)
            nombre=random.choices(listaA,[0.50,0.05,0.05,0.05,0.05,0.05])
            print("Menos 1 pt para={}".format(random.choices(listaA)))
            listaA.remove(nombre[0])
            val+=1
        else:
            print("Mas 1 pt para {}".format(random.choices(listaA[0])))


    elif ncodigo == "Exit" or ncodigo == "exit" or ncodigo == "Salir" or  ncodigo == "salir":
        break

    else: 
        print('''Hello World!
            My name is James and 
            I am 20 years old''')
        
        print("Favor ingrese una de las opciones desplegadas!\n")