import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap

class Game: 
    def __init__(self):  
        pygame.init()

        pygame.display.set_caption('ninja game')
        #This function will create our window
        #screen is our handle for a window so we can draw onto it
        self.screen = pygame.display.set_mode((640, 480))
        
        #pygame.Surface generates an empty surface
        #we will render on the smaller display and then scale it up to the screen
        self.display = pygame.Surface((320, 240))

        #instantiate a clock object
        self.clock = pygame.time.Clock()
       
        self.movement = [False, False]

        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size = 16)
    
    def run(self):        
        #our game's main loop
        while True:
            #filling the whole screen with a background color to also erase the previous render of the blit images onto the screen
            self.display.fill((14, 219, 248))
           
            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            #prints the tiles that the player is near by
            #print(self.tilemap.tiles_around(self.player.pos))
            #prints the rects
            #print(self.tilemap.physics_rects_around(self.player.pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            #we need to render onto the screen, otherwise we would get a black screen
            #we use the pygame.transform.scale to scale the display to the size of the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0 ))
            pygame.display.update()
            #force our game to run at 60 fps
            self.clock.tick(60)
            
Game().run()