# Solicita ao usuário que informe a nota e converte o valor para float
nota = float(input('informe a nota: '))
# PEga a entrada do usuario e convete para valor booleano
comportamento = True if input('Comportado (s/n)') == 's' else False

# Verifica a nota e o comportamento para determinar o resultado
if nota >= 9.5 and comportamento:
    print('OTIMA NOTA')
    print("Muito Bem!!!")
elif nota >= 6:
    print('Aprovado')
elif nota >= 4:
    print('recuperaçao')
else:
    print('reprovado')
print(nota)


print('\n\nEX2:')

# Variáveis para testar valores que são considerados verdadeiros ou falsos
x = 'valor' #sim
x = 0 #nao
x = -0.00001 #sim
x = '' #nao
x = ' ' #sim
x = [] #nao
x = {} #nao
if x:
    print('sim')
else:
    print('nao')



print('\n\nLaco for:')
#Testes de laco for do python

# Loop de 0 a 19
for i in range(20):
    print(i)

# Loop de 1 a 20
for i in range(1,21):
    print(i)
    
# Loop de 1 a 19 com passo de 10
for i in range(1,20,10):
    print(i)

# Loop de 20 a -19 com passo de -10
for i in range(20,-20,-10):
    print(i)

# Loop sobre uma lista de 1 a 10
lista = [1,2,3,4,5,6,7,8,9,10]
for x in lista:
    print(x,end=' ')
print('\n')
for x in lista:
    print(x)


# Dicionário representando um produto  
produto = {
    'nome': 'abacaxi',
    'valor': 10,
    'promocao': 5
}

# Itera sobre as chaves do dicionário definido acima 
for x in produto:
    print(x, "-->", produto[x])

for x, y in produto.items():
    print(x, "-->", y)

for y in produto.values():
    print(y,end=' ')

for x in produto.keys():
    print(x,end=' ')



print('\n\nLaco While:')
#Testes de laco while do python

soma = 0
controle = 0
qtd = 0

# Loop enquanto o controle for diferente de -1
while controle != -1:
    controle = float(input('Digite -1 para sair'))
    if controle != -1:
        soma += controle  # Adiciona o valor de controle à soma
        qtd += 1 # Incrementa a quantidade de entradas

# Calcula e imprime a média dos valores inseridos
print(f'Media = {soma/qtd}')