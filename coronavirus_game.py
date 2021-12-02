import pygame
import random

pygame.init()

score = 0
clock = pygame.time.Clock()

screenWidth = 640
screenHeight = 540

screen = pygame.display.set_mode((screenWidth, screenHeight))

background = pygame.image.load("resources/images/background..png")

pygame.mixer.music.load("resources/sound/dark_music.bgm.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

player = pygame.image.load("resources/images/player1.png")
playerSize = player.get_rect().size
playerWidth = playerSize[0]
playerHeight = playerSize[1]
playerXpos = (screenWidth / 2) - (playerWidth / 2)
playerYpos = screenHeight - playerHeight

toX = 0
toY = 0

playerSpeed = 0.6

randomNumber = 30
poSpeed = 10

coronavirus = pygame.image.load("resources/images/coronavirus.png")
coronavirusSize = coronavirus.get_rect().size
coronavirusWidth = coronavirusSize[0]
coronavirusHeight = coronavirusSize[1]
coronavirusXpos = 200
coronavirusYpos = 100

pygame.display.set_caption("코로나바이러스 피하기 게임")

game_font = pygame.font.Font(None, 40)

running = True
while running:
    dt = clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= playerSpeed
            if event.key == pygame.K_RIGHT:
                toX += playerSpeed
            if event.key == pygame.K_UP:
                toY -= playerSpeed
            if event.key == pygame.K_DOWN:
                toY += playerSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0

    playerXpos += toX * dt
    playerYpos += toY * dt

    if playerXpos < 0:
        playerXpos = 0
    elif playerXpos > screenWidth - playerWidth:
        playerXpos = screenWidth - playerWidth
    if playerYpos < 0:
        playerYpos = 0
    elif playerYpos > screenHeight - playerHeight:
        playerYpos = screenHeight - playerHeight

    randomNumber = random.randrange(1, 200)
    randomNumber2 = random.randrange(1, 440)

    if coronavirusYpos > 640:
        coronavirusYpos = randomNumber
        coronavirusXpos = randomNumber2
        score += 1
        poSpeed += 2

    coronavirusYpos += poSpeed

    playerRect = player.get_rect()
    playerRect.left = playerXpos
    playerRect.top = playerYpos

    coronavirusRect = coronavirus.get_rect()
    coronavirusRect.left = coronavirusXpos
    coronavirusRect.top = coronavirusYpos

    if playerRect.colliderect(coronavirusRect):
        print("충돌")
        running = False

    scoree = game_font.render(str(score), True, (200, 200, 200))

    screen.blit(background, (0, 0))
    screen.blit(player, (playerXpos, playerYpos))
    screen.blit(coronavirus, (coronavirusXpos, coronavirusYpos))
    screen.blit(scoree, (10, 30))
    pygame.display.update()

pygame.quit()