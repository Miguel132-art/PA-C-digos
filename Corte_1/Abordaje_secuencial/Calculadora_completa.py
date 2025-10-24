class Calculadora:
    "Calculadora Basica OOP"
    
    def __init__(self):
        """Inicializar la calculadora"""
        self.resultado = 0
    
    # Operaciones básicas
    def sumar(self, a, b):
        """Suma de dos numeros"""
        self.resultado = a + b
        return self.resultado
    
    def restar(self, a, b):
        """Resta de dos números"""
        self.resultado = a - b
        return self.resultado
    
    def multiplicar(self, a, b):
        """Multiplicacion de dos numeros"""
        self.resultado = a * b
        return self.resultado
    
    def dividir(self, a, b):
        """Divicion de dos numeros"""
        if b == 0:
            return "Error: Division por cero"
        self.resultado = a / b
        return self.resultado
    
    # Operaciones extras
    def potencia(self, base, exponente):
        """Calcular la potencia de un numero"""
        self.resultado = 1
        if exponente >= 0:
            for _ in range(exponente):
                self.resultado *= base
        else:
            for _ in range(abs(exponente)):
                self.resultado *= base
            self.resultado = 1 / self.resultado
        return self.resultado
    
    def raiz_cuadrada(self, numero):
        """Calcular la raiz cuadrada usando el metodo de Newton"""
        if numero < 0:
            return "Error: No se puede calcular raiz cuadrada de numero negativo"
        if numero == 0:
            return 0
        
        # Metodo de Newton para raiz cuadrada
        x = numero
        epsilon = 0.00001
        while True:
            raiz = 0.5 * (x + numero / x)
            if abs(raiz - x) < epsilon:
                break
            x = raiz
        
        self.resultado = raiz
        return self.resultado
    
    def factorial(self, n):
        """Calcular el factorial de un numero"""
        if n < 0:
            return "Error: El factorial no esta definido para numeros negativos"
        if n == 0 or n == 1:
            self.resultado = 1
            return self.resultado
        
        self.resultado = 1
        for i in range(2, n + 1):
            self.resultado *= i
        return self.resultado


class CalculadoraGeometrica(Calculadora):
    """Calculadora para areas geometricas"""
    
    def __init__(self):
        """Inicializa la calculadora geométrica"""
        super().__init__()
        self.pi = 3.141592653589793
    
    def area_cuadrado(self, lado):
        """Calcula el area de un cuadrado"""
        if lado < 0:
            return "Error: El lado no puede ser negativo"
        self.resultado = self.multiplicar(lado, lado)
        return self.resultado
    
    def area_rectangulo(self, base, altura):
        """Calcula el area de un rectangulo"""
        if base < 0 or altura < 0:
            return "Error: Las dimensiones no pueden ser negativas"
        self.resultado = self.multiplicar(base, altura)
        return self.resultado
    
    def area_circunferencia(self, radio):
        """Calcula el area de una circunferencia"""
        if radio < 0:
            return "Error: El radio no puede ser negativo"
        radio_cuadrado = self.multiplicar(radio, radio)
        self.resultado = self.multiplicar(self.pi, radio_cuadrado)
        return self.resultado
    
    def area_triangulo_rectangulo(self, base, altura):
        """Calcula el area de un triangulo rectangulo"""
        if base < 0 or altura < 0:
            return "Error: Las dimensiones no pueden ser negativas"
        # area = (base * altura) / 2
        area = self.multiplicar(base, altura)
        self.resultado = self.dividir(area, 2)
        return self.resultado


# Programa principal
def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("CALCULADORA CIENTÍFICA Y GEOMÉTRICA")
    print("="*50)
    print("\nOperaciones Básicas:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("\nOperaciones Avanzadas:")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("\nÁreas Geométricas:")
    print("8. Área de cuadrado")
    print("9. Área de rectángulo")
    print("10. Área de circunferencia")
    print("11. Área de triángulo rectángulo")
    print("\n0. Salir")
    print("="*50)


def main():
    """Funcion principal del programa"""
    calc = CalculadoraGeometrica()
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSelecciona una opción: "))
            
            if opcion == 0:
                print("\ncalculadora cerrada")
                break
            
            elif opcion == 1:
                a = float(input("Primer numero: "))
                b = float(input("Segundo numero: "))
                print(f"Resultado: {calc.sumar(a, b)}")
            
            elif opcion == 2:
                a = float(input("Primer numero: "))
                b = float(input("Segundo numero: "))
                print(f"Resultado: {calc.restar(a, b)}")
            
            elif opcion == 3:
                a = float(input("Primer numero: "))
                b = float(input("Segundo numero: "))
                print(f"Resultado: {calc.multiplicar(a, b)}")
            
            elif opcion == 4:
                a = float(input("Numerador: "))
                b = float(input("Denominador: "))
                print(f"Resultado: {calc.dividir(a, b)}")
            
            elif opcion == 5:
                base = float(input("Base: "))
                exp = int(input("Exponente: "))
                print(f"Resultado: {calc.potencia(base, exp)}")
            
            elif opcion == 6:
                num = float(input("Numero: "))
                print(f"Resultado: {calc.raiz_cuadrada(num)}")
            
            elif opcion == 7:
                n = int(input("Numero: "))
                print(f"Resultado: {calc.factorial(n)}")
            
            elif opcion == 8:
                lado = float(input("Lado del cuadrado: "))
                print(f"area: {calc.area_cuadrado(lado)}")
            
            elif opcion == 9:
                base = float(input("Base del rectangulo: "))
                altura = float(input("Altura del rectangulo: "))
                print(f"area: {calc.area_rectangulo(base, altura)}")
            
            elif opcion == 10:
                radio = float(input("Radio de la circunferencia: "))
                print(f"area: {calc.area_circunferencia(radio)}")
            
            elif opcion == 11:
                base = float(input("Base del triangulo: "))
                altura = float(input("Altura del triangulo: "))
                print(f"area: {calc.area_triangulo_rectangulo(base, altura)}")
            
            else:
                print("Opcion no valida. Intenta de nuevo.")
        
        except ValueError:
            print("Error: Debes ingresar un numero valido.")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
