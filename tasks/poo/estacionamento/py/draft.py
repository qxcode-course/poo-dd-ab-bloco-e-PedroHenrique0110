from abc import ABC, abstractmethod
from typing import Dict

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.entrada = 0

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
        return f"{tipo_f} : {id_f} : {self.entrada}"
    
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
        self.hora_atual = 0

    def procurarVeiculo(self, id: str):
        if id in self.veiculos:
            return self.veiculos[id].getEntrada()
        return -1
    
    def estacionar(self, veiculo: Veiculo):
        if veiculo.getId() in self.veiculos:
            print(f"Veiculo {veiculo.getId()} ja esta estacionado")
            return
        veiculo.setEntrada(self.hora_atual)
        self.veiculos[veiculo.getId()] = veiculo


    def pagar(self, id: str):
        if id not in self.veiculos:
            print(f"Veiculo nao encontrado")
            return
        veiculo = self.veiculos[id]
        valor = veiculo.calcularValor(self.hora_atual)

        tipo = veiculo.getTipo()
        entrada = veiculo.getEntrada()
        saida = self.hora_atual

        print(f"{tipo} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")

    def sair(self, id: str):
        if id not in self.veiculos:
            print(f"Veiculo {id} nao encontrado")
            return
        veiculo = self.veiculos[id]
        valor = veiculo.calcularValor(self.hora_atual)
        del self.veiculos[id]

    def passarTempo(self, tempo: int):
        self.hora_atual += tempo

    def __str__(self):
        if not self.veiculos:
            return f"Hora atual: {self.hora_atual}"
        
        resultado = [ ]
        for veiculo in self.veiculos.values():
            resultado.append(str(veiculo))
        resultado.append(f"Hora atual: {self.hora_atual}")
        
        return "\n".join(resultado)
    
def main():
    estacionamento = Estacionamento()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "tempo":
            if len(args) < 2:
                print("Uso: tempo <minutos>")
                continue
            try:
                minutos = int(args[1])
                estacionamento.passarTempo(minutos)
            except ValueError:
                print("Erro: O tempo deve ser em minutos")
        elif args[0] == "estacionar":
            if len(args) < 3:
                print("Uso: estacionar <tipo> <id>")
                continue
            tipo = args[1].lower()
            id_veiculo = args[2]
            
            if tipo == "bike":
                veiculo = Bike(id_veiculo)
            elif tipo == "moto":
                veiculo = Moto(id_veiculo)
            elif tipo == "carro":
                veiculo = Carro(id_veiculo)
            else:
                print(f"Erro: Tipo '{tipo}' invalido. Use: bike, moto ou carro")
                continue

            estacionamento.estacionar(veiculo)
        elif args[0] == "pagar":
            if len(args) < 2:
                print("Uso: pagar <id>")
                continue
            estacionamento.pagar(args[1])


main()