class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []

    def deposito(self, valor): #função usada para deposito
        if valor > 0: #condição para garantir que o sque não seja negativo
            self.saldo += valor #incremento para toda vez que for feito um deposito, o valor do deposito seja somado com o saldo existente na conta
            self.depositos.append(valor)
            return True
        else:
            print("Erro: O valor do depósito deve ser positivo.")
            return False

    def saque(self, valor): #função usada para saque
        if valor > 0 and valor <= 500 and len(self.saques) < 3:#condição para ser saque m aior que 0 e menor que 500 para limitar e no máximo 3 saques por dia
            if self.saldo >= valor:#condição que verifica se existe saldo para saque e se o valor do saque não extrapola o saldo
                self.saldo -= valor# subtrai(decremento) valor do saque ba conta
                self.saques.append(valor)# conta quantos saques foram feitos
                return True
            else:
                print("Erro: Saldo insuficiente para o saque.")
                return False
        else:
            print("Erro: Saque inválido. Verifique o valor ou o limite diário.")
            return False

    def extrato(self): #função usada para extrato bancário
        extrato = ["Extrato:"]
        for deposito in self.depositos:
            extrato.append(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            extrato.append(f"Saque: R$ {saque:.2f}")
        extrato.append(f"Saldo atual: R$ {self.saldo:.2f}")
        return "\n".join(extrato)


# Exemplo de uso do sistema
conta = ContaBancaria()

while True:
    opcao = input("""
----------------Banco Diome-----------------

    Qual operação deseja fazer?
        [1] Saque
        [2] Depósito
        [3] Extrato
        [0] Sair

----------------Banco Diome-----------------
        Escolha a opção (0/1/2/3): """)

    if opcao == "1":
        valor = float(input("Quanto deseja sacar? "))
        if conta.saque(valor):
            print("Saque realizado com sucesso.")
        else:
            print("Falha ao realizar o saque.")

    elif opcao == "2":
        valor = float(input("Quanto deseja depositar? "))
        if conta.deposito(valor):
            print("Depósito realizado com sucesso." + conta.extrato())
        else:
            print("Falha ao realizar o depósito.")

    elif opcao == "3":
        extrato = conta.extrato()
        print(extrato)

    elif opcao == "0":
        print("Operação finalizada.")
        break

    else:
        print("Opção inválida. Tente novamente.")