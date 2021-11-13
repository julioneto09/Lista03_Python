'''Crie um módulo chamado matematica e dentro dele crie funções capazes de realizar as
operações básicas (soma, subtração multiplicação e divisão), bem como insira
funcionalidades de uma calculadora científica (exponenciação, log, seno, cosseno, etc).
Após a criação do módulo faça um programa com diferentes operações (cálculo da área,
volume, MDC, entre outros) utilizamos, apenas, as funções criadas. Para facilitar crie
um menu para que o usuário possa escolher o que ele deseja calcular.'''

import time, matematica as ma

while True:
    print('\tOperações: \n1. Área de um retângulo\n2. Área do triângulo\n3. Área do círculo\n4. Seno\nOutro numero para sair')
    calc=int(input('\nQue operação deseja realizar: '))

    if calc==1:
        while True:
            try:
                x=float(input('\nComprimento: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break
        while True:
            try:
                y=float(input('Altura: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break           
        print(f'\nA área de um retângulo com lados {x} m e {y} m é: {ma.multiplicar(x,y)} m²\n')
        time.sleep(3)

    elif calc==2:
        while True:
            try:
                x=float(input('\nBase: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break
        while True:
            try:
                y=float(input('Altura: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break           
        a = ma.multiplicar(x,y)
        b = ma.dividir(a,2)
        print(f'\nÁrea do triângulo com base {x} m e altura {y} m é: {b} m²\n')
        time.sleep(3)
    
    elif calc==3:
        while True:
            try:
                x=float(input('\nRaio do círculo: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break
        a = ma.multiplicar(ma.pi(),ma.potencia(x,2))
        print(f'\nÁrea da circunferência com raio {x} m é: {a} m²\n')
        time.sleep(3)

    elif calc==4:
        while True:
            try:
                x=float(input('\nInforme o ângulo: '))
            except ValueError:
                print('Digite um número!')
                continue
            else:
                break 
        sen = ma.seno(x)
        print(f'\nO seno do ângulo {x}° é: {round(sen,4)}\n')
        time.sleep(3)
    else:
        print('sair')
        break