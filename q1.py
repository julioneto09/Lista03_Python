'''Pense em um problema do seu dia a dia que pode ser automatizado. Utilize conceitos
de RPA:
a. Defina o problema a ser automatizado.
b. Apresente o algoritmo do programa utilizando fluxograma.
c. Implemente um programa que solucione o problema. Use as bibliotecas
pyautogui e time.'''

'''
a) Entrar na sala de aula virtual.'''

'''
b) 
-> *Abrir* menu do windows 
-> *Digitar* chrome para abrir o navegador
-> *Clicar* no botão dos favoritos da aula
-> *Clicar* para desligar o video
-> *Clicar* para desligar o audio
-> *Clicar* para entrar
'''

#c)

import pyautogui as pag
import time

pag.alert('\tO processo vai começar...\nNão mexer no teclado nem no mouse!')

pag.PAUSE = 2

pag.press('win')

pag.write('chrome')

pag.press('enter')
time.sleep(20)

pag.moveTo(55,85)#clicar no link da aula
pag.leftClick()
time.sleep(10)

pag.click(x=490, y=600)#desligar a câmera

pag.click(x=405, y=600)#desligar o microfone

pag.click(x=975, y=475)#participar



