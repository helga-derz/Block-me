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

wall = game.Wall()
cat = game.Character()

while not done and not Blocked:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # clicked close
            done = True

        if event.type == pygame.KEYDOWN:
            cat.move(event.key, wall.update_walls()) # here should be map

    screen.blit(bg, (0, 0))  # filling screen with colour

    for x, y in wall.update_walls():
        screen.blit(wall.pic, (x, y))

    screen.blit(cat.pic, (cat.x, cat.y))  # draw character

    pygame.display.update()
