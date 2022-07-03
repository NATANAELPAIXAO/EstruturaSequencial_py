# 9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
# mostre a temperatura em graus Celsius.

f = float(input("Digite a temperatura Fahrenheit: "))
c = 5 * ((f - 32) / 9)
print("A temperatura em º Celsius é {}".format(c))