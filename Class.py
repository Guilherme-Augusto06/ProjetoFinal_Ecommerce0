class Administrador:
    def __init__(self):
        self.admin = {}
        self.cadastrar_admin(1, "Carlos", 123, 123, 123)

    def cadastrar_admin(self, id_adm, nome_adm, senha_admin, cpf_adm, tel_adm):
        self.admin[id_adm] = [nome_adm, senha_admin, cpf_adm, tel_adm]

    def login_admin(self, id_adm, senha_admin):
        if id_adm in self.admin and self.admin[id_adm][1] == senha_admin:
            return True
        return False

    def listar_administradores(self):
        print("Lista de administradores:")
        for chave, valor in self.admin.items():
            print(f'ID: {chave} - NOME: {valor[0]} - CPF: {valor[1]} - TELEFONE: {valor[2]}')
        

# Definindo a classe E_commerce que representa uma loja.
class E_commerce:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome  # Atributo do nome da loja
        self.endereco = endereco # Atributo do endereço da loja
        self.cnpj = cnpj # Atributo do cnpj da loja
        self.cliente = {}  # Lista para armazenar clientes
        self.cadastrarCliente(1, "Thiago", 123, 123, 123)
        
    def login_cliente(self, id, senha):
        if id in self.cliente and self.cliente[id][1] == senha:
            return True
        return False

    def cadastrarCliente(self, id, nome, senha, cpf, tel, carrinho_cli = {}):
        # !Dicionário para armazenar informações dos clientes (Agregação)
        self.cliente[id] = [nome, senha, cpf, tel, carrinho_cli]
        

    def listarClientes(self):
        for chave, valor in self.cliente.items():
            #!Imprime informações dos clientes (Agregação)
             print(f'ID: {chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}')

    def listar_compras_clietne(self):
        cont = 1
        for chave, valor in self.cliente.items():
            for chave2, valor2 in valor[4].items():
                print(f'ID: {chave} - Nome: {valor[0]} - Compras do cliente: Produto:{valor2[0]} Valor: {valor2[1]}')
            
            cont += 1   
            #!Imprime informações dos clientes (Agregação)


# Classe Produtos
class Produtos:
    def __init__(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.quantidade = quantidade  # Atributo da quantidade de produtos disponíveis
        self.produtos = {}  # ?Atributo para armazenar produtos (Composição)
        self.carrinho = {}  # ?Atributo para armazenar produtos no carrinho (Composição)
        self.cadastrarProduto(1, "Playstation 5", 5000, 10)
        self.cadastrarProduto(2, "Xbox Series X", 4500, 10)
        self.cadastrarProduto(3, "Controle Playstation 5", 500, 10)
        self.cadastrarProduto(4, "Controle Xbox Series X", 450, 10)
        self.cadastrarProduto(5, "Guitarra", 1500, 10)
        self.cadastrarProduto(6, "Violão", 1000, 10)
        self.cadastrarProduto(7, "IPhone 14", 10000, 10)

    def listarprodutos(self):
        for chave, valor in self.produtos.items():
            print(f'ID: {chave} - NOME: {valor[0]} - VALOR: {valor[1]}')

    def getId_produto(self):
        return self.Id_produto

    def getNome_produto(self):
        return self.nome_produto

    def getValor_produto(self):
        return self.valor_produto

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def cadastrarProduto(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto  # Atributo de identificação do produto
        self.nome_produto = nome_produto  # Atributo do nome do produto
        self.valor_produto = valor_produto  # Atributo do valor do produto
        self.quantidade = quantidade  # Atributo da quantidade de produtos disponíveis

        # !Dicionário para armazenar informações dos produtos (Agregação)
        self.produtos[self.Id_produto] = [self.nome_produto, self.valor_produto, self.quantidade]

    def adicionar_carrinho(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.quantidade = quantidade
        self.carrinho[self.Id_produto] = [self.nome_produto, self.valor_produto, self.quantidade]


    def listarCarrinho(self):
        print('Carrinho:')
        for chave, valor in self.carrinho.items():
            print(f'ID: {chave} - NOME: {valor[0]} - VALOR: {valor[1]} - QUANTIDADE: {valor[2]}')
