import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state() #log state 
        for event in pygame.event.get(): #this will cycle through pygame events
            if event.type == pygame.QUIT:
                return
        screen.fill("black") #backround in black
        pygame.display.flip() #screen refresh 

if __name__ == "__main__":
    main()