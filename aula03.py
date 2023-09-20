


""" aprovado ou não aprovado"""

media = 8.5

if (media >= 7.0):
    situacao = "Aprovado"
elif (media >= 5.0):
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"

print(f'O estudante está: {situacao}')
