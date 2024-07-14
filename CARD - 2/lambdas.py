from functools import reduce # Importa a função 'reduce' do módulo 'functools'

# Lista de dicionários, onde cada dicionário representa um aluno com seu nome e nota
alunos = [
    {'nome': 'maria', 'nota': 8},
    {'nome': 'joao', 'nota': 7.5},
    {'nome': 'cleiton', 'nota': 5},
    {'nome': 'julia', 'nota': 10},
    {'nome': 'gabriela', 'nota': 6.1},
]

# Define uma função lambda que retorna True se a nota do aluno for maior ou igual a 7
aprovado = lambda aluno: aluno['nota'] >= 7
#honra = lambda aluno: aluno['nota'] >= 9
obter_N = lambda aluno: aluno['nota']

# Filtra a lista de alunos para incluir apenas aqueles aprovados, usando a função 'aprovado' (coverte a saida para um list)
alunos_aprovados = list(filter(aprovado, alunos))
nota_a = list(map(obter_N, alunos_aprovados)) # Mapeia a lista de alunos aprovados para obter apenas as notas, usando a função 'obter_N'

print(nota_a)
#print(alunos_aprovados)
#print(alunos)


# Define uma função lambda que soma dois valores
somar = lambda a,b: a+b
total = reduce(somar,nota_a,0)# Usa a função 'reduce' para somar todas as notas da lista 'nota_a'
# Calcula e imprime a média das notas dos alunos aprovados
print(total / len(alunos_aprovados))
