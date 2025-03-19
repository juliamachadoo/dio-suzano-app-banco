import textwrap

def menu():
  menu = """\n
  ========= MENU ==========
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [nc] Nova Conta
  [lc] Listar Contas
  [nu] Novo Usuário
  [q] Sair
  => """
  
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor < 0:
      print('O valor de depósito não pode ser negativo, favor informar outro valor: ')
  else:
    saldo += valor
    extrato += f'Depósito: R${valor:.2f}\n'
    print(f'Depósito: {valor:.2f}')
    print(f'Saldo: R${saldo:.2f}')
    print('=== Depósito realizado com Sucesso ===')
    
  return saldo, extrato

def sacar(*, saldo, valor,extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques
  
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
      print('=== Saque realizado com Sucesso ===')
  
  return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
  print('===== EXTRATO =====')
  print('Não foram realizadas movimentações.' if not extrato else extrato)
  print(f'Saldo: R${saldo:.2f}')
  print('====================')

def criar_usuario(usuarios):
  cpf = input('Informe seu CPF (apenas números): ')
  usuario = filtrar_usuarios(cpf, usuarios)
  
  if usuario:
    print('Usuário já cadastrado nesse CPF')
    return
    
  nome = input('Digite seu nome completo: ')
  data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa): ')
  endereco = input('Informe o seu endereço (logradouro, nro - bairro - cidade/Sigla Estado): ')
  
  usuarios.append({
    "nome": nome,
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereco": endereco,
  })
  
  print("=== Usuário criado com sucesso ===")
  
def filtrar_usuarios(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']==cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_bancaria(agencia, numero_conta, usuarios):
  cpf = input('Informe seu CPF (apenas números): ')
  usuario = filtrar_usuarios(cpf, usuarios)
  
  if usuarios:
    print('=== Conta criada com Sucesso ===')
    return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print('=== Usuário não encontrado, fluxo de criação de conta encerrado ===')

def listar_contar(contas):
  for conta in contas:
    linha = f"""
    Agência: {conta['agencia']}\n
    C/C: {conta['numero_conta']}\n
    Titular: {conta['usuario']['nome']}
    """
    
    print('='*100)
    print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUE = 3
  AGENCIA = '0001'  
  saldo = 0
  limite=500
  extrato = ""
  numero_saques = 0 
  usuarios =[]
  contas = []
  
  while True:
      opcao = menu()
      
      if opcao == 'd':
        valor = float(input('Valor a ser depositado: '))
        
        saldo, extrato = depositar(saldo, valor,extrato)
      
      if opcao == 's':
        valor = float(input('Valor a ser sacado: '))
        
        saldo, extrato = sacar(
          saldo=saldo,
          valor=valor,
          extrato=extrato,
          limite=limite,
          numero_saques=numero_saques,
          limite_saques=LIMITE_SAQUE,
        )
        
      elif opcao == 'e':
        visualizar_extrato(saldo, extrato=extrato)
        
      elif opcao == 'nu':
        criar_usuario(usuarios)
        
      elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta_bancaria(AGENCIA, numero_conta, usuarios)
        
        if conta:
          contas.append(conta)
      
      elif opcao == 'lc':
        listar_contar(contas)
        
      elif opcao == 'q':
        break
      
      else:
        print('Operação Inválida, por favor selecione novamente a operação desejada')
        
        
main()