#PROGRAMA COM AS FUNÇÕES DE:
# 1.CONSULTA DO EXTRATO
# 2.EFETUAR DEPOSITO
# 3.SAQUE

class Conta:
	
    cliente = 'admin'
    saldo = 0

    def deposito(self, valor):	
        self.saldo += valor
        self.extrato(valor)

    def saque(self, valor):	
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato(-valor)
        else:
            print('Saldo insuficiente.')
        
    def menu(self):
        print('-' * 30)
        print(f'     MENU')
        print('-' * 30)
        print('Opções:')
        print('1 - Extrato')
        print('2 - Depósito')
        print('3 - Saque')
        print('4 - Sair')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            self.extrato()
        elif opcao == '2':
            valor = float(input('Digite o valor a ser depositado: '))
            self.deposito(valor)
        elif opcao == '4':
            exit()

    def extrato(self, ultimo = 0):
        print()
        print('-' * 40)
        print(f'                EXTRATO           ')
        print('-' * 40)
        print(f'CLIENTE - {self.cliente}')
        print('-' * 40)
        print('LANÇAMENTOS')
        if ultimo > 0:
            print(f' DEPÓSITO ATM |     CRÉDITO {ultimo:.2F} ')
        print('              |                |')
        print('              |                |')
        print('-' * 40)
        print(f'                        SALDO: R$ {self.saldo:.2F}')
        print('-' * 40)
        print('             FIM DO EXTRATO				  ')
        print('-' * 40)
        aperte = input('Aperte ENTER para retornar ao MENU\nou (X e ENTER) para sair: ')
        if aperte == 'X' or aperte == 'x': 
            exit()
        else:
            self.menu()

pessoa = Conta()

while True:
    pessoa.menu()
