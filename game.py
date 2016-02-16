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
        self.pic = self.open_image('cat.png')

    def move(self, key, walls):   # returning movement, changing coordinates
        # go left
        if key == pygame.K_LEFT:
            if (self.x-20, self.y) not in walls:
                self.x -= 20

        # go right
        if key == pygame.K_RIGHT:
            if (self.x+20, self.y) not in walls:
                self.x += 20

        # go down
        if key == pygame.K_DOWN:
            if (self.x, self.y+20) not in walls:
                self.y += 20

        # go up
        if key == pygame.K_UP:
            if (self.x, self.y-20) not in walls:
                self.y -= 20


class Wall(Object):

    def __init__(self):
        self.pic = self.open_image('wall.jpeg')
        self.walls = self.create_edges()

    def create_edges(self):  # creating frame of walls

        walls = []

        for x in range(0, 1000, size):
            walls.append((x, 0))
            walls.append((x, 580))

        for y in range(20, 580, size):
            walls.append((0, y))
            walls.append((980, y))

        return walls

    def add_wall(self, free_space):
        self.walls.append(random.choice(free_space))


class Bonus(Object):

    def __init__(self):
        self.bonuses = []
        self.points = 1
        self.pic = self.open_image('bonus.png')

    def add_bonus(self, free_space):
        self.bonuses.append(random.choice(free_space))

    def del_bonus(self, eaten_bonus):  # deleting eaten bonus
        self.bonuses.remove(eaten_bonus)


class Map:

    def __init__(self):
        self.Map_Full = False
        self.game_map = self.clear_map()
        self.wall = Wall()
        self.bonus = Bonus()
        self.cat = Character()
        self.Blocked = False

    def clear_map(self):
        game_map = {}
        for x in range(0, 1000, size):
            for y in range(0, 600, size):
                game_map[(x, y)] = 0

        return game_map

    def update_map(self):

        # checking if cat eats a bonus
        # if yes - get points of the bonus and then delete it
        if (self.cat.x, self.cat.y) in self.bonus.bonuses:
            self.cat.points += self.bonus.points
            self.bonus.del_bonus((self.cat.x, self.cat.y))

        # searching for some space on the map
        free_space = self.where_free_space()

        if not free_space:
            self.Map_Full = True

        if not self.Map_Full:
            # choose what goes next - bonus or wall
            if self.choose_block() == 'wall':
                self.wall.add_wall(free_space)
            else:
                self.bonus.add_bonus(free_space)

            # cleaning a map
            self.game_map = self.clear_map()

            # fill the map with walls
            for wall in self.wall.walls:
                self.game_map[wall] = 'wall'

            # fill the map with bonuses
            if self.bonus.bonuses:
                for bonus in self.bonus.bonuses:
                    self.game_map[bonus] = 'bonus'

            # fill the map with the character
            self.game_map[(self.cat.x, self.cat.y)] = 'cat'

            self.check_if_blocked()

    def choose_block(self):
        if random.randint(1, 2) == 1:
            return 'wall'
        else:
            return 'bonus'

    def where_free_space(self):

        free_space = []

        for coord, block in self.game_map.items():
            if block == 0:
                free_space.append(coord)

        return free_space

    def check_if_blocked(self):

        left = (self.cat.x-20, self.cat.y)
        right = (self.cat.x+20, self.cat.y)
        down = (self.cat.x, self.cat.y+20)
        up = (self.cat.x, self.cat.y-20)

        if left in self.wall.walls and right in self.wall.walls and up in self.wall.walls and down in self.wall.walls:
            self.Blocked = True
