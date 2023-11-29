# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Seu salário é: R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário era {:.2f} e com o reajuste ficou {:.2f}'.format(salario, novo))