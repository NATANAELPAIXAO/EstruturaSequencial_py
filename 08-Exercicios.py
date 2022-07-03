# 8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

horas_trabalhadas = float(input("Digite as horas trabalhadas no mes: "))
valor_por_hora = float(input("Quanto você ganha por hora: "))
calulo = horas_trabalhadas*valor_por_hora
print ("O salario do mes é {}".format(calulo))