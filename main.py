def mostrar_menu():
    print('=== Menu ===')
    print('1 - Ver Mensagem')
    print('0 - Sair')

def mostrar_mensagem():
    print('Bem-vindo!')

mostrar_menu()
opção = input('Escolha: ')

if opção == '1':
    mostrar_mensagem()
elif opção == '0':
    print('Encerrando...')
else:
    print('Opção inválida')
