casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Em quantos anos você irá pagar a casa? '))
parcela = casa / (anos * 12)

if parcela >(30/100) * salario:
    print('SEU EMPRESTIMO FOI NEGADO')
else:
    print('SEU EMPRESTIMO FOI ACEITO, VOCÊ RECEBERÁ O VALOR DE R${:.0f}'.format(parcela))