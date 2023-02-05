import pygame
import random

WIDTH = 800
HEIGHT = 600
BALL_SIZE_BLUE = 50
BALL_SIZE_WHITE = 20
BALL_COLOR = (255, 255, 255)
BALL_COLOR_2 = (0, 0, 255)
FRAME_COLOR = (0, 0, 0)
HIT_COLOR = (255, 0, 0)
BALL_SPEED = 5
BALL_SPEED_2 = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, color, size, speed):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.speed_x = random.uniform(-speed, speed)
        self.speed_y = random.uniform(-speed, speed)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < self.size or self.x > WIDTH - self.size:
            self.speed_x = -self.speed_x
        if self.y < self.size or self.y > HEIGHT - self.size:
            self.speed_y = -self.speed_y

    # Move the blue ball horizontally across the screen's midline
        if self.color == BALL_COLOR_2:
            self.x = WIDTH/ 2

    def check_collision(self, ball):
        return ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5 <= self.size + 50

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

white_ball = Ball(WIDTH / 2, HEIGHT / 2, BALL_COLOR, BALL_SIZE_WHITE, BALL_SPEED)
blue_ball = Ball(WIDTH / 4, HEIGHT / 4, BALL_COLOR_2, BALL_SIZE_BLUE, BALL_SPEED_2)
balls = [white_ball, blue_ball]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HIT_COLOR, (0, 0, BALL_SIZE_WHITE, HEIGHT), 0)
    pygame.draw.rect(screen, HIT_COLOR, (WIDTH - BALL_SIZE_WHITE, 0, BALL_SIZE_WHITE, HEIGHT), 0)

    for ball in balls.copy():
        ball.update()
        ball.draw(screen)
        if ball.check_collision(blue_ball):
            if ball == white_ball:
                balls.remove(white_ball)

    pygame.display.update()
    clock.tick(60)

pygame.quit()