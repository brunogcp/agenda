AGENDA = {}


def mostar_agenda():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('Agenda vazia')


def buscar_contato(contato):
    try:
        print()
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['tel'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Contato inexistente')
        print(erro)


def ler_detalhes():
    tel = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereço: ')
    return tel, email, endereco


def inserir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel': tel,
        'email': email,
        'endereco': endereco
    }
    exportar_agenda('database.csv')
    print('>>>>>>> Contato {} adicionado/editado com sucesso'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        exportar_agenda('database.csv')
        print('>>>>>>> Contato {} excluido com sucesso'.format(contato))
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Contato inexistente')
        print(erro)


def carregar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                inserir_editar_contato(nome, tel, email, endereco)
    except FileNotFoundError:
        print('>>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>>> Algum erro inesperado ocurreu')
        print(error)


def exportar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            #arquivo.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))
        print('>>>>>>> Agenda exportata com sucesso')
    except:
        print('>>>>>>> Algum erro ocorreu ao exportar contatos')


def salvar_agenda():
    exportar_agenda('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'tel': tel,
                    'email': email,
                    'endereco': endereco
                }
        print('>>>>>>> Database carregado com sucesso')
        print('>>>>>>> {} contatos carregado'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>>>> Algum erro inesperado ocurreu')
        print(error)


def menu():
    print()
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Inserir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos para CSV')
    print('0 - Fechar agenda')


carregar()

while True:
    menu()

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        mostar_agenda()
    elif opcao == 2:
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == 3:
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>>>> Contato já existente')
        except KeyError:
            tel, email, endereco = ler_detalhes()
            inserir_editar_contato(contato, tel, email, endereco)
    elif opcao == 4:
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>>>> Editando contato', contato)
            tel, email, endereco = ler_detalhes()
            inserir_editar_contato(contato, tel, email, endereco)
        except KeyError:
            print('>>>>>>> Contato inexistente')
    elif opcao == 5:
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == 6:
        nome_do_arquivo = input('Digite o nome o arquivo a ser exportado: ')
        exportar_agenda(nome_do_arquivo)
    elif opcao == 7:
        nome_do_arquivo = input('Digite o nome o arquivo a ser importado: ')
        carregar_agenda(nome_do_arquivo)
    elif opcao == 0:
        print('>>>>>>> Fechando programa')
        break
    else:
        print('>>>>>>> Opção inválida')
