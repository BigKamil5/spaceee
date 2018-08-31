import pygame
import Missiles


class Ship:
    myimage = pygame.image.load("nie.jpg")

    def __init__(self,window):
        self.window = window
        self.color = (150, 150, 150)
        self.missile_color = (255, 0, 0)
        self.block_size = 31
        self.position_x = 350-self.block_size  # starting postion x
        self.position_y = 800-self.block_size  # starting postion y

        self.ship_rect = pygame.draw.rect(self.window, self.color, [self.position_x, self.position_y, self.block_size, self.block_size])

    def update(self):
        self.ship_rect = pygame.draw.rect(self.window, self.color, [self.position_x, self.position_y, self.block_size, self.block_size])
        self.window.blit(Ship.myimage, self.ship_rect)
        for i in Missiles.Missile.missile_list:
            i.update()

    def movement(self):  # przekazujemy tutaj paramtery event z listy pygame.event
        keys = pygame.key.get_pressed()  # checking pressed keys
        if 0 < self.position_x < 671:
            if keys[pygame.K_LEFT]:
                self.position_x -= 1
            if keys[pygame.K_RIGHT]:
                self.position_x += 1
        if self.position_x == 0:
            if keys[pygame.K_RIGHT]:
                self.position_x += 1
        if self.position_x == 671:
            if keys[pygame.K_LEFT]:
                self.position_x -= 1

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            Missiles.Missile(self, self.position_y, 1, self.missile_color)
            #n = 0
            for i in Missiles.Missile.missile_list:
                i.update()
                #n += 1
                #print(n)

