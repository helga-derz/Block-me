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

# images

wall_image = pygame.image.load("image/wall.jpeg")
wall_image = pygame.transform.scale(wall_image, (20, 20))

cat_image = pygame.image.load("image/cat.jpg")
cat_image = pygame.transform.scale(cat_image, (20, 20))

bonus_image = pygame.image.load("image/bonus.png")
bonus_image = pygame.transform.scale(bonus_image, (20, 20))


done = False
Blocked = False

while not done and not Blocked:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # clicked close
            done = True

    screen.blit(bg, (0, 0))  # filling screen with colour
    pygame.display.update()
