import pygame
import random

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Create a ball object
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Check if ball hits the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= 400:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= 300:
            self.speed_y = -self.speed_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create ball object
ball = Ball(200, 150, 20, (255, 255, 255))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update ball position
    ball.update()
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw rectangle frame
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 20, 300), 0)
    pygame.draw.rect(screen, (255, 0, 0), (380, 0, 20, 300), 0)
    pygame.draw.rect(screen, (255, 0, 0), (20, 0, 360, 20), 0)
    pygame.draw.rect(screen, (255, 0, 0), (20, 280, 360, 20), 0)
    
    # Draw ball
    ball.draw(screen)
    
    # Check if ball hits the red walls
    if (ball.x - ball.radius <= 20 and ball.y - ball.radius <= 0) or (ball.x + ball.radius >= 380 and ball.y - ball.radius <= 0) or (ball.x - ball.radius <= 20 and ball.y + ball.radius >= 280) or (ball.x + ball.radius >= 380 and ball.y + ball.radius >= 280):
        running = False
    
    # Update screen
    pygame.display.update()
    clock.tick(60)

# Quit pygame
pygame.quit()
