## import libs
import pygame
import random
import math
import time
from pygame import mixer

#screen
pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("backgrounds.png")

#import sounds
mixer.music.load("Adel_Shakal_sound_r.wav")
mixer.music.play(-1)
#name and icon
pygame.display.set_caption("Shakloo")
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

## space-invaders
playerimg = pygame.image.load('space-invaders.png')
playerx = 380
playery = 520
playerX_change = 0

## enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('shakal_2.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)

    enemyimg.append(pygame.image.load('shakal_3.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)

    enemyimg.append(pygame.image.load('shakal_4.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)

    enemyimg.append(pygame.image.load('shakal_5.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)

    enemyimg.append(pygame.image.load('shakal_1.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)

    enemyimg.append(pygame.image.load('shakal_0.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,100))
    enemyx_change.append(6)
    enemyy_change.append(40)


bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 520
bulletx_change = 0
bullety_change = 15
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    mixer.music.load("gameover.wav")
    mixer.music.play()


def show_score(x,y):
    score = font.render("Score : " + str(score_value)  , True , (255,255,255))
    screen.blit(score , (x,y))

## functions
def player(x , y):
    screen.blit(playerimg,(x , y))

def enemy(x , y , i):
    screen.blit(enemyimg[i],(x , y))

def fire_bullet(x , y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x+16 , y+10))
def iscollision(enemyx , enemyy , bulletx , bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx ,2))  + (math.pow(enemyy - bullety ,2)))
    if distance < 70:
        return True
    else :
        return False

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background , (0,0))

    for event in pygame.event.get() :
        if event.type  == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("5d_azlfy.wav")
                    bullet_sound.play()
                    fire_bullet(playerx,bullety)
                    bulletx = playerx

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerx += playerX_change

    if playerx <= 0:
        playerx = 0

    elif playerx >=737:
        playerx = 737

    for i in range(num_of_enemies):
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 5 #########################5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >=737:
            enemyx_change[i] = -5#########################-10
            enemyy[i] += enemyy_change[i]

        collision = iscollision(enemyx[i] , enemyy[i] , bulletx , bullety)
        if collision:
            bullety = 520
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0,735)
            enemyy[i] = random.randint(50,100)

        enemy(enemyx[i],enemyy[i] , i)

    if bullety <= 0 :
        bullety = 520
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change


    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()
