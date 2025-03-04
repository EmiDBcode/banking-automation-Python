class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

class Empleado(Persona):  # Hereda de Persona
    def __init__(self, nombre, edad, puesto, salario):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.puesto = puesto
        self.salario = salario

    def info_empleado(self):
        return f"{self.presentar()} Trabajo como {self.puesto} y gano ${self.salario}."

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "El monto debe ser mayor a 0."

    def ver_saldo(self):
        return f"Saldo de {self.titular}: ${self.saldo}"

def main():
    # Solicitar datos al usuario
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    puesto = input("Ingrese el puesto del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))

    # Crear empleado con los datos ingresados
    empleado1 = Empleado(nombre, edad, puesto, salario)
    print("\n" + empleado1.info_empleado())

    # Crear cuenta bancaria asociada
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta bancaria: "))
    cuenta1 = CuentaBancaria(nombre, saldo_inicial)
    print(cuenta1.ver_saldo())

    # Permitir depósitos interactivos
    while True:
        opcion = input("\n¿Desea hacer un depósito? (s/n): ").lower()
        if opcion == "s":
            monto = float(input("Ingrese el monto a depositar: "))
            print(cuenta1.depositar(monto))
        else:
            print("Operación finalizada.")
            break

    # Mostrar saldo final
    print(cuenta1.ver_saldo())

if __name__ == "__main__":
    main()
