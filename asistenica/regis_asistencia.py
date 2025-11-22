# =================================================================
# REGISTRO SIMPLE DE ASISTENCIA
# Script en Python para registrar, mostrar y eliminar la asistencia
# de personas usando un archivo de texto (asistencia.txt).
# =================================================================
# Ingreso de personas con nombre y apellido, ademas de su asistencia
def ingreso_asistencia():
    #El strip elimina los espacios en blanco iniciales y finales (por ejemplo, " Juan " se convierte en "Juan")
    #El capitalize convierte la primera letra de la cadena a mayúscula y el resto a minúscula (por ejemplo, "pedro" o "PEDRO" se convierte en "Pedro").
    nombre = str(input("Ingrese su nombre: ")).strip().capitalize()
    apellido = str(input("Ingrese su apellido: ")).strip().capitalize()
    print("-"*60)
    asistencia=int(input("Ingrese si la persona está presente, llegó tarde o ausente "))
    print("1. Presente")
    print("2. Llegó tarde")
    print("3. Ausente")

    if asistencia== 1:
        print(f"Ingresado al sistema {nombre} {apellido},estado: presente")
    elif asistencia== 2:
        print(f"Ingresado al sistema {nombre} {apellido},estado: llega tarde")
    elif asistencia ==3:
        print(f"Ingresado al sistema {nombre} {apellido},estado: ausente")
    else:
        print("error, por favor ingrese una opción válida")
ingreso_asistencia()
