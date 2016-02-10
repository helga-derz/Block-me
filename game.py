import random

size = 20

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
