from functools import reduce
notas = [6.0, 7.5, 5.7, 8]


# Itera sobre a lista de notas com índice usando 'enumerate'
for i, nota in enumerate(notas):
    print(i,nota) # Imprime o índice e a nota original
    notas[i] = nota + 1.5

print(notas)
print('\n\n')

# Itera sobre a lista de notas usando 'range' e o comprimento da lista
for i in range(len(notas)):
    notas[i] =  notas[i] + 1.5


# Define uma função 'somar_nota' que retorna outra função
def somar_nota(x):
    def calculo(nota):
        return nota+x # Adiciona 'x' à nota
    return calculo

# Define uma função 'ponto_extra' que adiciona 1.5 à nota
def ponto_extra(nota):
    return nota + 1.5

# redefinindo as notas
notas = [6.0, 7.5, 5.7, 8]
notas_atualizada = list(map(somar_nota(1.7), notas)) # Atualiza as notas usando 'map' e a função retornada por 'somar_nota(1.7)'
print(notas_atualizada)

print('\n\n')

notas = [6.0, 7.5, 5.7, 8]


# Define uma função 'somar' que soma dois valores
def somar(x, y):
    return x + y

# Usa a função 'reduce' para somar todas as notas da lista 'notas'
total = reduce(somar,notas,0)
print(total)
