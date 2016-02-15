import pygame
from pygame import *
import game

# colours
background_colour = "#CC66CC"

# окно
size = (1000, 600)  # ширина и высота

screen = pygame.display.set_mode(size)
pygame.display.set_caption('13FPL LIFE')

bg = Surface(size)
bg.fill(Color(background_colour))


done = False
Blocked = False

game_map = game.Map()
cat = game.Character()
bonus = game.Bonus()
wall = game.Wall()

while not done and not Blocked:

    screen.blit(bg, (0, 0))  # filling screen with colour

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # clicked close
            done = True

        if event.type == pygame.KEYDOWN:
            movement = cat.move(event.key, wall.walls)

            if movement:
                new_wall = wall.wall_generator(movement, [cat.x, cat.y])  # new wall appears
                wall.walls = wall.update_walls(wall.walls, new_wall)  # adding new wall to a map

        for block in wall.walls:   # drawing walls
            screen.blit(wall.pic, (block[0], block[1]))

        if bonus.bonuses:         # drawing bonuses if they exist
            for block in bonus.bonuses:
                screen.blit(bonus.pic, (block[0], block[1]))

        screen.blit(cat.pic, (cat.x, cat.y))  # draw character

        pygame.display.update()
