class produto:
    # Método construtor da classe, inicializa os atributos nome, __preco e desconto
    def __init__(self, nome, preco = 1.99, desconto = 0):
        self.nome = nome
        self.__preco = preco
        self.desconto = desconto
    
    # Usado para acessar o valor de __preco
    @property
    def preco(self):
        return self.__preco
    
    # Setter para o atributo __preco, usado para alterar o valor de __preco com validação
    @preco.setter
    def preco(self, preco_n):
        if preco_n > 0:
            self.__preco = preco_n
    
    # Calcula o preço atualizado com desconto aplicado
    @property
    def preco_atualizado(self):
        return (1 - self.desconto) * self.__preco



# Cria duas instâncias da classe produto   
p1 = produto('caneta', 2.95, 0.5)
p2 = produto('lapis', 0.99, 0.2)

# Tenta definir o preço das instâncias com valores negativos
# Estes valores vão ser ignorados porque a validação no setter não permite valores negativos
p1.preco = -7
p2.preco = -1


# Define o preço das instâncias com valores positivo
p1.preco = 10
p2.preco = 15


print(p1.nome,p1.preco, p1.desconto, p1.preco_atualizado)
print(p2.nome,p2.preco, p2.desconto, p2.preco_atualizado)