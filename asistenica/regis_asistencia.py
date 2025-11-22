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

def mostrar_asistencia():

    try:
    # Abre el archivo en modo "r" (read/lectura).
        with open("asistencia.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda como una lista de strings.
            asistentes = archivo.readlines()
            if asistentes:
                print("\n--- Lista de asistentes ---")
            # Enumerate() da tanto el índice (i) como el valor (persona_line) para numerar la lista.
                for i, persona_line in enumerate(asistentes):
                    try:
                        nombre, apellido, asistencia = persona_line.strip().split(',')
                        print(f"{i+1}. Nombre: {nombre}, Apellido: {apellido}, Asistencia: {asistencia}")
                    except ValueError:
                    # Captura si una línea no tiene el formato esperado (ej. faltan comas).
                        print(f"Error: Línea mal formateada en el archivo: {persona_line.strip()}")
                print("-"*60)
            else:
                print("No hay asistentes registrados aún.")
        # Devuelve la lista de asistentes (útil para la función eliminar_asistencia).
        return asistentes
    except FileNotFoundError:
        print("No hay registros de asistencia aún.")
        return []
    except IOError:
        print("Error al leer el archivo de asistencia.")
        return []

def eliminar_asistencia():
    asistentes = mostrar_asistencia()
    if not asistentes:
        return

    while True:
        try:
            seleccion = int(input("Ingrese el número del registro a eliminar (0 para cancelar): "))
            if seleccion == 0:
                print("Eliminación cancelada.")
                return
            if 1 <= seleccion <= len(asistentes):
                registro_a_eliminar = asistentes.pop(seleccion - 1)
                try:
#With open para evitar fuga y corrupción de datos
                    with open("asistencia.txt", "w") as archivo:
                        archivo.writelines(asistentes)
                    print(f"Registro '{registro_a_eliminar.strip()}' eliminado exitosamente.")
                except IOError:
                    print("Error al escribir en el archivo de asistencia después de eliminar.")
                return
            else:
                print("Número de registro inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

#definimos el menu, ademas de poner un while para entrar en un bucle donde el usuario deba elegir las opciones 1, 2, 3 o 4
def menu():
    try:
      while True:
        print("-"*60)
        print("Bienvenido al Registrador S-S,por favor seleccione una opción ")
        print("1. Ingresar asistencia")
        print("2. Mostrar asistencia")
        print("3. Eliminar asistencia")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingreso_asistencia()
        elif opcion == "2":
            mostrar_asistencia()
        elif opcion == "3":
            eliminar_asistencia()
        elif opcion == "4":
            print("="*60)
            print("Muchas gracias por usar el Registrador S-S, Cerrando el programa")
            break
        else:
            print("Opción inválida. Por favor, ingrese de nuevo (1, 2, 3 o 4).")
    except Exception as e:
        print(f"Ocurrió un error inesperado en el menú: {e}")

# Bloque principal para ejecutar el menú
menu()
