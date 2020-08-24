
# Calculadora criada para realizar operações aritiméticas em Binário.
def calcular():
    # input para receber os operadores.
    operacao = input('''
    Por favor, selecione o operador desejado:
    ( + ) Para Soma
    ( - ) Para Subtração
    ( * ) Para Multiplição
    ( / ) Para Dvivisão 
    ( % ) Para Porcentagem 
    ''')

    # Bloco criado para receber o input do primeiro número Binário.
    while True:

        if operacao == '%':
            binario1 = int(input('Por favor, digite a porcentagem desejada: '))
            b1 = str(binario1)
            numero1 = int(b1, 2)

        if operacao != '%':
            binario1 = int(input('Por favor, digite o primeiro número binário entre 0 e 255: '))
            b1 = str(binario1)
            numero1 = int(b1, 2)

        if numero1 < 0 or numero1 > 255:
            print('Você digitou o numero {}, por favor digite um numero entre 0 e 255.'.format(numero1))

        else:
            break

    # Bloco criado para receber o input do segundo número Binário.
    while True:
        binario2 = int(input('Por favor, digite o segundo número binário ente 0 - 255: '))
        b2 = str(binario2)
        numero2 = int(b2, 2)

        if numero2 < 0 or numero2 > 255:
            print('Você digitou o número {} '.format(numero2))
            print('Por favor, digite um número em binário entre 0 - 255 ')

        else:
            break

    # Bloco contendo as fórmulas definidas pelos operadores aritiméticos.
    if operacao == '+':
        resultado = numero1 + numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} + {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '-':
        resultado = numero1 - numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} - {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '*':
        resultado = numero1 * numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} * {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '/':
        resultado = numero1 / numero2
        d = int(resultado)
        resultadoFinal = (bin(d)[2:])
        print('{} / {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '%':
        resultado = (numero1 * numero2 / 100)
        p = int(resultado)
        resultadoFinal = (bin(p)[2:])
        print('{} % de {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    # Mensgem exibida ao digitar um operador inválido.
    else:
        print('Você não escolheu um operador válido, por favor escolha novamente.')

    again()


# Função criada para dar continuidade ao programa caso seja solicitado sim ou não.
def again():
    calc_again = input('''
Você deseja calcular novamente ?
Por favor aperte Y para sim ou N para não.
''')

    if calc_again.upper() == 'Y':
        calcular()
    elif calc_again.upper() == 'N':
        print('Até breve!.')
    else:
        again()


calcular()
