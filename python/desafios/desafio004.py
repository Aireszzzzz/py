# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivéis sobre ele.
n = input('Digite um valor: ')
print('É numérico?',n.isnumeric())
print('É alfanumérico?',n.isalnum())
print('É alfabético?',n.isalpha())
print('Está em maiúsculo?',n.isupper())
print('Está em minúsculo?',n.islower())
print('É printável?',n.isprintable())

