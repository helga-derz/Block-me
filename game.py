import random
import pygame

size = 20


class Object:

    def __init__(self):
        self.size = 20

    def open_image(self, name):
        image = pygame.image.load("image/" + name)
        return pygame.transform.scale(image, (20, 20))


class Character(Object):

    def __init__(self):
        self.x = 480
        self.y = 280
        self.points = 0
        self.pic = self.open_image('cat.jpg')

    def move(self, key, walls):   # returning movement, changing coordinates
        # go left
        if key == pygame.K_LEFT:
            if [self.x-20, self.y] not in walls:
                self.x -= 20
                return 'l'

        # go right
        if key == pygame.K_RIGHT:
            if [self.x+20, self.y] not in walls:
                self.x += 20
                return 'r'

        # go down
        if key == pygame.K_DOWN:
            if [self.x, self.y+20] not in walls:
                self.y += 20
                return 'd'

        # go up
        if key == pygame.K_UP:
            if [self.x, self.y-20] not in walls:
                self.y -= 20
                return 'u'


class Wall(Object):

    def __init__(self):
        self.pic = self.open_image('wall.jpeg')
        self.walls = self.create_edges()

    def create_edges(self):  # creating frame of walls

        walls = []

        for x in range(0, 1000, size):
            walls.append([x, 0])
            walls.append([x, 580])

        for y in range(20, 580, size):
            walls.append([0, y])
            walls.append([980, y])

        return walls

    def update_walls(self, walls=[], new_wall=[]):  # adding new wall if exists

        if new_wall:
            walls.append(new_wall)

        return walls

    def wall_generator(self, movement, char_coord):  # building new wall in front of character

        if movement == 'l':
            new_wall = [char_coord[0] - 20, char_coord[1]]
        if movement == 'r':
            new_wall = [char_coord[0] + 20, char_coord[1]]
        if movement == 'u':
            new_wall = [char_coord[0], char_coord[1] - 20]
        if movement == 'd':
            new_wall = [char_coord[0], char_coord[1] + 20]

        return new_wall


class Bonus(Object):

    def __init__(self):
        self.points = random.randint(1, 5)
        self.pic = self.open_image('bonus.png')

    def update_bonuses(self, bonuses=[], new_bonus=[]):   # adding new bonus if exists

        if new_bonus:
            bonuses.append(new_bonus)

        return bonuses

    def del_bonus(self, bonuses, eaten_bonus):  # deleting eaten bonus
        return bonuses.remove(eaten_bonus)


class Game:
    pass

