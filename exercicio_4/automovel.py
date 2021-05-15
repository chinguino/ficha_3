

class Automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quantidade()

    def autonomia(self):
        return (self.quantidade * 100) / self.consumo

    def abastece(self, n_litros):
        self.quantidade += n_litros
        if self.quantidade > self.capacidade:
            print("erro")
            self.quantidade -= n_litros
        print("abasteceu", n_litros)
        return self.autonomia()

    def percorre(self, n_km):
        percorrido = self.autonomia() * n_km
        if percorrido > self.quantidade:
            self.quantidade -= percorrido
            return self.autonomia
        else:
            print("erro")



