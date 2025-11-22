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
    print("Ingrese si la persona está presente, llegó tarde o ausente ")
    print("1. Presente")
    print("2. Llegó tarde")
    print("3. Ausente")

   estado = {
        1: "presente",
        2: "llega tarde",
        3: "ausente"
    }

    llegada = 0
    # Bucle de validación de entrada
    while llegada not in estado:
        try:
            llegada = int(input("Su opción: "))
            if llegada not in estado:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (1, 2 o 3).")
    # Obtiene la cadena de estado ('presente', 'llega tarde', 'ausente').
    status_string = estado[llegada]
    print(f"Ingresado al sistema {nombre} {apellido}, asistencia: {status_string}")

    try:
        with open("asistencia.txt", "a") as archivo:
            archivo.write(f"{nombre},{apellido},{status_string}\n")
        print("Registro guardado exitosamente.")
    except IOError:
        print("Error al escribir en el archivo de asistencia.")
