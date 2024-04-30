class Usuario:
    contador = 0

class Pessoa:
    def __init__(self, nome, email, password, apelido):
        Usuario.contador += 1
        self.id = Usuario.contador
        self.nome = nome
        self.email = email
        self.__senha = password
        self.username = apelido

class Cliente(Pessoa):
    def __init__(self, nome, email, password, apelido, rg, cpf, telefone, dt_nascimento, endereco):
        super().__init__(nome, email, password, apelido)
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, nome, email, password, apelido, setor):
        super().__init__(nome, email, password, apelido)
        self.setor = setor

class Produto:
    def __init__(self, descricao, tipo, marca, modelo, dimensoes, peso, qualidade, validade, categoria, preco, desconto, codigo_barras, id_fornecedor, quantidade):
        Usuario.contador += 1
        self.id = Usuario.contador
        self.descricao = descricao
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.dimensoes = dimensoes
        self.peso = peso
        self.qualidade = qualidade
        self.validade = validade
        self.categoria = categoria
        self.preco = preco
        self.desconto = desconto
        self.codigo_barras = codigo_barras
        self.id_fornecedor = id_fornecedor
        self.quantidade = quantidade

class Compra:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos
        self.total = sum([produto.preco for produto in produtos])

class Pagamento:
    def __init__(self, compra, metodo_pagamento):
        self.compra = compra
        self.metodo_pagamento = metodo_pagamento
        self.status = 'Pendente'

    def realizar_pagamento(self):
        self.status = 'Pago'
        print(f"Pagamento realizado com {self.metodo_pagamento}.")

class Entrega:
    def __init__(self, compra, endereco):
        self.compra = compra
        self.endereco = endereco
        self.status = 'Pendente'

    def realizar_entrega(self):
        self.status = 'Entregue'
        print(f"Entrega realizada no endereço {self.endereco}.")

# Produtos
produto1 = Produto("Teclado", "Periférico", "Logitech", "Modelo XYZ", "20x10x5 cm", 0.5, "Alta", "01/01/2025", "Informática", 150.00, 0.10, "1234567890123", 1, 100)
produto2 = Produto("Caixinha de som", "Eletrônico", "Sony", "Modelo ABC", "15x15x10 cm", 0.3, "Média", "01/01/2023", "Áudio", 98.00, 0.05, "9876543210987", 2, 50)
produto3 = Produto("Perfume", "Cosmético", "Chanel", "Modelo DEF", "10x10x5 cm", 0.2, "Alta", "01/01/2024", "Fragrância", 500.00, 0.15, "1357924680246", 3, 20)

# Cliente
cliente1 = Cliente("Joana Silvana", "joanasilvana@gmail.com", "senha123", "joana123", "1234567", "987654321", "123456789", "01/01/1990", "Rua dos avacanoeiros, nº 896")

# Compra
compra1 = Compra(cliente1, [produto1, produto2, produto3])

# Pagamento
pagamento1 = Pagamento(compra1, "Cartão de Crédito")
pagamento1.realizar_pagamento()

# Entrega
entrega1 = Entrega(compra1, "Rua dos avacanoeiros, nº 896")
entrega1.realizar_entrega()
