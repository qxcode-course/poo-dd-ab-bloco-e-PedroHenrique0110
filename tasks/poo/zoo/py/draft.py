from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Grilo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Cri Cri! Cri Cri!")

    def mover(self):
        print("Pulando pela grama")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Shhhhhhhh Shhhhhhhh")

    def mover(self):
        print("Se arrastando pela savana")

class Pombo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Pruuu! Pruuu!")

    def mover(self):
        print("Voando por aí")

class Galo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Cocorico Cocorico")

    def mover(self):
        print("Ciscando no galinheiro")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Especie: {type(animal).__name__}")
    print()

animais: list[Animal] = [
    Grilo("Arnaldo"),
    Cobra("Suzane"),
    Pombo("Rodolfo"),
    Galo("Legolas")
]

for animal in animais:
    apresentar(animal)