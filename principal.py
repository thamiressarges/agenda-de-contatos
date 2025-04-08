from agenda import adicionar_contato, ver_contatos, deletar_contato

def main():
    while True:
        print('\nAgenda de Conatatos')
        print('1. Adicionar Contato')
        print('2. Listar Contatos')
        print('3. Remover Contatos')
        print('4. Sair')

        escolha = input('Escolha uma opção (1-4)\n')
        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            ver_contatos()
        elif escolha == '3':
            deletar_contato()
        elif escolha == '4': 
            break
        else:
            print('Informe uma opção válida')

main()