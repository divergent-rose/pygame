import constants
import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state, log_event 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
from background import Background
import sys



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = Background()
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0 #set fps to 60
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = updatable, drawable
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time
        log_state() #log state 
        for event in pygame.event.get(): #this will cycle through pygame events
            if event.type == pygame.QUIT:
                return
        
        #updates game objects 
        updatable.update(dt)
        asteroid_field.update(dt)
        background.update()


        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                #print("Game over!")

                #shows the game over test 
                gameover_font = pygame.font.SysFont(None, 74)
                gameover_text = gameover_font.render("Game Over!", True, (255, 0, 0))
                screen.blit(gameover_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 24))

                #show final score
                final_score_text = gameover_font.render(f"Final Score: {background.score}", True, (255, 255, 255))
                screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 24))
                
                pygame.display.flip()
                pygame.time.delay(3000)  #waits 3 seconds before quitting
                
                sys.exit()
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    #awards points 
                    if asteroid.radius == constants.ASTEROID_MIN_RADIUS:
                        background.score += 100
                    elif asteroid.radius == constants.ASTEROID_MIN_RADIUS *2:
                        background.score += 50
                    else:
                        background.score += 20
                    #splits asteroid
                    asteroid.split()
                    shot.kill()
        
        #draws game objects 
        background.draw(screen)

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()  # Update the full display Surface to the screen

if __name__ == "__main__":
    main()