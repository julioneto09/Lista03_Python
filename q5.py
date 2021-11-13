'''
Vamos nos divertir jogando o Jogo da Velha?!?! Crie um programa em python do jogo
da velha. Mas, antes de tudo, é necessário definir o jogador que iniciará a jogada, desta
forma, vamos fazer isso usando um dado. Cada jogador irá jogar um dado e aquele que
tirar o maior valor irá iniciar a jogada. No final do jogo é importante informar qual o
jogador vencedor e caso a jogada tenha sido empatada, favor informar que houve
empate.

'''
import random

'''Jogando o dado para definir quem vai começar'''
p1, p2 = int(0), int(0)

while p1 == p2: #Sorteando quem vai começar. Joga o dado até p1 != p2
    p1 = random.randint(1,6)
    p2 = random.randint(1,6)
    print(f'P1: {p1}\nP2: {p2}')

if p1 > p2: #Quem tirou o maior número vai começar
    #print('P1 vai começar!')
    st=str('P1')
    nd=str('P2')
else:
    #print('P2 vai começar!')
    st=str('P2')
    nd=str('P1')


print(f'\n{st} vai começar com o X, e {nd} vai ficar com o O\n')

m1=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3): #mostrando o tabuleiro do jogo da velha
    for j in range(3):
        if j==2:
            print(m1[i][j])
            print('- - - - -')
        else:
            print(f'{m1[i][j]} |', end=' ')

m2=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

livre=[]
for k in range(9):
    livre.append('livre')
print(livre)

def tabuleiro_atualizado():
    '''A cada jogada, o tabuleiro vai atualizando'''
    for i in range(3):
        for j in range(3):
            if j==2:
                print(m2[i][j])
                print('- - - - -')
            else:
                print(f'{m2[i][j]} |', end=' ')
    return(tabuleiro_atualizado)

def posições(a,b):
    '''Sendo (a) a posição e (b) o símbolo.
    Substituindo o tabuleiro vazio pela jogada feita'''
    if a == 1:
        m2[0][0] = b        
    elif a == 2 :
        m2[0][1] = b     
    elif a == 3 :
        m2[0][2] = b       
    elif a == 4 :
        m2[1][0] = b       
    elif a == 5 :
        m2[1][1] = b       
    elif a == 6 :
        m2[1][2] = b      
    elif a == 7 :
        m2[2][0] = b       
    elif a == 8 :
        m2[2][1] = b
    elif a == 9 :
        m2[2][2] = b

    livre.pop(a-1)
    livre.insert(a-1,'ocupado')    
    return(posições)

def ganhar():
    '''Verifica se as linhas/colunas ou diagonais estão preenchidas com X ou O.
    Se estiverem, indica quem ganhou'''
    if (m2[0][0] == m2[1][1] == m2[2][2]):
        #if (m2[0][0] or m2[1][1] or m2[2][2]) == 'X':
        if m2[0][0] == 'X':
            print(f'{st} Ganhou na diagonal!')
        if (m2[0][0] or m2[1][1] or m2[2][2]) == 'O' :
            print(f'{nd} Ganhou na diagonal!')
    for l in range(2):
        if (m2[0][l] == m2[1][l]) and (m2[1][l] == m2[2][l]):
            if m2[0][l] == 'X':
                print(f'{st} Ganhou na coluna {l}!')
            if m2[0][l] == 'O' :
                print(f'{nd} Ganhou na coluna {l}!')
    return(ganhar)

jogadas = int(0)

x=int(0)
y=int(0)

while jogadas < 9: 
    x=int(input(f'{st} (X): Informe a posição que quer jogar: '))

    if livre[x-1] == 'livre': 
        posições(x,'X')
    else:
        print('posição ocupada')

    tabuleiro_atualizado()
    jogadas=jogadas+1
    #print(f'Jogada {jogadas}\n')
    #print(f'\n\nPosições: {livre}')

    y=int(input(f'{nd} (O): Informe a posição que quer jogar: '))

    if livre[x-1] == 'livre': 
        posições(y,'O')
    else:
        print('posição ocupada')

    tabuleiro_atualizado()
    jogadas=jogadas+1
    #print(f'Jogada {jogadas}\n')
    #print(f'\n\nPosições: {livre}')

ganhar()
