import pygame

pygame.init()

LARGURA = 1000
ALTURA = 700

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Escape Room Escolar")

relogio = pygame.time.Clock()

# Jogador
jogador = pygame.Rect(475, 325, 50, 50)
velocidade = 5

# Paredes do mapa
paredes = [
    pygame.Rect(0, 0, LARGURA, 20),
    pygame.Rect(0, ALTURA - 20, LARGURA, 20),
    pygame.Rect(0, 0, 20, ALTURA),
    pygame.Rect(LARGURA - 20, 0, 20, ALTURA)
]

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimento horizontal
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        jogador.x -= velocidade

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        jogador.x += velocidade

    # Colisão horizontal
    for parede in paredes:
        if jogador.colliderect(parede):
            if jogador.x < parede.x:
                jogador.right = parede.left
            else:
                jogador.left = parede.right

    # Movimento vertical
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        jogador.y -= velocidade

    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # Colisão vertical
    for parede in paredes:
        if jogador.colliderect(parede):
            if jogador.y < parede.y:
                jogador.bottom = parede.top
            else:
                jogador.top = parede.bottom

    # Fundo
    tela.fill((30, 30, 30))

    # Desenha as paredes
    for parede in paredes:
        pygame.draw.rect(tela, (180, 180, 180), parede)

    # Desenha o jogador
    pygame.draw.rect(tela, (50, 150, 255), jogador)

    pygame.display.flip()

    relogio.tick(60)

pygame.quit()