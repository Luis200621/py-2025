def mostrar_menu():
    print("\n🏦 CAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def cajero():
    saldo = 1000.0  # Saldo inicial

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            print(f"💳 Tu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                ingreso = float(input("¿Cuánto deseas ingresar?: $"))
                if ingreso > 0:
                    saldo += ingreso
                    print(f"✅ Ingresaste ${ingreso:.2f}. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("⚠️ El monto debe ser mayor que 0.")
            except ValueError:
                print("⚠️ Entrada inválida. Usa números.")

        elif opcion == "3":
            try:
                retiro = float(input("¿Cuánto deseas retirar?: $"))
                if retiro <= 0:
                    print("⚠️ El monto debe ser mayor que 0.")
                elif retiro > saldo:
                    print("❌ No tienes suficiente saldo.")
                else:
                    saldo -= retiro
                    print(f"✅ Retiraste ${retiro:.2f}. Nuevo saldo: ${saldo:.2f}")
            except ValueError:
                print("⚠️ Entrada inválida. Usa números.")

        elif opcion == "4":
            print("👋 ¡Gracias por usar el cajero!")
            break

        else:
            print("⚠️ Opción no válida.")

# Ejecutar el programa
cajero()
