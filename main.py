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
    pygame.Rect(LARGURA - 20, 0, 20, ALTURA),

    # Sala de Matemática, aberta para o corredor na parte inferior.
    pygame.Rect(20, 280, 200, 16),
    pygame.Rect(300, 280, 220, 16),
    pygame.Rect(520, 20, 16, 276),

    # Laboratório, com entrada pelo corredor na parte superior.
    pygame.Rect(20, 400, 200, 16),
    pygame.Rect(300, 400, 220, 16),
    pygame.Rect(520, 400, 16, 280),

    # Área de saída, também aberta para o corredor.
    pygame.Rect(690, 20, 16, 276),
    pygame.Rect(690, 280, 110, 16),
    pygame.Rect(880, 280, 100, 16)
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

    # Pisos coloridos destacam o corredor e cada área do mapa.
    tela.fill((62, 68, 70))
    pygame.draw.rect(tela, (105, 112, 108), pygame.Rect(20, 296, 960, 104))
    pygame.draw.rect(tela, (105, 112, 108), pygame.Rect(536, 36, 154, 260))
    pygame.draw.rect(tela, (76, 91, 111), pygame.Rect(36, 36, 484, 244))
    pygame.draw.rect(tela, (75, 105, 94), pygame.Rect(36, 416, 484, 264))
    pygame.draw.rect(tela, (111, 105, 73), pygame.Rect(706, 36, 254, 244))

    # Desenha as paredes
    for parede in paredes:
        pygame.draw.rect(tela, (180, 180, 180), parede)

    # Desenha o jogador
    pygame.draw.rect(tela, (50, 150, 255), jogador)

    pygame.display.flip()

    relogio.tick(60)

pygame.quit()