import random


class Object:

    def __init__(self):
        pic = None


class MovingObj(Object):

    def __init__(self):
        pass

    def move(self, string):
        if string == 'w':
            self.y += 1
        if string == 'a':
            self.x -= 1
        if string == 'd':
            self.x += 1
        if string == 's':
            self.y -= 1


class Character(MovingObj):

    def __init__(self):
        x = 9
        y = 9
        points = 0


class StaticObj(Object):

    def __init__(self):
        pass


class Wall(StaticObj):

    def __init__(self):
        pass


class Bonus(StaticObj):

    def __init__(self):
        points = random.randint(1, 5)


class Game:

    def __init__(self):
        map = []

    def create_edges(self, map):

    def update_map(self, new_wall):


