
contador = 1
M_div = 3

while contador <= 20:
    if contador % M_div == 0:
        print(contador, 'es divisible en', M_div)
    elif contador % 2 == 0:
        print(contador, 'es un número par')
    else:
        print(contador, 'no es un número par')


    contador += 1