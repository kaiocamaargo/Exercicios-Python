#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Qual é o salário do Funcionário?'))
aumento = salario * (15/100)
salario_final = salario + aumento
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, salario_final))