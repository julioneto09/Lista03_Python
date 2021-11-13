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

def potencia(x,y):
    '''Retorna o resultado de 'x' elevado a 'y' '''
    pot = x**y
    return(pot)

def pi():
    '''Retorna o número pi'''
    n_pi = 3.14159265359
    return(n_pi)

def e():
    '''Retorna o número de Euler'''
    n_e = 2.718281828
    return(n_e)

def fatorial(x):
    '''Retorna o fatorial do número 'x' '''
    n=1
    if x <0:
        print('Não existe fatorial de número negativo!')
        exit()
    elif x<1:
        f = 1
    else:
        for k in range(1,x+1):
            f = n*k
            n=f
    return(f)

def euler(x):
    '''Retorna o número de euler elevado ao numero 'x' '''
    '''Como não pode usar a biblioteca math, escrevi 'e^x' (bem como seno, cosseno e tangente), 
    como séries de McLaurin ('for k in range()' faz o somatório)'''
    e_x = 0
    for k in range(0,50):
        o1 = potencia(x,k)
        o2 = dividir(o1,fatorial(k))
        e_x = somar(e_x,o2)
    return(e_x)

def seno(x):
    '''Dado um angulo 'x' em graus, retorna o valor de seu seno'''
    sen = 0
    angulo_radiano = multiplicar(x, dividir(pi(),180))
    for k in range(0,50):
        o1 = potencia(-1,k)
        o2 = potencia(angulo_radiano,somar(multiplicar(2,k),1))
        o3 = multiplicar(o1,o2)
        o4 = fatorial(somar(multiplicar(2,k),1))
        o5 = dividir(o3,o4)

        sen = somar(sen,o5)
    return(sen)

def cosseno(x):
    #Dado um angulo 'x' em graus, retorna o valor de seu cosseno
    cos=0
    angulo_radiano = multiplicar(x, dividir(pi(),180))
    for k in range(0,50):
        #cos = cos + potencia(-1,k) * potencia(angulo_radiano,2*k)/fatorial(2*k)
        cos = somar(cos,dividir(multiplicar(potencia(-1,k),potencia(angulo_radiano,multiplicar(2,k))),fatorial(multiplicar(2,k))))
    return(cos)

def tangente(x):
    #Dado um angulo 'x' em graus, retorna o valor da sua tangente
    if abs(cosseno(x))<0.0001:
        tan = print('Tende ao infinito!')
        exit()
    else:
        tan = dividir(seno(x),cosseno(x))

    return(tan)


'''
def logaritmo(x,y):
    #Retorna o logaritmo do numero 'x' na base 'y' 
    log = math.log(x,y)
    return(log)
'''




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