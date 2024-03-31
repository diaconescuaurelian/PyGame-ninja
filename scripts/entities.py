import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        #the list function will convert any iterable into a list
        self.pos = list(pos)
        self.size = list(size)
        self.velocity = [0, 0]

    def rect(self):
        #we're using the position as the top left of the entity
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap,  movement = (0, 0)):
        #we are creating a vector that represents how much the entity should be moved in this frame
        #based on how much we want to force it to move in this particular frame
        # plus however much there already is in velocity
        frame_movement = (
            movement[0] + self.velocity[0], 
            movement[1] + self.velocity[1],
        )

        self.pos[0] += frame_movement[0]

        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                #when moving right
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                #when moving left
                if frame_movement[0] < 0: 
                    #we set the left side of the entity to the right side of the tile
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]

        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0: 
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1) #velocity will not be > 
    
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)