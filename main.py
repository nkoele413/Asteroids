# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1 > 0:
        screen.fill("black")
        pygame.display.flip()
    #print ("Starting Asteroids!")
    #print (f"Screen width: {SCREEN_WIDTH}")
    #print (f"Screen height: {SCREEN_HEIGHT}")

    

if __name__ == "__main__":
    main()
