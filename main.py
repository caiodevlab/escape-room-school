import pygame

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Escape Room Escolar")

relogio = pygame.time.Clock()

# Jogador
jogador = pygame.Rect(375, 275, 50, 50)
velocidade = 5

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        jogador.y -= velocidade

    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        jogador.x -= velocidade

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        jogador.x += velocidade

    # Fundo
    tela.fill((30, 30, 30))

    # Desenha o jogador
    pygame.draw.rect(tela, (50, 150, 255), jogador)

    pygame.display.flip()

    relogio.tick(60)

pygame.quit()