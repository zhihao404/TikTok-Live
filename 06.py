import pygame
import random

WIDTH = 800
HEIGHT = 600
BALL_SIZE_WHITE = 20
BALL_SIZE_BLUE = 50
BALL_COLOR_WHITE = (255, 255, 255)
BALL_COLOR_BLUE = (0, 0, 255)
FRAME_COLOR = (0, 0, 0)
HIT_COLOR = (255, 0, 0)
BALL_SPEED_WHITE = 5
BALL_SPEED_BLUE = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, color, speed, ball_size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.speed_x = random.uniform(-speed, speed)
        self.speed_y = random.uniform(-speed, speed)
        self.ball_size = ball_size

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < self.ball_size or self.x > WIDTH - self.ball_size:
            self.speed_x = -self.speed_x
        if self.y < self.ball_size or self.y > HEIGHT - self.ball_size:
            self.speed_y = -self.speed_y

    # Move the blue ball horizontally across the screen's midline
        if self.color == BALL_COLOR_BLUE:
            self.x = WIDTH/ 2

    def check_collision(self, ball):
        return ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5 <= self.ball_size 
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.ball_size)

white_ball = Ball(WIDTH / 2, HEIGHT / 2, BALL_COLOR_WHITE, BALL_SPEED_WHITE, BALL_SIZE_WHITE)
blue_ball = Ball(WIDTH / 4, HEIGHT / 4, BALL_COLOR_BLUE, BALL_SPEED_BLUE, BALL_SIZE_BLUE)
balls = [white_ball, blue_ball]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            white_ball = Ball(x, y, BALL_COLOR_WHITE, BALL_SPEED_WHITE, BALL_SIZE_WHITE)
            balls.append(white_ball)

    screen.fill(FRAME_COLOR)#Ballが繋がらないようにしている

    for ball in balls.copy():
        ball.update()
        ball.draw(screen)
        if ball.check_collision(blue_ball):
            if ball == white_ball:
                balls.remove(white_ball)

    for ball in balls:
        ball.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

