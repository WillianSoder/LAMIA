# Define uma função chamada 'soma' que aceita um número variável de argumentos
def soma(*numeros):
    total = 0
    for i in numeros: # Percorre cada número fornecido como argumento
        total += i
    return total

resultado = soma(5,5,5,5,5)
print(resultado)

# Define uma função chamada 'Rfinal' que aceita um número variável de argumentos nomeados (kwargs)
def Rfinal (**kwargs):
    # Verifica se a nota é maior ou igual a 6 para determinar o status de aprovação ou reprovação e armazena em 'status'
    status = 'aprovado' if kwargs['nota'] >= 6 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'

resultado = Rfinal(nome = 'willian', nota = 9.5)
print(resultado)
