import pygame
import random
from threading import Thread
import Missiles


class Enemies:
    enemy_list = []
    counter = 0
    myimage = pygame.image.load("shi.jpg")

    def __init__(self, window, x, y, direction):
        self.window = window
        self.position_x = x
        self.position_y = y
        self.size = 20
        self.color = (0, 0, 255)
        self.missile_color = (255, 255, 255)
        self.ID = self.__class__.counter = self.__class__.counter + 1
        self.__class__.enemy_list.append(self)
        self.enemy_rect = pygame.draw.rect(self.window, self.color, [self.position_x, self.position_y, self.size, self.size])

        self.move_counter = 0
        self.move_speed = direction

    def update(self):
        for i in Enemies.enemy_list:
            self.enemy_rect = pygame.draw.rect(i.window, i.color, [i.position_x, i.position_y, i.size, i.size])
            self.window.blit(Enemies.myimage, self.enemy_rect)
            i.move()
            if random.randint(0, 150) == 0:
                i.shoot()

#  ruch wahadlowy wrogow
    def move(self):
        if self.move_speed > 0:
            self.position_x += self.move_speed
            self.move_counter += 1
            #print ("COUNTER : ",self.move_counter)
            if self.move_counter == 200:
                self.move_speed = -0.1
                self.move_counter = 0

        if self.move_speed < 0:
            self.position_x += self.move_speed
            self.move_counter += 1
            if self.move_counter == 200:
                self.move_speed = 0.1
                self.move_counter = 0

    def shoot(self):
        Missiles.Missile(self, self.position_y, -1, self.missile_color)



