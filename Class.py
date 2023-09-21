# Definindo a classe E_commerce que representa uma loja.
class E_commerce:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome  # Atributo do nome da loja
        self.cliente = {}  #?Atributo para armazenar clientes (Composição)

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id  # Atributo de identificação do cliente
        self.nome = nome  # Atributo do nome do cliente
        self.cpf = cpf  # Atributo do CPF do cliente
        self.tel = tel  # Atributo do telefone do cliente

        self.cliente[self.id] = [self.nome, self.cpf, self.tel]  #!Dicionário para armazenar informações dos clientes (Agregação)

    def listarClientes(self):
        for chave, valor in self.cliente.items():
            #!Imprime informações dos clientes (Agregação)
            print(f'ID: {chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}')

# Classe Produtos
class Produtos:
    def __init__(self, Id_produto, nome_produto, valor_produto, quantidade):
        self.Id_produto = Id_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.quantidade = quantidade  # Atributo da quantidade de produtos disponíveis
        self.produtos = {}  #?Atributo para armazenar produtos (Composição)
        self.carrinho = {}
        self.ps5 = Playstation5
        self.xbox_x = Xbox_Series_X
        self.ConPS5 = Controle_Playstation5
        self.ConX = Controle_Xbox
        self.gui =Guitarra
        self.vio = Violão
        self.IP4 = IPhone14

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

    def cadastrarProduto(self, Id_produto, nome_produto, valor_produto):
        self.Id_produto = Id_produto  # Atributo de identificação do produto
        self.nome_produto = nome_produto  # Atributo do nome do produto
        self.valor_produto = valor_produto  # Atributo do valor do produto

        self.produtos[self.Id_produto] = [self.nome_produto, self.valor_produto]  #!Dicionário para armazenar informações dos produtos (Agregação)

    def adicionar_carrinho(self, idCli, reserva):
        match reserva:
            case 1:
                produto = "Playstation 5"
            case 2:
                produto = "Xbox Series X"
            case 3:
                produto = "Controle Playstation 5"
            case 4:
                produto = "Controle Xbox"
            case 5:
                produto = "Guitarra"
            case 6:
                produto = "Violão"
            case 7:
                produto = "IPhone 14"
            case _:
                produto = "Produto não encontrado"

        if idCli not in self.carrinho:
            self.carrinho[idCli] = []  # Crie uma lista vazia para o cliente se ainda não existir

        self.carrinho[idCli].append(produto) # Adicione o produto à lista de compras do cliente         


    def listarcarrinho(self):
        for chave, valor in self.carrinho.items():
            print(f'ID: {chave} - Produto: {valor}')
        

class Playstation5(Produtos):
    pass

class Xbox_Series_X(Produtos):
    pass

class Controle_Playstation5(Produtos):
    pass

class Controle_Xbox(Produtos):
    pass

class Guitarra(Produtos):
    pass

class Violão(Produtos):
    pass

class IPhone14(Produtos):
    pass