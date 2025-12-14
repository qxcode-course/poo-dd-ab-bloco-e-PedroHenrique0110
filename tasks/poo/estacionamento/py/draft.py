from abc import ABC, abstractmethod
from typing import Dict, List

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = 0

    def setEntrada(self, horaEntrada: int):
        self.entrada = horaEntrada

    def getEntrada(self):
        return self.entrada
    
    def getTipo(self):
        return self.tipo
    
    def getId(self):
        return self.id
    
    @abstractmethod
    def calcularValor(self, horaSaida: int) -> float:
        pass

    def __str__(self):
        tipo_f = self.tipo.rjust(10, '_')
        id_f = self.id.rjust(10, '_')
        return f"{tipo_f} : {id_f} : {self.horaEntrada}"
    
class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, horaSaida: int):
        return 3.00

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int):
        tempo_permanencia = horaSaida - self.entrada
        return tempo_permanencia / 20.0
    
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int):
        tempo_permanencia = horaSaida - self.entrada
        valor = tempo_permanencia / 10.0
        return max(valor, 5)
    
class Estacionamento:
    def __init__(self):
        self.veiculos: Dict[str, Veiculo] = {}