'''
Estamos monitorando a temperatura de uma máquina. Faça um programa que envie
um alerta por e-mail de forma automática. O e-mail deverá ser enviado quando o valor
da temperatura for superior a 40°C. Desta forma, no e-mail deverá informar qual a
temperatura que foi registrada, o horário e lembrar que é um ALERTA DE
TEMPERATURA. Use a biblioteca smtplib e time.
'''
import smtplib, random, time, getpass

destino = input("Informe o e-mail que receberá os alertas: ")
v = int(input('Informe quantas verificação serão feitas: '))
i = int(input('Informe o intervalo das verificações, em segundos: '))

'''Para apresentar o código na sala, e não mostrar minha senha'''
meu_email = input('\nInforme seu email, o que enviará os dados: ')
senha = getpass.getpass(prompt='Digite a senha do seu email para enviar os dados: ')

maior=[]
tempo=[]

''' "Lendo" as temperaturas (x) aleatórias, e registrando o horário em que foram obtidas'''
for k in range(v):
    x = 100*random.random()
    tempo.append(time.strftime('%H:%M:%S'))
    time.sleep(i)
    print(f'\nTemperatura de: {round(x,2)}°C as {tempo[k]}')
    '''Salvando as temperaturas que forem maiores que 40°C'''
    if x > 40.0:
        maior.append(x)

if maior != []:
    for c in range(len(maior)):
        #print(f'\nTemperatura de: {round(maior[c],2)}°C as {tempo[c]}')
        '''Enviando e-mail:'''
        try:
            email = smtplib.SMTP('smtp.gmail.com', 587)
            email.ehlo()
            email.starttls()
            #meu_email = 'julioneto09@gmail.com'
            #senha = ''
            email.login(meu_email, senha)
            '''Se em "mensagem" tiver os caracteres "°" e ":", a mensagem enviada é vazia/nula,
            por isso, sua sintaxe está mais "complicada" que o normal'''
            mensagem = 'Temperatura de {} graus, as {}h e {}min e {}s'\
                .format(round(maior[c],2), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'))          
               
            email.sendmail(meu_email,destino,'Subject: Aletra de temperatura\n{}'.format(mensagem))
            #smtpObj.quit()
            print('Email enviado!')
        except:
            print('Erro ao enviar e-mail')
