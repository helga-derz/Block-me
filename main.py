import pygame
from pygame import *
import game
import time

pygame.init()

# colours
background_colour = "#CC66CC"
font_colour = (0, 0, 0)

# окно
size = (1000, 620)  # ширина и высота

screen = pygame.display.set_mode(size)
pygame.display.set_caption('13FPL LIFE')

my_font = pygame.font.SysFont("monospace", 20, bold=True)

bg = Surface(size)
bg.fill(Color(background_colour))

done = False

game_map = game.Map()
KEYS_OF_MOVEMENT = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

while not done and not game_map.Blocked and not game_map.Map_Full:

    screen.blit(bg, (0, 0))  # filling screen with colour

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # clicked close
            done = True

        if event.type == pygame.KEYDOWN and event.key in KEYS_OF_MOVEMENT:
            movement = game_map.cat.move(event.key, game_map.wall.walls)

            game_map.update_map()

        for block in game_map.wall.walls:  # drawing walls
            screen.blit(game_map.wall.pic, block)

        if game_map.bonus.bonuses:  # drawing bonuses if they exist
            for block in game_map.bonus.bonuses:
                screen.blit(game_map.bonus.pic, block)

        screen.blit(game_map.cat.pic, (game_map.cat.x, game_map.cat.y))  # draw character

        score_string = "SCORE:{0}".format(game_map.cat.points)
        score_label = my_font.render(score_string, 1, font_colour)
        screen.blit(score_label, (450, 600))

        pygame.display.update()

if game_map.Blocked:
    time.sleep(3)

print("score:", game_map.cat.points)

pygame.quit()
