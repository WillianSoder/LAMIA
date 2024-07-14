# Define uma função que imprime uma mensagem
def teste():
    print('funcao teste')

# Chamada da função
teste()

# Define uma função chamada 'aluno' que recebe dois parâmetros: 'nome' e 'idade'
# Os parâmetros têm valores padrão 'aluno' e 999, respectivamente
def aluno(nome = 'aluno', idade = 999):
    print(f'ALUNO: {nome} IDADE = {idade}')

# Chama a função 'aluno' sem argumentos, usando os valores padrão
aluno()
# Chama a função 'aluno' com um argumento, o nome 'joao'
aluno('joao')
# Chama a função 'aluno' com dois argumentos, o nome 'willian' e a idade 21
aluno('willian', 21)
# Chama a função 'aluno' especificando apenas a idade, usando o valor padrão para o nome
aluno(idade=87)



# Imprime o nome do módulo onde o código está sendo executado
# Se o código estiver sendo executado diretamente como é o caso, '__name__' será '__main__'
print(__name__)


# Define uma função chamada 'soma_e_multplicacao' que recebe três parâmetros: 'x', 'y' e 'z'
# Retorna a soma de 'x' com o produto de 'y' e 'z'
def soma_e_multplicacao(x,y,z):
    return x + y * z

result = soma_e_multplicacao(2,3,10)
print(result)