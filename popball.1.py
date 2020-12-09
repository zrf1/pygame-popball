# -*- coding: utf-8 -*-
'''
1、游戏基本框架：初始化，加载资源，主循环，退出事件
2、实现游戏流程：开始，游戏，失败
'''

import pygame, os               # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
from sys import exit            # 导入sys库中的exit函数

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

# 游戏状态：0 开始，1 游戏，2 失败
state_index = 0

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

    # 绘制背景
    if state_index == 0:
        img = start_img
    elif state_index == 2:
        img = fail_img
    else:
        img = back_img
    screen.blit(img, (0, 0))   # 绘制背景

    # 更新屏幕
    pygame.display.update()     # 更新屏幕
