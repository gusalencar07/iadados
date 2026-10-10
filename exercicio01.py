#crie um script para solicitar as 4 notas de um aluno e inserir em uma lista ,exibir a maior nota ,a soma de todas as notas

#notas =[] 

n1 = float(input("digite a nota 1: "))
n2 = float(input("digite a nota 2: "))
n3 = float(input("digite a nota 3: "))
n4 = float(input("digite a nota 4: "))

#notas.append(n1)
#notas.append(n2)
#notas.append(n3)
#notas.append(n4)

notas = [n1,n2,n3,n4]

print(f"a maior nota é: {max(notas)}")
print(f"o menor nota é: {min(notas)}")
print(f"a soma é: {sum(notas)}")

media = sum(notas)/len(notas)
print(media)

print("-"*30)
if media >= 7:
    print("aprovado!")
else:
    print("reprovado!")  
print("-"*30)

