import os

def adicionar_contato():
    nome = input('Informe o seu nome\n')
    endereco = input('Informe o endereço\n')
    telefone = input('Informe o telefone\n')

    contato = f'Nome: {nome}\nEndereço: {endereco}\nTelefone: {telefone}\n\n'

    with open('contatos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(contato)

def ver_contatos():
    if not os.path.exists('contatos.txt'):
        print('Lista de contatos está vazia')
        return
    with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
        contatos = arquivo.read()
    print('Lista de Contatos')
    print(contatos)

def deletar_contato():
    if not os.path.exists('contatos.txt'):
        print('Lista de contatos está vazia')
        return 
    with open('contatos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('')
    print('Contatos excluídos com sucesso')
