
banking-automation-Python

 💼 Sistema de Gestión de Empleados y Cuentas Bancarias

 ✨ Descripción del Proyecto
Este programa en **Python** permite gestionar empleados y sus cuentas bancarias utilizando el paradigma de **Programación Orientada a Objetos (POO)**. Los usuarios pueden ingresar empleados, asignarles cuentas bancarias, realizar depósitos y visualizar su saldo.

El código fue diseñado para ser modular, reutilizable y escalable.

---

 ⚙ Tecnologías Utilizadas
- **Python 3**
- **Paradigma POO**
- **Interacción con el usuario a través de input/output**

---

 📝 Paso a Paso del Desarrollo del Código
 1. **Diseño de la Estructura**
Se plantearon tres clases principales:
- `Persona`: Clase base para empleados.
- `Empleado`: Hereda de `Persona` y añade información laboral.
- `CuentaBancaria`: Maneja el saldo y transacciones bancarias.

Se definió un **`main()`** para la ejecución del programa, permitiendo la interacción con el usuario.

### 2. **Implementación del Código**
1. **Clase `Persona`**: Define el nombre y la edad.
2. **Clase `Empleado`**: Extiende `Persona` y agrega puesto y salario.
3. **Clase `CuentaBancaria`**: Gestiona saldo y transacciones bancarias.
4. **Función `main()`**:
   - Pide al usuario los datos del empleado y crea un objeto `Empleado`.
   - Solicita el saldo inicial y crea una `CuentaBancaria`.
   - Permite hacer depósitos interactivos.
   - Muestra el saldo final.
5. **Bloque `if __name__ == "__main__":`** para ejecutar el código principal si el archivo se ejecuta directamente.

---

## 🔍 Explicación del Código Paso a Paso

### **1. Definimos la Clase `Persona`**
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."
```
**✔ Explicación**:
- `__init__()` inicializa `nombre` y `edad`.
- `presentar()` retorna una presentación básica.

 **2. Definimos la Clase `Empleado` (Hereda de `Persona`)**
```python
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto, salario):
        super().__init__(nombre, edad)
        self.puesto = puesto
        self.salario = salario

    def info_empleado(self):
        return f"{self.presentar()} Trabajo como {self.puesto} y gano ${self.salario}."
```
**✔ Explicación**:
- Usa `super().__init__()` para heredar `nombre` y `edad`.
- Agrega `puesto` y `salario`.
- `info_empleado()` devuelve la información laboral del empleado.

 **3. Definimos la Clase `CuentaBancaria`**
```python
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
```
**✔ Explicación**:
- `__init__()` inicializa el saldo con valor predeterminado `0`.
- `depositar(monto)` añade dinero si el monto es válido.
- `ver_saldo()` devuelve el saldo actual.

 **4. Implementamos `main()` para la Interacción con el Usuario**
```python
def main():
    # Solicitar datos del empleado
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    puesto = input("Ingrese el puesto del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))

    empleado1 = Empleado(nombre, edad, puesto, salario)
    print("\n" + empleado1.info_empleado())

    # Crear la cuenta bancaria
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta1 = CuentaBancaria(nombre, saldo_inicial)
    print(cuenta1.ver_saldo())

    # Ciclo de depósitos
    while True:
        opcion = input("\n¿Desea hacer un depósito? (s/n): ").lower()
        if opcion == "s":
            monto = float(input("Ingrese el monto a depositar: "))
            print(cuenta1.depositar(monto))
        else:
            print("Operación finalizada.")
            break
    print(cuenta1.ver_saldo())

if __name__ == "__main__":
    main()
```

**✔ Explicación**:
1. **Solicita datos del empleado** y crea un objeto `Empleado`.
2. **Solicita saldo inicial** y crea `CuentaBancaria`.
3. **Bucle `while True`** permite hacer depósitos hasta que el usuario elija salir.
4. **`if __name__ == "__main__":`** ejecuta `main()` solo si el archivo es el principal.

---

 🏆 Características del Proyecto
✅ Entrada de datos dinámica desde el teclado.  
✅ Estructura modular con POO.  
✅ Permite realizar múltiples depósitos.  
✅ Implementa herencia entre clases.  

---

 🛠 Posibles Mejoras Futuras
- ✅ **Agregar funcionalidad para retiros de dinero.**
- ✅ **Permitir gestionar múltiples empleados y cuentas.**
- ✅ **Guardar y cargar datos desde un archivo o base de datos.**

---

 💪 Contribuciones 
Si deseas mejorar este proyecto, podés hacer un **fork** y enviar un **pull request** en GitHub.

---

🎉 **¡Gracias por revisar este proyecto!**

