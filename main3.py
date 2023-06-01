from clases import Vehiculo, Automovil, Bicicleta, Particular, Carga, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
particular2 = Particular("Ford","Bronco",4,"180","2500",7)

#Guardar datos en archivo csv

particular.guardar_datos()
carga.guardar_datos()
bicicleta.guardar_datos()
motocicleta.guardar_datos()
particular2.guardar_datos()

print("--------------------------------------------")
#Leer datos de archivo csv
particular.leer_datos()
carga.leer_datos()
bicicleta.leer_datos()
motocicleta.leer_datos()


