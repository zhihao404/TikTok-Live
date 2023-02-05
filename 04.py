import pygame
import random

WIDTH = 800
HEIGHT = 600
BALL_SIZE = 20
BLUE_BALL_SIZE = 100
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
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.speed_x = random.uniform(-speed, speed)
        self.speed_y = random.uniform(-speed, speed)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < BALL_SIZE or self.x > WIDTH - BALL_SIZE:
            self.speed_x = -self.speed_x
        if self.y < BALL_SIZE or self.y > HEIGHT - BALL_SIZE:
            self.speed_y = -self.speed_y

    # Move the blue ball horizontally across the screen's midline
        if self.color == BALL_COLOR_2:
            self.x = WIDTH/ 2

    def check_collision(self, ball):
        return ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5 <= BALL_SIZE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BLUE_BALL_SIZE)

blue_ball = Ball(WIDTH / 4, HEIGHT / 4, BALL_COLOR_2, BALL_SPEED_2)
balls = [blue_ball]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            balls.append(Ball(x, y, BALL_COLOR, BALL_SPEED))

    screen.fill(FRAME_COLOR)#両端の赤い壁のサイズ
    pygame.draw.rect(screen, HIT_COLOR, (0, 0, BALL_SIZE, HEIGHT), 0)
    pygame.draw.rect(screen, HIT_COLOR, (WIDTH - BALL_SIZE, 0, BALL_SIZE, HEIGHT), 0)

    for ball in balls.copy():
        ball.update()
        ball.draw(screen)
        if ball.check_collision(blue_ball):
            if ball != blue_ball:
                balls.remove(ball)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
