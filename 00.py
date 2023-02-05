import pygame
import random

# Pygameの初期化
pygame.init()

# 画面の大きさとタイトルの設定
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Bouncing Ball Game")

# 色の定義
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)

# 丸い物体の位置と速度を設定
x = 150
y = 150
speed_x = 1
speed_y = 1

# 画面の描画
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 画面の背景色を白に設定
    screen.fill((0, 0, 0))
    
    # 四角の枠を描画
    pygame.draw.rect(screen, red, (50, 50, 300, 200), 2)
    
    # 赤い部分を描画
    pygame.draw.rect(screen, red, (50, 50, 50, 200))
    pygame.draw.rect(screen, red, (300, 50, 50, 200))
    
    # 丸い物体を描画
    pygame.draw.circle(screen, white, (x, y), 20)
    
    # 丸い物体を四角の枠内で跳ね返す
    x += speed_x
    y += speed_y
    if x > 350 or x < 100:
        speed_x = -speed_x
    if y > 250 or y < 100:
        speed_y = -speed_y
    
    # 赤い部分に当たった場合は丸い物体を消す
    if x > 300 and y > 50 and y < 250:
        running = False
    if x < 100 and y > 50 and y < 250:
        running = False
    
    # 画面の更新
    pygame.display.update()

# Pygameの終了
pygame.quit()
