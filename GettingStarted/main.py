# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
pygame.init()

screen = pygame.display.set_mode((100,100),0,32)
pygame.display.set_caption("Hello pygame")
screen.fill((0,0,0))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()















