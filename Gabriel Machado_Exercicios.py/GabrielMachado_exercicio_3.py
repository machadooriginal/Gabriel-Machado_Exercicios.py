lista_altura_mulher = []
lista_nome_homem = []
lista_idade = []
lista_sexo = []
lista_idade_homem = []
lista_idade_mulher = []
percentual_idades = []

for c in range (1,5):
    print('-------------- {}ª pessoa ----------------'.format(c))
    altura= str(input('Digite a altura: ')).strip().upper()
    lista_altura_mulher.append(altura)

    idade = int(input('Digite a idade: '))
    lista_idade.append(idade)

    sexo = str(input('Digite o sexo 0/1: ')).strip().upper()
    lista_sexo.append(sexo)

    percentual = str(input('Digite as idades 0/1')).strip().upper()

    if sexo == '1':
        lista_idade_homem.append(idade)
    if sexo == '0' and idade < 20:
        lista_idade_mulher.append(idade)
        lista_altura_mulher.append(altura)

print('A média de idade do grupo é {}'.format(sum(lista_idade)/len(lista_idade)))
print('A média da altura das mulheres é {}'.format(sum(lista_altura_mulher)/len(lista_altura_mulher)))
print('A média de idade dos homens é {}' .format(sum(lista_idade_homem)/len(lista_idade)))
print('O percentual de idade entre 18 e 35 anos é {}'.format(sum(percentual_idades)/len(percentual_idades)))