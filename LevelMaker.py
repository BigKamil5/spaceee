import Enemies
import random

class LevelMaker:

    def __init__(self, window, enemy, n):  #  start_x - jest x pierwszego enemiesea, n jest liczba wrogow w rzedzie
        self.window = window
        self.enemy = enemy
        self.position_y = enemy.position_y
        self.start_x = enemy.position_x
        self.n = n
        for i in range(n):
            self.start_x += 80
            Enemies.Enemies(self.window, self.start_x, self.position_y, self.enemy.move_speed)
