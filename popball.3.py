# -*- coding: utf-8 -*-
'''
1、创建档板精灵
2、模拟档板反弹（碰撞检测）
'''

import pygame, os               # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
from sys import exit            # 导入sys库中的exit函数
from random import randint, choice

# 定义窗口的分辨率
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 600
FRAME_RATE = 60                 # 定义画面帧率
clock = pygame.time.Clock()

# 初始化
pygame.init()                                                       # 初始化pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 70)             # 设定窗口打开的位置
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # 初始化窗口
pygame.display.set_caption('弹球小游戏')                            # 设置窗口标题

start_img = pygame.image.load('res/start.gif')                      # 开始图
back_img = pygame.image.load('res/back.gif')                        # 背景图
fail_img = pygame.image.load('res/fail.gif')                        # 失败图
ball_img = pygame.image.load('res/ball.png')                        # 小球图
board_img = pygame.image.load('res/board.png')                      # 档板图

# 游戏状态：0 开始，1 游戏，2 失败
state_index = 0


##############################################################


class Ball(pygame.sprite.Sprite):
    '小球精灵'

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [(SCREEN_WIDTH - self.rect.width)/2,
                             (SCREEN_HEIGHT - self.rect.height)/2]
        self.dx = randint(3, 6) * choice([1, -1])
        self.dy = randint(3, 9) * choice([1, -1])

    def update(self):
        ''
        x = self.rect.left + self.dx
        y = self.rect.top + self.dy

        if x < 0 or x > SCREEN_WIDTH:
            # 左右边界反弹
            self.dx = -self.dx

        if y < 0:
            # 上边界反弹
            self.dy = -self.dy

        if y > SCREEN_HEIGHT:
            # 超出下沿，失败
            global state_index
            state_index = 2
            self.kill()

        self.rect.left += self.dx
        self.rect.top += self.dy


class Board(pygame.sprite.Sprite):
    '挡板精灵'

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [(SCREEN_WIDTH - self.rect.width)/2,
                             SCREEN_HEIGHT - self.rect.height - 30]
        self.dx = 10

    def update(self):
        x = self.rect.left + self.dx * board_mv
        if x >= 0 and x <= SCREEN_WIDTH - self.rect.width:
            self.rect.left += self.dx * board_mv

    def draw(self, screen):
        screen.blit(self.image, self.rect)

##############################################################


ball = pygame.sprite.Group()
board = Board(board_img)
board_mv = 0

# 事件循环(main loop)
while True:
    clock.tick(FRAME_RATE)      # 控制游戏最大帧率

    # 处理游戏退出,从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state_index in [0, 2]:
                    state_index = 1
                    ball.add(Ball(ball_img))
            elif state_index == 1 and event.key == pygame.K_LEFT:
                board_mv = -1
            elif state_index == 1 and event.key == pygame.K_RIGHT:
                board_mv = 1
        elif state_index == 1 and event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                board_mv = 0

    # 碰撞检测
    ball_list = pygame.sprite.spritecollide(board, ball, False)
    if len(ball_list) > 0:
        for b in ball_list:
            b.dy = -b.dy
            b.rect.top += b.dy

    # 绘制背景
    if state_index == 0:
        img = start_img
    elif state_index == 2:
        img = fail_img
    else:
        img = back_img
    screen.blit(img, (0, 0))    # 绘制背景

    # 更新屏幕
    if state_index == 1:
        ball.update()
        board.update()
        ball.draw(screen)
        board.draw(screen)

    pygame.display.update()     # 更新屏幕
