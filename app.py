menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
valor_max_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
  opcao = input(menu)
  
  if opcao == 'd':
    print('Deposito: ')
    valor = float(input('Qual o valor você deseja depositar? '))
    
    if valor < 0:
      print('O valor de depósito não pode ser negativo, favor informar outro valor: ')
    else:
      saldo += valor
      extrato += f'Depósito: R${valor:.2f}\n'
      print(f'Depósito: {valor:.2f}')
      print(f'Saldo: R${saldo:.2f}')
      
  
  elif opcao == 's':
    print('Sacar: ')
    valor = float(input('Qual o valor você deseja sacar? '))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > valor_max_saque
    excedeu_saques = numero_saques >= LIMITE_SAQUE
    
    if excedeu_saldo:
      print('Operação falhou. Você não tem saldo suficiente para realizar esse saque.')
    elif excedeu_limite:
      print('Operação falhou. O valor do saque excede o limite')
    elif excedeu_saques:
      print('Operação falhou. Você excedeu o número de saques permitidos')
      
    elif valor > 0:
      saldo -= valor
      numero_saques += 1
      extrato += f'Saque: R${valor:.2f}\n'
      print(f'Saque: {valor:.2f}')
      print(f'Saldo: R${saldo:.2f}')
      
  elif opcao == 'e':
    print('===== EXTRATO =====')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}')
    print('====================')
  
  elif opcao == '0':
    break
  
  else:
    print('Opção invalida, favor escolher a opção desejada')
  