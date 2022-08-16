from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos de idade'.format(nasc, idade))

if idade == 18:
    print('Você tem que se alistar ao exército! ')

elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} ano(s) para você se alistar'.format(saldo))

elif idade > 18:
    saldo2 = idade - 18
    print('Você ja deveria ter se alistado há {} ano(s)'.format(saldo2))