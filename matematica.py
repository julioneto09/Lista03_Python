'''Módulo contendo operções matemáticas'''
import math

def somar(x,y):
    '''Dados dois numeros ('x' e 'y'), a função retorna a soma destes números '''
    mais = x+y
    return(mais)

def subtrair(x,y):
    '''Dados dois números ('x' e 'y'), a função retorna diferença entre x e y'''
    menos = x - y
    return(menos)

def multiplicar(x,y):
    '''Dados dois números ('x' e 'y'), a função retorna o produto entre eles'''
    vezes = x*y
    return(vezes)

def dividir(x,y):
    '''Dados dois números ('x' o numerador e 'y' o denominador), 
    a função retorna o quociente entre x e y'''
    while True:
        try:
            div = x/y
            #print(div)
        except ZeroDivisionError:
            print('O denominador não pode ser zero!')
            break
        else:
            break
    return(div)

def exponencial(x,y):
    '''Retorna o resultado de 'x' elevado a 'y' '''
    exp = x**y
    return(exp)

def logaritmo(x,y):
    '''Retorna o logaritmo do numero 'x' na base 'y' '''
    log = math.log(x,y)
    return(log)

def seno(x):
    '''Dado um angulo 'x' em graus, retorna o valor de seu seno'''
    a = math.radians(x)
    sen = math.sin(a)
    return(sen)

def cosseno(x):
    '''Dado um angulo 'x' em graus, retorna o valor de seu cosseno'''
    a = math.radians(x)
    cos = math.cos(a)
    return(cos)

def tangente(x):
    '''Dado um angulo 'x' em graus, retorna o valor da sua tangente'''
    a = math.radians(x)
    tan = math.tan(a)
    return(tan)





'''
Soma com varios termos
qte = int(input('Informe quantos termos da soma: '))
k=0
for num in range(kk):
    num = int(input(f'o termo {qte+1}: '))
    w=somar(k,num)
    k=w
    
print(w)
'''

'''

'''
