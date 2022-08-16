nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 6:
    print('A sua média foi {} então você foi reprovado'.format(media))
elif media > 6 < 6.5:
    print('A sua média foi {}, então você ficou de recuperação'.format(media))
else:
    print('Parabéns, você foi aprovado \nA média do aluno foi {}'.format(media))