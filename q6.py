'''
Crie um programa que leia um arquivo texto e gere um arquivo de saída paginado. Cada
linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas.
Adicione na última linha de cada página o número da página atual e o nome do arquivo
original.
'''

entrada = open('texto_in(Q6).txt','r')#o texto_in(Q6).txt é um lorem ipsum, por comodidade/preguiça
saida = open('texto_out(Q6).txt', 'w')

caractere = int(76)#número máximo de caracteres por linha
linha = int(59)#número máximo de linhas por página(não é 60 pq a ultima linha tem q ter o numero da página)

l = list()#uma lista para receber as linhas do arquivo de entrada
c = 1

for k in range(310):#'310 é um número aleatorio, só para ter uma qunatidade consideravel de linhas
    l.append(entrada.readline(caractere)+'\n')
    '''cada linha vai receber os 76 primeiros digitos do arquivo de entrada, e o \n é a quebra de linha'''
    if k == (c*linha)+(c-1):#Quando chegar numa linha multipla de 59, acrescenta o texto
        msg = ('{0:>50}'.format(f'Pagina {c} do arquivo texto_in.txt\n'))
        saida.write(msg)        
        c=c+1#contando o número de páginas
    else:#para as outras linhas, acrescenta o conteudo do arquivo original, tendo a linha 76 caracteres
        saida.write(f'{l[k]}')

entrada.close()
saida.close()
print('concluido')