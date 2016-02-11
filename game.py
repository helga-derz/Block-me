import random
import pygame

size = 20


class Object:

    def __init__(self):
        pass

    def open_image(self, name, size=20):
        image = pygame.image.load("image/" + name)
        return pygame.transform.scale(image, (20, 20))


class Character(Object):

    def __init__(self):
        self.x = 490
        self.y = 290
        self.points = 0
        self.pic = self.open_image('cat.jpg')

    def move(self, key):
        if key == pygame.K_LEFT:
            self.x -= 20
        if key == pygame.K_RIGHT:
            self.x += 20
        if key == pygame.K_DOWN:
            self.y += 20
        if key == pygame.K_UP:
            self.y -= 20


class Wall(Object):

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


class Bonus(Object):

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
