# Define uma função chamada 'soma' que recebe dois parâmetros (x e y) e retorna a soma deles
def soma(x,y):
    return x+y
s = soma(5,5)
print(s)
# Define uma função chamada 'subtracao' que recebe dois parâmetros (x e y) e retorna a subtração deles
def subtracao(x,y):
    return x-y


# Define uma função chamada 'op_aritmetica' que recebe uma função (fn) e dois operadores (operador1 e operador2)
# e retorna o resultado da função (fn) aplicada aos dois operadores
def op_aritmetica(fn, operador1, operador2):
    return fn(operador1, operador2)

result = op_aritmetica(soma,10,7)
print(result)
result = op_aritmetica(subtracao,10,7)
print(result)


# Define uma função chamada 'soma_p' que recebe um parâmetro (a) e retorna outra função
def soma_p(a):
    # A função interna chamada 'concluir' recebe um parâmetro (b) e retorna a soma de 'a' e 'b'
    def concluir(b):
        return a + b
    return concluir

result = soma_p(10)(5)
print(result)