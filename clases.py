import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas) :
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def guardar_datos(self):
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe el archivo")
        except Exception as e:
            print("Error reportado: ",e)

    def leer_datos(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehiculos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print(item[1])
        except FileNotFoundError:
            print("No existe el archivo")
        except Exception as e:
            print("Error reportado: ",e)


    def __str__(self):
        return f" Marca {self.marca}, Modelo {self.modelo}, numero_ruedas {self.numero_ruedas} "

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f"{self.velocidad}, {self.cilindrada}"

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puesto):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puesto = numero_puesto

    def get_numero_parte(self):
        return self.numero_puesto
    
    def set_numero_parte(self, numero_puesto_new ):
        self.numero_puesto = numero_puesto_new

    def __str__(self):
        return Automovil.__str__(self) + f" Numero de puestos: {self.numero_puesto}"

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return Automovil.__str__(self) + f" Peso de carga: {self.peso_carga}"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + f" Tipo: {self.tipo}"
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, numero_radio, motor, cuadro):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.numero_radio = numero_radio
        self.motor = motor
        self.cuadro = cuadro

    def __str__(self):
        return Bicicleta.__str__(self) + f" Motor: {self.motor}, Cuadro: {self.cuadro}, Numero de radio: {self.numero_radio}"

    