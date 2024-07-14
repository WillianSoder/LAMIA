# Exemplo utilizando o que foi aprendido em aula para realizar uma analise estatitica simples
from functools import reduce

numeros = [15, 78, 47, 98, 52, 23, 32, 84, 9, 82, 57, 1]

# Função lambda para definir se um número é par
numeros_pares = lambda x: x % 2 == 0

# Filtrando números pares usando a função lambda e armazenando em uma nova lista
pares = list(filter(numeros_pares, numeros))

print("Números pares:", pares)

# Definindo uma classe para análise estatística
class Estatisticas:
    @classmethod
    def calcular_media(cls, lista):
        return reduce(lambda x, y: x + y, lista) / len(lista)
    
    @classmethod
    def calcular_soma(cls, lista):
        return reduce(lambda x, y: x + y, lista)
    
    @staticmethod
    def encontrar_maior_valor(lista):
        return max(lista) # Usada para encontrar o maior elemento da lista
    
    @staticmethod
    def encontrar_menor_valor(lista):
        return min(lista) # Usada para encontrar o menor elemento da lista

# Calculando estatísticas sobre a lista de números usando a classe Estatisticas
media = Estatisticas.calcular_media(numeros)
soma = Estatisticas.calcular_soma(numeros)
maior = Estatisticas.encontrar_maior_valor(numeros)
menor = Estatisticas.encontrar_menor_valor(numeros)

# Imprimindo as estatísticas calculadas
print("\nEstatísticas:")
print("Média:", media)
print("Soma:", soma)
print("Maior valor:", maior)
print("Menor valor:", menor)
