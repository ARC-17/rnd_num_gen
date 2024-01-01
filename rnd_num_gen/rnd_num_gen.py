lista = []
i = 1
while i < 3:
    from random import randint
    lista.append(int(randint(1,60)))
    print(lista)
    i += 1
print()
print(f'Lista de números: {lista}')
