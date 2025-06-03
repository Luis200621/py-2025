def mostrar_menu():
    print("\n📋 MENÚ DE TAREAS")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def mostrar_tareas(tareas):
    if not tareas:
        print("⚠️ No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            mostrar_tareas(tareas)

        elif opcion == "2":
            nueva = input("Escribe la nueva tarea: ")
            tareas.append(nueva)
            print("✅ Tarea agregada.")

        elif opcion == "3":
            mostrar_tareas(tareas)
            try:
                indice = int(input("Número de la tarea a editar: ")) - 1
                if 0 <= indice < len(tareas):
                    nueva = input("Escribe la nueva descripción: ")
                    tareas[indice] = nueva
                    print("✏️ Tarea actualizada.")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("⚠️ Entrada no válida.")

        elif opcion == "4":
            mostrar_tareas(tareas)
            try:
                indice = int(input("Número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    eliminada = tareas.pop(indice)
                    print(f"🗑️ Tarea eliminada: {eliminada}")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("⚠️ Entrada no válida.")

        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
main()
