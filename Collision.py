import Missiles
import Enemies
import pygame

class Collision:

    def __init__(self, ):
        pass

    def destroy(self):
        for i in Missiles.Missile.missile_list:
            for j in Enemies.Enemies.enemy_list:
                if i.position_y <= j.position_y and j.position_x < i.position_x < j.position_x+j.size and i.speed < 0:
                    Missiles.Missile.missile_list.remove(i)
                    Enemies.Enemies.enemy_list.remove(j)
                    print("DESTROYED")
                    print("MISSSILE : ", i.position_x, " ", i.position_y)
                    print("ENEMY  :  ", j.position_x, " ", j.position_y)

