# Define a classe 'carro'
class carro:
    # Método construtor da classe, inicializa o atributo privado '__velocidade'
    def __init__(self):
        self.__velocidade = 0
    
    # Usado para acessar o valor de '__velocidade'
    @property  
    def velocidade(self):
        return self.__velocidade
    
    # Método para aumentar a velocidade em 5 unidades
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    # Método para diminuir a velocidade em 5 unidades
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
  
# Define a classe 'celta' que herda da classe 'carro'      
class celta(carro):
    pass # A classe 'celta' herda todos os métodos e atributos da classe 'carro' sem modificações

# Define a classe 'porsche' que herda da classe 'carro'
class porsche(carro):
    # Sobrescreve o método 'acelerar' da classe base
    def acelerar(self):
        super().acelerar() # Chama o método 'acelerar' da classe base uma vez
        return super().acelerar()  # Chama o método 'acelerar' da classe base novamente e retorna o resultado
    
 
# Cria uma instância da classe 'porsche'  
c1 = porsche()



# Chama o método 'acelerar' três vezes e imprime a velocidade (velocidade vai ser 10 em 10 por conta da classe 'porsche' ter duas aceleracoes por vez)
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())

# Chama o método 'frear' três vezes e imprime a velocidade
print(c1.frear())
print(c1.frear())
print(c1.frear())