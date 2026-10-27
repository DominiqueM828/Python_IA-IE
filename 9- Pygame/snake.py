#Importando a biblioteca Pygame 
from sys import exit
import pygame
from pygame.locals import *

#-----1. Criando a Janela------
pygame.init() #Inicializa o Pygame

#1--Configura as dimenções da janela e cria a tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
#1--Definindo título do jogo 
pygame.display.set_caption("Snake Game")

#1--Cria o relógio para controlar os FPS
relogio = pygame.time.Clock()

#-----2. Definindo o tamnho dos blocos e o fundo-----
GRAMADO_TAM = 20 # Largura x Altura em pixels
FUNDO = (170,215,81) #(R,G,B)
COR_GRAMA = (162,209,73)

#-----4. A estrutura e o Estado Inicial da Cobra------
inicio = [
    pygame.Rect(x,200,GRAMADO_TAM,GRAMADO_TAM)
    for x in (80,60,40)
]
cobra = inicio.copy()

#-----5. Movimento Automático da Cobra------
velocidade_x = GRAMADO_TAM
velocidade_y = 0

#1--Lopping que mantém a janela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    #-----6. Controles do teclado------
        elif evento.type == KEYDOWN:
            if (evento.key == K_LEFT or evento.key == K_a) and velocidade_x == 0:
                velocidade_x = -GRAMADO_TAM
                velocidade_y = 0
            elif (evento.key == K_RIGHT or evento.key == K_d) and velocidade_x == 0:
                velocidade_x = GRAMADO_TAM
                velocidade_y = 0
            elif (evento.key == K_UP or evento.key == K_w) and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = -GRAMADO_TAM
            elif (evento.key == K_DOWN or evento.key == K_s) and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = GRAMADO_TAM

    #5--Atualizando a Posição da Cobra
    cabeca = pygame.Rect(
        cobra[0].x + velocidade_x,
        cobra[0].y + velocidade_y,
        GRAMADO_TAM,
        GRAMADO_TAM
    )
    cobra.insert(0,cabeca) #Incere novo elemento na cabeça
    cobra.pop() #Remove o último da lista cobra

    #2--Pintando toda a tela com a cor de fundo
    tela.fill(FUNDO)

    #-----3. Desenhando o Fundo Quadriculado (Grama)------
    for x in range(0,LARGURA,GRAMADO_TAM):
        for y in range(x % 40, ALTURA, 40):
            pygame.draw.rect(
                tela,
                COR_GRAMA,
                (x,y,GRAMADO_TAM,GRAMADO_TAM)
            )
    #4--Desenhando na tela a cobra
    for parte in cobra:
        pygame.draw.rect(
            tela, 
            "Purple",
            parte,0,6
        )

    #1--Atualiza o que aparece na tela
    pygame.display.flip()

    #1--Mantém a taxa de 10 quadros por segundo
    relogio.tick(5)

#1--Encerra o pygame corretamente
pygame.quit()
exit()