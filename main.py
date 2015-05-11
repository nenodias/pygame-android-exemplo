# *-* coding: utf-8 *-*
import pygame
from pygame.locals import *
# Importando o modulo android, específico para android
try:
    import android
except ImportError:
    android = None

TIMEREVENT = pygame.USEREVENT

# FPS
FPS = 30

#Cores
COR_TRANSPARENTE = (100,100,100,128)

RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0,0,255,255)
WHITE = (255,255,255,255)
BLACK = (0,0,0,255)
YELLOW = (255, 255, 0, 255)
AZUL_CLARO = (0, 255, 255, 255)
ROXO = (255, 0, 255, 255)

color = RED

LARGURA = 800
ALTURA = 480

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.key.set_repeat(1, 10)


class Controle():

    def __init__(self, largura, altura):
        tamanho_botao = 80
        espacamento = 50
        X_CIMABAIXO = 150
        Y_BAIXO = altura - tamanho_botao
        Y_CIMA = altura - (2*tamanho_botao) - ( espacamento *2 )
        Y_ESQUERDADIREITA = altura - (2*tamanho_botao) - int(espacamento / 10)
        X_ESQUERDA = X_CIMABAIXO - ( espacamento *2 )
        X_DIREITA = X_CIMABAIXO + ( espacamento *2 )

        X_ACAO1 = LARGURA - ( espacamento *2 ) - int( tamanho_botao * 1.75 )
        X_ACAO2 = LARGURA - ( espacamento *2 )

        self.botao_cima = pygame.Rect(X_CIMABAIXO,Y_CIMA,tamanho_botao,tamanho_botao)
        self.botao_baixo = pygame.Rect(X_CIMABAIXO,Y_BAIXO,tamanho_botao,tamanho_botao)
        self.botao_esquerda = pygame.Rect(X_ESQUERDA,Y_ESQUERDADIREITA,tamanho_botao,tamanho_botao)
        self.botao_direita = pygame.Rect(X_DIREITA,Y_ESQUERDADIREITA,tamanho_botao,tamanho_botao)

        self.botao_acao1 = pygame.Rect(X_ACAO1,Y_ESQUERDADIREITA,tamanho_botao,tamanho_botao)
        self.botao_acao2 = pygame.Rect(X_ACAO2,Y_ESQUERDADIREITA,tamanho_botao,tamanho_botao)
        self.cor = None

    def evento(self, evento, cor):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(self.botao_cima.collidepoint(pos)):
                self.cima()
            if(self.botao_baixo.collidepoint(pos)):
                self.baixo()
            if(self.botao_esquerda.collidepoint(pos)):
                self.esquerda()
            if(self.botao_direita.collidepoint(pos)):
                self.direita()
            if(self.botao_acao1.collidepoint(pos)):
                self.acao1()
            if(self.botao_acao2.collidepoint(pos)):
                self.acao2()
        elif evento.type == pygame.MOUSEBUTTONUP:
            self.botao_solto()
        elif evento.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                self.cima()
            if keys[K_DOWN]:
                self.baixo()
            if keys[K_LEFT]:
                self.esquerda()
            if keys[K_RIGHT]:
                self.direita()
            if keys[K_LSHIFT]:
                self.acao1()
            if keys[K_LCTRL]:
                self.acao2()
        elif evento.type == KEYUP:
            self.botao_solto()

    def cima(self):
        self.cor = GREEN
    def baixo(self):
        self.cor = BLUE
    def esquerda(self):
        self.cor = YELLOW
    def direita(self):
        self.cor = BLACK
    def acao1(self):
        self.cor = AZUL_CLARO
    def acao2(self):
        self.cor = ROXO
    def botao_solto(self):
        self.cor = RED

    def desenha(self, screen):
        if(self.cor):
            screen.fill(self.cor)
        superficie = pygame.Surface((LARGURA, ALTURA))
        superficie.fill(COR_TRANSPARENTE)
        superficie.set_colorkey(COR_TRANSPARENTE)
        pygame.draw.rect(superficie, WHITE, self.botao_cima)
        pygame.draw.rect(superficie, WHITE, self.botao_baixo)
        pygame.draw.rect(superficie, WHITE, self.botao_esquerda)
        pygame.draw.rect(superficie, WHITE, self.botao_direita)
        pygame.draw.rect(superficie, WHITE, self.botao_acao1)
        pygame.draw.rect(superficie, WHITE, self.botao_acao2)
        superficie.set_alpha(60)
        screen.blit(superficie, (0, 0))

def main():
    # Mapeando o botao voltar do android como K_ESCAPE (ESC)
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    # Usando timer para controlar os FPS
    pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    # A cor da tela
    global color
    controle = Controle(LARGURA,ALTURA)
    while True:

        ev = pygame.event.wait()

        # Especifico para android
        if android:
            if android.check_pause():
                android.wait_for_resume()

        if ev.type == TIMEREVENT:
            screen.fill(color)
            controle.desenha(screen)
            pygame.display.flip()
        else:
            controle.evento(ev, color)

        if (ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE) or ev.type == pygame.QUIT:
            break

if __name__ == "__main__":
    main()