from Class import *
import os

def mani():
    admin = Administrador()
    Loja = E_commerce("Augusto's E_commerce", "Rua 1", "123456789")
    produtos = Produtos(30, "Produtos", "R$ 0,00", 30)
    playstation5 = Playstation5(1, "Playstation 5", 5000, 30)
    xbox_series_x = Xbox_Series_X(2, "Xbox Series X", 4500, 30)
    controle_ps5 = Controle_Playstation5(3, "Controle Playstation 5", 500, 30)
    controle_xbox = Controle_Xbox(4, "Controle Xbox", 400, 30)
    guitarra = Guitarra(5, "Guitarra", 1000, 30)
    violao = Violão(6, "Violão", 800, 30)
    iphone = IPhone14(7, "IPhone 14", 10000, 30)
    
    countID = 1
    countID_adm = 1

    sair = False   
    while sair == False:
        try:
            os.system('cls')
            print("---MENU---")
            print("Augusto's E-commerce")
            print("1- Cadastrar cliente")
            print("2- Cadastrar produto")
            print("3- Listar produtos")
            print("4- Listar clientes")
            print("5- Cadastrar administrador")
            print("6- Listar administradores")
            print("7- Sair")
            print("----------")
            op = int(input(">> "))
            try:
                match op:
                    case 1:
                        # Cadastrar Cliente
                        os.system('cls')
                        print('Cadastro de clientes')
                        print('Informe os dados do cliente')
                        countID += 1
                        id = countID
                        nome = input("Nome -")
                        cpf = int(input("CPF -"))
                        tel = int(input("Telefone -"))

                        Loja.cadastrarCliente(id, nome, cpf, tel)
                        print('Cliente cadastrado com sucesso')
                        os.system('pause')

                    case 2:
                        # Cadastrar Produto
                        os.system('cls')
                        print('Cadastro de produtos')
                        print('Informe os dados do produto')
                        id_produto = int(input("ID -"))
                        nome_produto = input("Nome -")
                        valor_produto = float(input("Valor -"))
                        quantidade = int(input("Quantidade -"))

                        produtos.cadastrarProduto(id_produto, nome_produto, valor_produto, quantidade)
                        print('Produto cadastrado com sucesso')
                        os.system('pause')

                    case 3:
                        # Listar Produtos
                        os.system('cls')
                        print('Lista de produtos')
                        print(f'ID: {playstation5.getId_produto()} - Nome: {playstation5.getNome_produto()} - Valor: {playstation5.getValor_produto()} - Quantidade: {playstation5.getQuantidade()}')
                        print(f'ID: {xbox_series_x.getId_produto()} - Nome: {xbox_series_x.getNome_produto()} - Valor: {xbox_series_x.getValor_produto()} - Quantidade: {xbox_series_x.getQuantidade()}')
                        print(f'ID: {controle_ps5.getId_produto()} - Nome: {controle_ps5.getNome_produto()} - Valor: {controle_ps5.getValor_produto()} - Quantidade: {controle_ps5.getQuantidade()}')
                        print(f'ID: {controle_xbox.getId_produto()} - Nome: {controle_xbox.getNome_produto()} - Valor: {controle_xbox.getValor_produto()} - Quantidade: {controle_xbox.getQuantidade()}')
                        print(f'ID: {guitarra.getId_produto()} - Nome: {guitarra.getNome_produto()} - Valor: {guitarra.getValor_produto()} - Quantidade: {guitarra.getQuantidade()}')
                        print(f'ID: {violao.getId_produto()} - Nome: {violao.getNome_produto()} - Valor: {violao.getValor_produto()} - Quantidade: {violao.getQuantidade()}')
                        print(f'ID: {iphone.getId_produto()} - Nome: {iphone.getNome_produto()} - Valor: {iphone.getValor_produto()} - Quantidade: {iphone.getQuantidade()}')
                        produtos.listarprodutos()
                        os.system('pause')


                    case 4:
                        # Listar Clientes
                        os.system('cls')
                        print('Lista de clientes')
                        Loja.listarClientes()
                        os.system('pause')

                    case 5:
                        os.system('cls')
                        print('Cadastro de clientes')
                        print('Informe os dados do administrador')
                        countID_adm += 1
                        id_adm = countID_adm
                        nome_adm = input('Insira o nome do administrador >> ')
                        senha_admin = int(input('Insira a senha >> '))
                        cpf_adm = int(input('Insira o cpf do administrador >> '))
                        tel_adm = int(input('Insira o telefone do administrador >> '))

                        Loja.cadastrar_admin(id_adm, nome_adm, senha_admin, cpf_adm, tel_adm)
                        print('Cadastrador de administrador realizado com sucesso!')
                        os.system('pause')

                    case 6:
                        os.system('cls')
                        print('Lista de administradores')
                        admin.listar_administradores()
                        os.system('pause')
                        

                    case 7:
                        print("Saindo...")
                        menu_inicial()

                    case _:
                        print("Opção Invalida")
            except ValueError as erro:
                print("Valor Invalido")
                print(f"erro: {erro.__class__.__name__}")

        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")


