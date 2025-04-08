class Vehiculo():
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        print(f"La marca de mi vehiculo es {self.marca} y el año es {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo
        print(f"Mi carro es modelo {self.modelo}")

carro = Coche("Ferrari", 2026, "Roma")