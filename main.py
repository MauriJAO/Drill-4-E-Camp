from clases import Automovil

nautomovil = []

n = int(input("Cuantos Vehículos desea insertar: "))
print("")
for i in range(n):
    print(f"Datos del automovil {i+1}")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el Modelo: ")
    numero_ruedas = int(input("Inserte el numero de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    auto = Automovil(marca,modelo,numero_ruedas,velocidad,cilindrada)
    nautomovil.append(auto)

print("Imprimiendo por la pantalla los Vehículos")

for index,item in enumerate(nautomovil):
    print(f"Datos del automovil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.numero_ruedas} ruedas, {item.velocidad} Km/h, {item.cilindrada} cc")