# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar, considere US$1,00 = 3,27
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.89
euro = real / 5.22
print('Com {:.2f} reais, você consegue comprar U${:.2f} e €{:.2f}'.format(real, dolar, euro))