'''Crie um módulo chamado matematica e dentro dele crie funções capazes de realizar as
operações básicas (soma, subtração multiplicação e divisão), bem como insira
funcionalidades de uma calculadora científica (exponenciação, log, seno, cosseno, etc).
Após a criação do módulo faça um programa com diferentes operações (cálculo da área,
volume, MDC, entre outros) utilizamos, apenas, as funções criadas. Para facilitar crie
um menu para que o usuário possa escolher o que ele deseja calcular.'''

import time, matematica as ma



while True:
    print('\tOperações: \n1. Área de um retângulo\n2. Área do triângulo\n3. Área do círculo\n4. Seno\
        \n5. Cosseno\n6. Tangente\n7. Fatorial\n8. Potência de Euler\nOutro numero para sair')
    calc=int(input('\nQue operação deseja realizar: '))

    if calc==1:
        print('\tÁrea de um retângulo')
        x=float(input('Comprimento: '))
        ma.teste(x)
        
        y=float(input('Altura: '))
        ma.teste(y)
        
        print(f'\nA área de um retângulo com lados {x} m e {y} m é: {ma.multiplicar(x,y)} m²\n')
        time.sleep(3)

    elif calc==2:
        print('\tÁrea do triângulo')
        x=float(input('Base: '))
        ma.teste(x)

        y=float(input('Altura: '))
        ma.teste(y)
        
        a = ma.multiplicar(x,y)
        b = ma.dividir(a,2)
        print(f'\nÁrea do triângulo com base {x} m e altura {y} m é: {b} m²\n')
        time.sleep(3)
    
    elif calc==3:
        print('\tÁrea do círculo')
        x=float(input('Raio do círculo: '))
        ma.teste(x)

        a = ma.multiplicar(ma.pi(),ma.potencia(x,2))
        print(f'\nÁrea da circunferência com raio {x} m é: {a} m²\n')
        time.sleep(3)

    elif calc==4:
        print('\tSeno')
        x=float(input('Informe o ângulo: '))
        ma.teste(x)

        sen = ma.seno(x)
        print(f'\nO seno do ângulo {x}° é: {round(sen,4)}\n')
        time.sleep(3)

    elif calc==5:
        print('\tCosseno')
        x=float(input('Informe o ângulo: '))
        ma.teste(x)

        cos = ma.cosseno(x)
        print(f'\nO coseno do ângulo {x}° é: {round(cos,4)}\n')
        time.sleep(3)
            
    elif calc==6:
        print('\tTangente')
        x=float(input('Informe o ângulo: '))
        ma.teste(x)

        tan = ma.tangente(x)
        print(f'\nA tangente do ângulo {x}° é: {round(tan,4)}\n')
        time.sleep(3)
    
    elif calc==7:
        print('\tFatorial')
        x=int(input('Informe o número: '))
        ma.teste(x)

        fat = ma.fatorial(x)
        print(f'\nO fatorial de {x} é: {fat}\n')
        time.sleep(3)
    
    elif calc==8:
        print('\tPotência de Euler')      
        x=float(input('Informe o número: '))
        ma.teste(x)

        e = ma.euler(x)
        print(f'\ne^{x} é: {e}\n')
        time.sleep(3)
    else:
        print('Saindo...')
        break