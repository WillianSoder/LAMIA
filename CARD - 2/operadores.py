print('\n\nunarios:')
# Op. unarios
y = 5 
print(not False)
print(not True)
print(--7)
print(-y)
print(+3)


print('\n\naritmeticos:')
# Op. aritmeticos
i = 1
j = 3

print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i % j)


print('\n\nrelacionais:')
# Op. Relacionais

a = 1
b = 9

print(a > b) 
print(a >= b) 
print(a < b)
print(a <= b)
print(a == b)
print(a != b)



print('\n\natribuicao:')
# Op. de atribuição 

result = 5
print(result)
result += 5 # soma 5 a result (susbtitui result++)
print(result)
result -= 5
print(result)
result *= 5
print(result)
result /= 5
print(result)
result %= 5
print(result)
result = 'agora recebeu texto'
print(result)


print('\n\nlogicos:')
# Op. logicos
a1 = True
a2 = False
a3 = True
print(a1 and a2 and a3)
print(a1 or a2 or a3)
print(a1 != a3)# xor | ^
print(not a3)
print(not a2 and a1)


print('\n\nternario:')
# Op. ternario

trabalhando = False
estudando = False
salario = 1000 if trabalhando or estudando else 0
print(salario)
