#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. 
produto = float(input('Qual é o preço do produto?'))
desconto = produto * (5/100)
preco_final = produto - desconto
print('O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}'.format(produto, preco_final))