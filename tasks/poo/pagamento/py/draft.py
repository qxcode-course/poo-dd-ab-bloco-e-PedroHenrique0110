from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self):
        return f"Pagamento de R$: {self.valor}:{self.descricao}"
    
    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("falhou: valor invalidp")
        
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome= nome
        self.limite: float= limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()
    
    def get_limite(self):
        return self.limite
    
    def processar(self):
        if self.valor > self.limite:
            print("Pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def resumo(self) -> str:
        return super().resumo()
    
    def processar(self):
        print(f"Pix enviado de {self.banco} da chave {self.chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def resumo(self) -> str:
        return super().resumo()
    
    def processar(self):
        print("Boleto gerado. Aguardando pagamento")
        print(f"Código de barras: {self.codigo_barras}")
        print(f"Vencimento: {self.vencimento}")

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())
        print()

pagamentos:list[Pagamento] = [
    CartaoCredito(nome = "David", descricao = "Coxinha", limite = 500.00, num = 123, valor = 0.50),
    Pix(descricao = "Salgado", banco = "Santander", chave = "telefone" , valor = 3.50),
    Boleto(descricao = "Enroladinho", codigo_barras = "00000000000000", vencimento = "12/12" , valor = 5.00)
]

processar_pagamentos(pagamentos)

    