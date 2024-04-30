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

    def get_senha(self):
        """Crie uma nova senha ."""
        return self.__senha
#O método get_senha na classe Pessoa retorna a senha do usuário


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

        class Administrador(Funcionario):
            def __init__(self, nome, email, password, apelido, setor):
                super().__init__(nome, email, password)
                self.username = apelido
                self.setor = setor

        print("Nome do administrador:", admin.nome)
        print("Email do administrador:", admin.email)
        print("Username do administrador:", admin.username)
        print("Setor do administrador:", admin.setor)

#class Administrador(Funcionario):
   # class Administrador:
      #  def __init__(self, nome, email, password, apelido, setor):
        #    self.nome = nome
         #   self.email = email
         #   self.__senha = password
          #  self.username = apelido
           # self.setor = setor


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

def tela_login(lista_usuarios):
    usuario_informado = input("Digite seu nome de usuário: ")
    senha_informada = input("Digite sua senha: ")

    print(lista_usuarios[0].username, usuario_informado, lista_usuarios[0].get_senha(), senha_informada)

    for usu in lista_usuarios:
        if usu.username == usuario_informado and usu.get_senha() == senha_informada:
            sessao = usu
            if isinstance(sessao, Funcionario):
                print("Login bem-sucedido como funcionário.")
            elif isinstance(sessao, Cliente):
                print("Login bem-sucedido como cliente.")
            break
    else:
        print("Nome de usuário ou senha incorretos.")



# Produtos
produto1 = Produto("Teclado", "Periférico", "Logitech", "Modelo XYZ", "20x10x5 cm", 0.5, "Alta", "01/01/2025",
                           "Informática", 150.00, 0.10, "1234567890123", 1, 100)
produto2 = Produto("Caixinha de som", "Eletrônico", "Sony", "Modelo ANC", "15x15x10 cm", 0.3, "Média",
                           "01/01/2023", "Áudio", 98.00, 0.05, "9876543210987", 2, 50)
produto3 = Produto("Perfume", "Cosmético", "Chanel", "Modelo PARIS", "10x10x5 cm", 0.2, "Alta", "01/01/2024",
                           "Fragrância", 500.00, 0.15, "1357924680246", 3, 20)

# Cliente
cliente1 = Cliente("Joana Silvana", "joanasilvana@gmail.com", "senha666", "joaninha", "1234567", "987654321", "123456789", "01/01/1990", "Rua dos avacanoeiros, nº 896")

admin = admin("Jorge", "jorgeoaulo@email.com", "senha7899", "jorgezinho", "RH")

# Lista_usu
lista_usuarios = [cliente1]

#chamar função de login
tela_login(lista_usuarios)


#EXPLIXANDO A TELA DE LOGIN DE UMA MANEIRA MAIS FACIL

#Funcionalidade: Essa função é responsável por permitir que os usuários entrem no sistema, autenticando-se com um nome de usuário e senha.
#Entrada: Quando um usuário deseja fazer login, ele precisa fornecer seu nome de usuário e senha.
#Verificação: O sistema verifica se as credenciais fornecidas estão corretas. Ele faz isso comparando-as com uma lista de usuários existentes no sistema.
#Resultado:
#Se as credenciais estiverem corretas:
#O usuário é logado no sistema.
#Dependendo do tipo de usuário (funcionário ou cliente), ele terá diferentes níveis de acesso e funcionalidades disponíveis.
#Se as credenciais estiverem incorretas:
#O sistema não permite o login e exibe uma mensagem de erro, indicando que as credenciais estão incorretas. Isso geralmente
# acontece quando o nome de usuário ou a senha fornecidos não correspondem aos registrados no sistema.