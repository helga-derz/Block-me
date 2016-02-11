import random
import pygame

size = 20

class Object:

    def __init__(self):
        pass

    def open_image(self, name, size=20):
        image = pygame.image.load("image/" + name)
        return pygame.transform.scale(image, (20, 20))


class MovingObj(Object):

    def __init__(self):
        pass

    def move(self, string):
        if string == 'w':
            self.y += 20
        if string == 'a':
            self.x -= 20
        if string == 'd':
            self.x += 20
        if string == 's':
            self.y -= 20


class Character(MovingObj):

    def __init__(self):
        self.x = 490
        self.y = 290
        self.points = 0
        self.pic = self.open_image('cat.jpg')

#    def update_character(self):


class StaticObj(Object):

    def __init__(self):
        pass


class Wall(StaticObj):

    def __init__(self):
        self.pic = self.open_image('wall.jpeg')

    def create_edges(self):

        walls = []

        for x in range(0, 1000, size):
            walls.append([x, 0])
            walls.append([x, 580])

        for y in range(20, 580, size):
            walls.append([0, y])
            walls.append([980, y])

        return walls

    def update_walls(self, walls=[], new_wall=[]):

        if not walls:
            walls = self.create_edges()

        if new_wall:
            walls.append(new_wall)

        return walls


class Bonus(StaticObj):

    def __init__(self):
        self.points = random.randint(1, 5)
        self.pic = self.open_image('bonus.png')

    def update_bonuses(self, bonuses=[], new_bonus=[]):

        if new_bonus:
            bonuses.append(new_bonus)

        return bonuses

    def del_bonus(self, bonuses, eaten_bonus):
        return bonuses.remove(eaten_bonus)


class Game:
    pass
