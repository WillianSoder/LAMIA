class Contador:
    contador = 0 # atributo de classe, compartilhado entre todas as instâncias da classe
    
    # Método de instância, retorna uma mensagem
    def msg(self):
        return 'Assim funciona'
    
    # Método de classe, incrementa o valor do atributo de classe 'contador'
    @classmethod
    def incremento(cls):
        cls.contador += 1
        return cls.contador
    
    # Método de classe, decrementa o valor do atributo de classe 'contador'
    @classmethod
    def decremento(cls):
        cls.contador -= 1
        return cls.contador
    
    # Método estático, retorna o valor do argumento 'n' incrementado em 1 unidade
    @staticmethod
    def mais_um(n):
        return n + 1



# Cria uma instância da classe 'Contador'        
x = Contador()
print(x.msg()) # Chama o método 'msg' da instância
print('\n')      

# Chama o método de classe 'incremento' diretamente pela classe e imprime o valor atualizado de 'contador'
print(Contador.incremento())
print(Contador.incremento())
print(Contador.incremento())
print(Contador.incremento())
print(Contador.incremento())
print('\n')

# Chama o método de classe 'decremento' diretamente pela classe e imprime o valor atualizado de 'contador'
print(Contador.decremento())
print(Contador.decremento())
print(Contador.decremento())
print('\n')

# Chama o método estático 'mais_um' diretamente pela classe com o argumento 7 e imprime o resultado
print(Contador.mais_um(7))