def menu_cli():
    Loja = E_commerce("Augusto's E_commerce", "Rua 1", "123456789")
    sair = False
    produtos = Produtos(30, "Produtos",  00, 30)
    playstation5 = Playstation5(1, "Playstation 5", 5000, 30)
    xbox_series_x = Xbox_Series_X(2, "Xbox Series X", 4500, 30)
    controle_ps5 = Controle_Playstation5(3, "Controle Playstation 5", 500, 30)
    controle_xbox = Controle_Xbox(4, "Controle Xbox", 400, 30)
    guitarra = Guitarra(5, "Guitarra", 1000, 30)
    violao = Violão(6, "Violão", 800, 30)
    iphone = IPhone14(7, "IPhone 14", 10000, 30)
    while sair == False:
        try:
            os.system('cls')
            print("---MENU---")
            print("Augusto's E-commerce")
            print('1- Listar produtos')
            print('2- Adicionar produto ao carrinho')
            print('3- Listar carrinho')
            print('4- Finalizar compra')
            print('5- Sair')
            print("----------")
            op = int(input(">> "))
            match op:
                case 1:
                    # Listar Produtos
                    os.system('cls')
                    print('Lista de produtos')
                    print(f'ID: {playstation5.getId_produto()} - Nome: {playstation5.getNome_produto()} - Valor: {playstation5.getValor_produto()} - Quantidade: {playstation5.getQuantidade()}')
                    print(f'ID: {xbox_series_x.getId_produto()} - Nome: {xbox_series_x.getNome_produto()} - Valor: {xbox_series_x.getValor_produto()} - Quantidade: {xbox_series_x.getQuantidade()}')
                    print(f'ID: {controle_ps5.getId_produto()} - Nome: {controle_ps5.getNome_produto()} - Valor: {controle_ps5.getValor_produto()} - Quantidade: {controle_ps5.getQuantidade()}')
                    print(f'ID: {controle_xbox.getId_produto()} - Nome: {controle_xbox.getNome_produto()} - Valor: {controle_xbox.getValor_produto()} - Quantidade: {controle_xbox.getQuantidade()}')
                    print(
                        f'ID: {guitarra.getId_produto()} - Nome: {guitarra.getNome_produto()} - Valor: {guitarra.getValor_produto()} - Quantidade: {guitarra.getQuantidade()}')
                    print(
                        f'ID: {violao.getId_produto()} - Nome: {violao.getNome_produto()} - Valor: {violao.getValor_produto()} - Quantidade: {violao.getQuantidade()}')
                    print(
                        f'ID: {iphone.getId_produto()} - Nome: {iphone.getNome_produto()} - Valor: {iphone.getValor_produto()} - Quantidade: {iphone.getQuantidade()}')
                    os.system('pause')

                case 2:
                    os.system('cls')
                    # Adicionar produto ao carrinho
                    print(
                        f'Quantidade de Playstation 5: {playstation5.getQuantidade()}')
                    print(
                        f'Quantidade de Xbox Series X: {xbox_series_x.getQuantidade()}')
                    print(
                        f'Quantidade de Controle Playstation 5: {controle_ps5.getQuantidade()}')
                    print(
                        f'Quantidade de Controle Xbox: {controle_xbox.getQuantidade()}')
                    print(
                        f'Quantidade de Guitarra: {guitarra.getQuantidade()}')
                    print(f'Quantidade de Violão: {violao.getQuantidade()}')
                    print(f'Quantidade de IPhone 14: {iphone.getQuantidade()}')
                    print("=-=-=-=-=-")
                    print('Qual produto você deseja adicionar ao carrinho?')
                    print('1- Playstation 5')
                    print('2- Xbox Series X')
                    print('3- Controle Playstation 5')
                    print('4- Controle Xbox')
                    print('5- Guitarra')
                    print('6- Violão')
                    print('7- IPhone 14')
                    print("=-=-=-=-=-")

                    op = int(input(">> "))

                    if op == 1:
                        playstation5.setQuantidade(playstation5.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(playstation5.getId_produto(), playstation5.getNome_produto(), playstation5.getValor_produto(), 1)
                    
                    elif op == 2:
                        xbox_series_x.setQuantidade(xbox_series_x.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(xbox_series_x.getId_produto(), xbox_series_x.getNome_produto(), xbox_series_x.getValor_produto(), 1)
                        
                    elif op == 3:
                        controle_ps5.setQuantidade(controle_ps5.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(controle_ps5.getId_produto(), controle_ps5.getNome_produto(),controle_ps5.getValor_produto(), 1)
                        
                    elif op == 4:
                        guitarra.setQuantidade(guitarra.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(guitarra.getId_produto(), guitarra.getNome_produto(),guitarra.getValor_produto(), 1)
                        
                    elif op == 5:
                        violao.setQuantidade(violao.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(violao.getId_produto(), violao.getNome_produto(),violao.getValor_produto(), 1)
                        
                    elif op == 6:
                        iphone.setQuantidade(iphone.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(iphone.getId_produto(), iphone.getNome_produto(),iphone.getValor_produto(), 1)
                        
                    elif op == 7:
                        iphone.setQuantidade(iphone.getQuantidade() - 1)
                        print('Produto adicionado ao carrinho com sucesso!')
                        produtos.adicionar_carrinho(iphone.getId_produto(), iphone.getNome_produto(),iphone.getValor_produto(), 1)

                case 3:
                    # Listar Carrinho
                    os.system('cls')
                    print('Lista de produtos')
                    produtos.listarCarrinho()
                    os.system('pause')

                case 4:
                    # Finalizar Compra
                    # somar os valores dos produtos
                    os.system('cls')
                    print('Somar valores dos produtos')
                    produtos.getValor_produto()
                    os.system('pause')

                case 5:
                    print("Saindo...")
                    menu_inicial()

        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")


def menu_inicial():
    Loja = E_commerce("Augusto's E_commerce", "Rua 1", "123456789")
    admin = Administrador()
    sair = False
    while sair == False:
        try:
            print("---MENU---")
            print("Augusto's E-commerce")
            print('1- logar como administrador')
            print('2- logar como cliente')
            print('3- Sair')
            print("----------")
            op = int(input(">> "))
            try:
                match op:
                    case 1:
                        os.system('cls')
                        id_adm = int(input('Insira o ID do administrador'))
                        senha_admin = int(input('Insira a senha >> '))
                        if admin.login_admin(id_adm, senha_admin):
                            print("Login bem-sucedido!")
                            os.system("pause")
                            os.system('cls')
                            mani()
                        else:
                            print("Login falhou. Verifique o ID e a senha.")
                            os.system("pause")
                            os.system('cls')
                         
                    case 2:
                        os.system('cls')
                        id = int(input('Insira o ID de cliente >> '))
                        senha = int(input('Insira a senha >> '))
                        if Loja.login_cliente(id, senha):
                            print("Login bem-sucedido!")
                            os.system("pause")
                            os.system('cls')
                            menu_cli()
                        else:
                            print("Login falhou. Verifique o ID e a senha.")
                            os.system("pause")
                            os.system('cls')
                        
                    case 3:
                        print("Saindo...")
                        menu_inicial()

            except ValueError as erro:
                print("Valor Invalido")
                print(f"erro: {erro.__class__.__name__}")

        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
