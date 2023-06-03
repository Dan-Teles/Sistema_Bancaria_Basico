#Projeto Sistema Bancario Dio
#Daniel Teles da Silva
import os

class Banco:
    def __init__(self) -> None:
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.numero_depositos = 0
        self.LIMITE_SAQUES = 3
        self.n_deposito = {}
        self.n_saque = {}

    def saque(self):
        valor = float(input("Digite o valor do saque: "))
        if self.saldo > valor and self.numero_saques <3:
            while(valor > self.limite):
                valor = float(input("Digite o valor do saque: "))
            self.saldo -= valor
            self.n_saque[self.numero_saques] = valor
            self.numero_saques += 1
        elif self.numero_saques == 3:
            print("Limites de saque diários alcançado!")
            os.system("pause")
        else:
            print("Não será possível sacar por falta de saldo!")
            os.system("pause")

    def deposito(self):
        valor = float(input("Digite o valor do deposito: "))
        self.saldo += valor
        self.n_deposito[self.numero_depositos] = valor
        self.numero_depositos += 1

    def imprimir_extrato (self):
            # percorrer pelo VETOR (n_deposito)
        for i,valor in self.n_deposito.items():
            print(f"Depósito {i} = R${valor:.2f}")
            # percorrer pelo VETOR (n_saque)
        for i,valor in self.n_saque.items():
            print(f"Saque {i} = R${valor:.2f}")
        print(f"\nSaldo Atual: R${valor:.2f}".format(self.saldo))
        os.system("pause")

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

banco = Banco()
while True:
    os.system("cls")
    opcao = input(menu)
    #os.system("cls")
    if opcao == 'd':
        print("Depósito")
        banco.deposito()
    elif opcao == 's':
        print("Saque")
        banco.saque()
    elif opcao == 'e':
        print("Extrato")
        banco.imprimir_extrato()
    elif opcao == 'q':
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
