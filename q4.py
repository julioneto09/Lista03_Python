'''
Vamos jogar o Jogo da Forca?!?! Crie programa em python que permita que um jogador
insira uma palavra “secreta” e o jogador adversário tente adivinhá-la. É importante que
no final da partida o programa informe qual foi a duração da jogada.
'''
import time
from getpass import getpass#explicado na questão q2. Para omitir o conteúdo do input

def forca():
    '''Desenahndo o boneco'''
    if erro == 1:
        print(' O ')
    if erro == 2:
        print(' O ')
        print('/')
    if erro == 3:
        print(' O ')
        print('/|')
    if erro == 4:
        print(' O ')
        print('/|\\')
    if erro == 5:
        print(' O ')
        print('/|\\')
        print('/')
    if erro == 6:
        print(' O ')
        print('/|\\')
        print('/ \\')
    return(forca)

secreta=list(getpass('Informe a palavra secreta: '))
dica = input('Informe uma dica para a palavra a ser descoberta: ')
print(f'\nUma palavra de {len(secreta)} letras, e a dica é: {dica}')

l=[]#criando os campos a serem preenchidos, com o mesmo tamanho da palavra misteriosa
for k in range(len(secreta)):
    l.append('_')
print(l)

erro=0

start=[]
while (erro<6) and (l != secreta):#o programa vai seguir até errar 6 letras, ou até a palavra "chutada" ser igual a palavra secreta
    x = input('\nInforme uma letra: ')
    start.append(time.time())
    '''o cronômetro começa quando é digitada a primeira letra. É uma lista, pois se não fosse, 
    só registaria o tempo da ultima letra digitada'''
    if x in secreta:#verificando se a letra está contida na palavra
        c = secreta.count(x)#numero de vezes que a letra está na palavra
        pos = 0
        '''substituindo a letra digitada na 'palavra' em branco. Foi usado .pop e .insert para apagar o espaço 
        onde a letra se encontra e só depois acrescentar a letra, garantindo que a lista não mude de tamanho'''
        for k in range(c):
                pos=secreta.index(x,pos)
                l.pop(pos)
                l.insert(pos,x)
                pos = pos+1
    else:#contando os erros
        erro = erro + 1
        print(f'Erro {erro} de 6')
        forca()

    if(erro==6):#Condição de parada. Atingiu o máximo de erros, e o 'cronômetro' é desligado
        print('\nVocê atingiu o número máximo de erros!')
        end = time.time()
    if (l==secreta):#Condição de parada. Acertou a palavra, e o 'cronômetro' é desligado
        print('\nParabens, você acertou!')
        end=time.time()   
    
    print(f'\n{l}')

print(f'\nTempo total: {round(end-start[0],2)}s')