# Importando as dependencias 
import pygame
from pygame.locals import *

from sys import exit
from random import randint

# Inicializando constantes e variaveis 
pygame.init()

# Configuração de música e sons
pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer_music.load('fundo.mp3')
pygame.mixer_music.play(-1)
som_colisao = pygame.mixer.Sound('smw_coin.wav')

# Configuração da tela de jogo

fonte = pygame.font.SysFont('arial', 20, True)
tela_x = 1200 # Largura da tela
tela_y = 700 # Altura da tela

tela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption('Explorando mecanica de jogos')
framer = pygame.time.Clock()

# Configuração de objetos
preto_x = tela_x / 2 - 50
preto_y = tela_y / 2 - 50

azul_x = randint(100, 1100)
azul_y = randint(100, 600)

pontos = 0

while True:
    framer.tick(1000)
    tela.fill((255, 255, 255)) # Cor da tela de jogo
    pontuacao = f'Pontuação: {pontos}'
    texto = fonte.render(pontuacao, True, (100, 200, 255))
    # Captura de eventos ocorrendo no jogo (Teclas, mouse etc)
    for evento in pygame.event.get():
        if evento.type == QUIT: # Evento igual a saida ele fecha a tela de jogo
            exit()

    # Desenhando objetos na tela (Figuras geometricas)
    preto = pygame.draw.rect(tela, (0, 0, 0), (preto_x, preto_y, 100, 100), 10, 5)
    azul = pygame.draw.rect(tela, (10, 10, 255), (azul_x, azul_y, 100, 100), 10, 5)

    # Controlo de objeto preto apartir do teclado
    if pygame.key.get_pressed()[K_l]:
        preto_x += 1    
    if pygame.key.get_pressed()[K_j]:
        preto_x -= 1
    if pygame.key.get_pressed()[K_k]:
        preto_y += 1
    if pygame.key.get_pressed()[K_i]:
        preto_y -= 1

    # Efeitos da colisão
    if preto.colliderect(azul):
        azul_x = randint(100, 1100) # Troca de posição quando colide com o objeto preto
        azul_y = randint(100, 600)
        pontos += 1
        som_colisao.play()
    # Coloca a pontuação na tela de jogo
    tela.blit(texto, (50, 50))

    # Atualiza a tela de jogo
    pygame.display.update()