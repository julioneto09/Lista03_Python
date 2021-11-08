'''
Vamos jogar o Jogo da Forca?!?! Crie programa em python que permita que um jogador
insira uma palavra “secreta” e o jogador adversário tente adivinhá-la. É importante que
no final da partida o programa informe qual foi a duração da jogada.
'''
import time

nome = list(input('Informe uma palavra: '))
#dica = input('Informe uma dica: \n')

l=[]
for k in range(len(nome)):
    l.append('_')
print(l)

erro=0
tempo=[]
while (erro<5) and (l != nome):
    x = input('\nInforme uma letra: ')
    tempo.append(time.strftime('%H:%M:%S'))
    if x in nome:
        c = nome.count(x)
        pos = 0
        for k in range(c):
                pos=nome.index(x,pos)
                l.pop(pos)
                l.insert(pos,x)
                pos = pos+1
    else:
        erro = erro + 1
        print(f'Erro {erro} de 5')
    if(erro==5):
        print('\nVocê atingiu o número máximo de erros!')
        tt=time.strftime('%H:%M:%S')
    if (l==nome):
        print('\nParabens, você acertou!')
        tt=time.strftime('%H:%M:%S')    
    print(l)

print(f'Começou: {tempo[0]}')
print(f'Acabou: {tt}')