from Class import *
import os

admin = Administrador()
Loja = E_commerce("Augusto's E_commerce", "Rua 1", "123456789")
produtos = Produtos(30, "Produtos", "R$ 0,00", 30) 
countID = 1
countID_adm = 1
countID_produto = 7

def mani():

    try:
            os.system('cls')
            print("_______________MENU_______________")
            print("|Augusto's E-commerce            |")
            print("|1- Cadastrar cliente            |")
            print("|2- Cadastrar produto            |")
            print("|3- Listar produtos              |")
            print("|4- Listar clientes              |")
            print("|5- Cadastrar administrador      |")
            print("|6- Listar administradores       |")
            print("|7- Histórico de compras/cliente |")
            print("|8- Sair                         |")
            print("|________________________________|")
            op = int(input(">> "))
            try:
                match op:
                    case 1:
                        # Cadastrar Cliente
                        os.system('cls')
                        print('Cadastro de clientes')
                        print('Informe os dados do cliente')
                        global countID
                        countID += 1
                        id = countID
                        nome = input("Nome >> ")
                        senha = int(input('Insira a senha >> '))
                        cpf = int(input("CPF >> "))
                        tel = int(input("Telefone >> "))
                        Loja.cadastrarCliente(id, nome, senha, cpf, tel)
                        print('Cliente cadastrado com sucesso')
                        os.system('pause')
                        mani()

                    case 2:
                        # Cadastrar Produto
                        os.system('cls')
                        print('Cadastro de produtos')
                        print('Informe os dados do produto')
                        global countID_produto
                        countID_produto += 1
                        id_produto = countID_produto
                        nome_produto = input("Nome >> ")
                        valor_produto = float(input("Valor >> "))
                        quantidade = int(input("Quantidade >> "))

                        produtos.cadastrarProduto(id_produto, nome_produto, valor_produto, quantidade)
                        print('Produto cadastrado com sucesso')
                        os.system('pause')
                        mani()

                    case 3:
                        # Listar Produtos
                        os.system('cls')
                        print('Lista de produtos')
                        produtos.listarprodutos()
                        os.system('pause')
                        mani()


                    case 4:
                        # Listar Clientes
                        os.system('cls')
                        print('Lista de clientes')
                        Loja.listarClientes()
                        os.system('pause')
                        mani()

                    case 5:
                        os.system('cls')
                        print('Cadastro de clientes')
                        print('Informe os dados do administrador')
                        global countID_adm
                        countID_adm += 1
                        id_adm = countID_adm
                        nome_adm = input('Insira o nome do administrador >> ')
                        senha_admin = int(input('Insira a senha >> '))
                        cpf_adm = int(input('Insira o cpf do administrador >> '))
                        tel_adm = int(input('Insira o telefone do administrador >> '))

                        admin.cadastrar_admin(id_adm, nome_adm, senha_admin, cpf_adm, tel_adm)
                        print('Cadastrador de administrador realizado com sucesso!')
                        os.system('pause')
                        mani()

                    case 6:
                        os.system('cls')
                        print('Lista de administradores')
                        admin.listar_administradores()
                        os.system('pause')
                        mani()
                        

                    case 7:
                        #Histórico de compras
                        os.system('cls')
                        print('Histórico de compras')
                        Loja.listarClientes()
                        id = int(input('Insira o ID do cliente >> '))
                        print(f'Histórico de compras do cliente')
                        Loja.listar_compras_clietne(id_cliente=id, produto=produtos.carrinho, valor=produtos.carrinho)
                        os.system('pause')
                        mani()
                    
                    case 8:
                        print("Saindo...")
                        menu_inicial()
                    case _:
                        print("Opção Invalida")
                        mani()
            except ValueError as erro:
                print("Valor Invalido")
                print(f"erro: {erro.__class__.__name__}")
                mani()

    except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")


def menu_cli():
    try:
            os.system('cls')
            print("_________________MENU___________________")
            print("|Augusto's E-commerce                  |")
            print('|1- Listar produtos                    |')
            print('|2- Adicionar produto ao carrinho      |')
            print('|3- Listar carrinho                    |')
            print('|4- Finalizar compra                   |')
            print('|5- Sair                               | ')
            print("|______________________________________|")
            op = int(input(">> "))
            try:
                match op:
                    case 1:
                        # Listar Produtos
                        os.system('cls')
                        print('Lista de produtos')
                        produtos.listarprodutos()
                        os.system('pause')
                        menu_cli()

                    case 2:
                        os.system('cls')
                        # Adicionar produto ao carrinho
                        produtos.listarprodutos()
                        id_produto = int(input('Insira o ID do produto >> '))
                        nome_produto = produtos.produtos[id_produto][0]
                        valor_produto = produtos.produtos[id_produto][1]
                        quantidade = int(input('Insira a quantidade >> '))
                        
                        produtos.adicionar_carrinho(id_produto, nome_produto, valor_produto, quantidade)
                        print('Produto adicionado ao carrinho com sucesso!')
                        os.system('pause')
                        menu_cli()


                    case 3:
                        # Listar Carrinho com o cliente
                        os.system('cls')
                        print('Lista de produtos no carrinho')
                        produtos.listarCarrinho()
                        os.system('pause')
                        menu_cli()

                        

                                    
                    case 4:
                        #Finalziar compra adicionando produtos ao historico de compras de cada cliente
                        os.system('cls')
                        print('Finalizar compra')
                        Loja.listarClientes()
                        id = int(input('Insira o ID do cliente >> '))
                        Loja.cliente[id][4] = produtos.carrinho                                            
                        print('Compra finalizada com sucesso!')
                        os.system('pause')
                        menu_cli()


                    case 5:
                        print("Saindo...")
                        menu_inicial()
                        
            except ValueError as erro:
                print("Valor Invalido")
                print(f"erro: {erro.__class__.__name__}")
                menu_cli() 

    except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            menu_cli()



def menu_inicial():
    try:
            print("|______________MENU______________|")
            print("|Augusto's E-commerce            |")
            print('|1- logar como administrador     |')
            print('|2- logar como cliente           |')
            print('|3- Sair                         |')
            print("|________________________________|")
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
                            menu_inicial()
                         
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
                            menu_inicial()
                        
                    case 3:
                        print("Saindo...")
                        exit()

            except ValueError as erro:
                print("Valor Invalido")
                print(f"erro: {erro.__class__.__name__}")
                menu_inicial()

    except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")
            menu_inicial()
 
