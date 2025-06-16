from sympy import symbols, Poly, factor
import sympy

x = symbols('x')

class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = [round(c, 2) for c in coeficientes]
        self.poly = Poly.from_list(list(reversed(self.coeficientes)), x)

    def evaluar(self, valor):
        resultado = sum(c * (valor ** i) for i, c in enumerate(self.coeficientes))
        return round(resultado, 2)

    def derivar(self):
        derivada_coef = [round(i * c, 2) for i, c in enumerate(self.coeficientes)][1:]
        return Polinomio(derivada_coef if derivada_coef else [0])

    def __add__(self, otro):
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        nuevos = [
            round((self.coeficientes[i] if i < len(self.coeficientes) else 0) +
                  (otro.coeficientes[i] if i < len(otro.coeficientes) else 0), 2)
            for i in range(max_len)
        ]
        return Polinomio(nuevos)

    def __sub__(self, otro):
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        nuevos = [
            round((self.coeficientes[i] if i < len(self.coeficientes) else 0) -
                  (otro.coeficientes[i] if i < len(otro.coeficientes) else 0), 2)
            for i in range(max_len)
        ]
        return Polinomio(nuevos)

    def __mul__(self, otro):
        result = [0] * (len(self.coeficientes) + len(otro.coeficientes) - 1)
        for i, a in enumerate(self.coeficientes):
            for j, b in enumerate(otro.coeficientes):
                result[i + j] += a * b
        return Polinomio([round(c, 2) for c in result])

    def dividir(self, otro):
        p1 = Poly.from_list(list(reversed(self.coeficientes)), x)
        p2 = Poly.from_list(list(reversed(otro.coeficientes)), x)
        cociente, residuo = divmod(p1, p2)
        coc = [round(float(c), 2) for c in reversed(cociente.all_coeffs())]
        res = [round(float(c), 2) for c in reversed(residuo.all_coeffs())]
        return Polinomio(coc), Polinomio(res)

    def factorizar(self):
        return factor(self.poly)

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coeficientes):
            if coef == 0:
                continue
            coef_str = f"{coef:.2f}"
            if i == 0:
                terms.append(f"{coef_str}")
            elif i == 1:
                terms.append(f"{coef_str}x")
            else:
                terms.append(f"{coef_str}x^{i}")
        return " + ".join(terms) if terms else "0"

def pedir_coeficientes():
    entrada = input("Introduce los coeficientes separados por comas (de menor a mayor grado):\nEjemplo: 2,3,0,1 para 2 + 3x + x^3\n> ")
    return [float(c.strip()) for c in entrada.split(",")]

def main():
    print("=== Calculadora de Polinomios ===")
    coef = pedir_coeficientes()
    pol = Polinomio(coef)
    print(f"Tu polinomio es: {pol}")

    while True:
        print("\n¿Qué operación deseas realizar?")
        print("1. Evaluar")
        print("2. Derivar")
        print("3. Sumar con otro polinomio")
        print("4. Restar otro polinomio")
        print("5. Multiplicar por otro polinomio")
        print("6. Dividir entre otro polinomio")
        print("7. Factorizar")
        print("8. Salir")
        opcion = input("> ")

        if opcion == "1":
            x_val = float(input("Introduce el valor de x: "))
            print(f"Resultado: {pol.evaluar(x_val)}")

        elif opcion == "2":
            derivada = pol.derivar()
            print(f"Derivada: {derivada}")

        elif opcion in ["3", "4", "5", "6"]:
            print("Introduce el segundo polinomio:")
            coef2 = pedir_coeficientes()
            pol2 = Polinomio(coef2)

            if opcion == "3":
                print(f"Suma: {pol + pol2}")
            elif opcion == "4":
                print(f"Resta: {pol - pol2}")
            elif opcion == "5":
                print(f"Multiplicación: {pol * pol2}")
            elif opcion == "6":
                try:
                    cociente, residuo = pol.dividir(pol2)
                    print(f"Cociente: {cociente}")
                    print(f"Residuo: {residuo}")
                except Exception as e:
                    print("Error en la división:", e)

        elif opcion == "7":
            try:
                print(f"Factorización simbólica: {pol.factorizar()}")
            except Exception as e:
                print("No se pudo factorizar:", e)

        elif opcion == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
