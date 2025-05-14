import random

lista_iput = input("digite os numeros para o sorteio(10 tem mais chance): ")

lista_iput = lista_iput.replace("," , " ")
lista_iput = lista_iput.split()
lista_vazia = []


for indice , valor in enumerate(lista_iput):
    # print(f"O termo na posição {indice} é '{valor}'")
    lista_vazia.append(valor)

lista_int = []

for i in lista_vazia:
    i = int(i)
    lista_int.append(i)

# print(lista_int)

peso = [5 if i == 10 else 1 for i in lista_int]

# print(peso)

vsf = random.choices( lista_int ,weights=peso  ,k=1)
print(f" o vsf é: {vsf[0]}")


