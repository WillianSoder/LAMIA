from functools import reduce # Importa a função 'reduce' do módulo 'functools'

# Lista de dicionários, onde cada dicionário representa um aluno com seu nome e nota
alunos = [
    {'nome': 'maria', 'nota': 8},
    {'nome': 'joao', 'nota': 7.5},
    {'nome': 'cleiton', 'nota': 5},
    {'nome': 'julia', 'nota': 10},
    {'nome': 'gabriela', 'nota': 6.1},
]


# Cria uma lista de alunos aprovados (nota maior ou igual a 7) usando list comprehension
alunos_aprovados = [aluno for aluno in alunos if aluno['nota']>=7]
print(alunos_aprovados)

# Cria uma lista com as notas dos alunos aprovados
nota_a = [aluno['nota'] for aluno in alunos_aprovados]
print(nota_a)

# Define uma função lambda para somar dois valores (para ser usado na soma de notas)
somar = lambda a,b: a+b

# Usa a função 'reduce' para somar todas as notas dos alunos aprovados
total = reduce(somar,nota_a,0)

# Calcula a média das notas dos alunos aprovados (total dividido pela qnt de alunos aprovados)
print(total / len(alunos_aprovados))