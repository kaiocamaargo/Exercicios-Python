#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro R$ 60,00 por dia e R$ 0,15 por KM rodado.
dias_alugados = int(input('Quantos dias alugados?'))
km_rodados = int(input('Quantos Km rodados'))
preco_por_dia = 60 * dias_alugados
preco_por_km = 0.15 * km_rodados
total = preco_por_dia + preco_por_km
print('O total a pagar é de R$ {}'.format (total))