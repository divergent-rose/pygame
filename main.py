import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0 #set fps to 60
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        log_state() #log state 
        for event in pygame.event.get(): #this will cycle through pygame events
            if event.type == pygame.QUIT:
                return
        screen.fill("black") #backround in black
        player.draw(screen)
        pygame.display.flip() #screen refresh 
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time

if __name__ == "__main__":
    main()