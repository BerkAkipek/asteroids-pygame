import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            first_rotation = self.velocity.rotate(rand_angle)
            second_rotation = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position[0], self.position[1], new_radius)
            first.velocity = first_rotation * 1.2
            second = Asteroid(self.position, self.position[1], new_radius)
            second.velocity = second_rotation * 1.2
