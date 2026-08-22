class Pessoas:
    def __init__(self,nome,cpf,email,telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email 
        self.telefone = telefone 

# metodos de acesso

# get
@property
def nome(self):
    return self.__nome
def cpf(self):
    return self.__cpf
def email(self):
    return self.__email
def telefone(self):
    return self.__telefone

#set; definir o valor do atributo
@nome.setter
def nome(self, nome):
    self.__nome = nome
@cpf.setter
def nome(self, cpf):
    self.__cpf = cpf
@email.setter
def email(self, email):
    self.__email = email
@telefone.setter
def telefone(self, telefone):
    self.__telefone = telefone