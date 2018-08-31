import pygame


class Missile:
    missile_list = []
    counter = 0

    def __init__(self, ship, y, direct, color):  #  direct -> kierunek lecących pociskow, albo w gore albo w dol, Y to miejsce z ktorego "wystrzeliwujemy pocisk"
        self.ship = ship
        self.position_x = ship.position_x+15
        self.position_y = y
        self.size = 5
        self.color = color
        self.ID = self.__class__.counter = self.__class__.counter + 1
        self.__class__.missile_list.append(self)
        self.speed = -5 * direct
        pygame.draw.rect(ship.window, self.color, [self.position_x, self.position_y, self.size, self.size])

    def update(self):
        self.move()
        self.list_control()
        for i in Missile.missile_list:
            pygame.draw.rect(i.ship.window, i.color, [i.position_x, i.position_y, i.size, i.size])

    def move(self):
        self.position_y += self.speed

    def list_control(self):
        for i in Missile.missile_list:
            if i.position_y < 0:
                Missile.missile_list.remove(i)
            if i.position_y > 800:
                Missile.missile_list.remove(i)




