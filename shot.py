from circleshape import CircleShape
from constants import * 
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,player_direction):
        super().__init__(x,y,SHOT_RADIUS)
        self.forward = pygame.Vector2(0,1).rotate(player_direction)


    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.forward * PLAYER_SPEED * dt)

