import Funções as mf

listaClientes = [{'nome': 'Ana', 'idade': 20}, {'nome': 'Maria', 'idade': 30}]

# while True

while True:
    opçoes = input('1 - Cadastrar Clientes\n2 - Buscar Cientes\n3 - Deletar Clientes\n4 - Sair\n')
    print('')
    if opçoes == '4':
        print('Saindo...')
        break
    if opçoes == '1':
        print('-------------- Cadastrar Clientes --------------')
        print('')
    if opçoes == '2':
        print('-------------- Buscar Clientes --------------')
        print('')
    if opçoes == '3':
        print('-------------- Deletar Clientes --------------')
        print('')