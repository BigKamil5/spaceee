import pygame
import Ship
import Enemies
import Collision
import Missiles
import time
import LevelMaker
import random


pygame.init()




white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
smallfont = pygame.font.SysFont("comicsansms", 25)



display_width = 700
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(' SPACE INVADERS ')
clock = pygame.time.Clock()
ship = Ship.Ship(gameDisplay)

enemy = Enemies.Enemies(gameDisplay,110, 50, random.choice((0.1, -0.1)))
level = LevelMaker.LevelMaker(gameDisplay, enemy, 5)

enemy1 = Enemies.Enemies(gameDisplay, 80, 100,  random.choice((0.1, -0.1)))
level1 = LevelMaker.LevelMaker(gameDisplay, enemy1, 6)

enemy2 = Enemies.Enemies(gameDisplay, 110, 150, random.choice((0.1, -0.1)))
level2 = LevelMaker.LevelMaker(gameDisplay, enemy2, 5)

enemy3 = Enemies.Enemies(gameDisplay, 80, 200, random.choice((0.1, -0.1)))
level3 = LevelMaker.LevelMaker(gameDisplay, enemy3, 6)

collision = Collision.Collision()


def game_exit():
    time.sleep(2)
    pygame.quit()
    quit()


def loose():
    for i in Missiles.Missile.missile_list:
        if i.position_y >= ship.position_y and ship.position_x < i.position_x < ship.position_x + ship.block_size:
            text = smallfont.render("GAME OVER", True, red)
            gameDisplay.blit(text, [300, 400])
            pygame.display.update()
            game_exit()

def win():
    for i in Enemies.Enemies.enemy_list:
        if i.position_y >= ship.position_y and ship.position_x < i.position_x < ship.position_x + ship.block_size:
            text = smallfont.render("GAME OVER", True, red)
            gameDisplay.blit(text, [300, 400])
            pygame.display.update()
            game_exit()


def update():
    gameDisplay.fill(black)
    ship.update()
    enemy.update()
    collision.destroy()

    loose()


# --------------------------     GAME LOOP    ------------------------- #
while True:
    #  print("X -> ", ship.position_x)
    for event in pygame.event.get():
        #  print(event)
        if event.type == pygame.QUIT:
            game_exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_exit()
        ship.shoot()
    ship.movement()
    update()
    pygame.display.update()
    clock.tick(130)