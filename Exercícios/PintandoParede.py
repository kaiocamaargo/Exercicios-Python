#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede: '))
área = larg * alt
print('A sua parede tem a dimensão de {}x{} e a sua área é de {}m².'.format(larg,alt,área))
tinta = área / 2
print('Para pinta essa parede, você precisará de {}l de tinta.'.format(tinta))