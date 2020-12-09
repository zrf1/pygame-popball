# pygame实现

## 第一步

### 游戏基本框架：初始化，主循环，退出事件

1. 初始化

2. 加载资源

3. 主循环：消息队列、更新界面

### 实现游戏流程：开始，游戏，失败


## 第二步

### 创建小球精灵

### 模拟小球反弹

`
class Ball(pygame.sprite.Sprite):
    __init__():
        image
        rect
    update()
        位置
`

`
ball = pygame.sprite.Group()
`


## 第三步

### 创建档板精灵
`
class Board(pygame.sprite.Sprite):
    __init__():
        image
        rect
    update()
        位置
    draw(self, screen):
        screen.blit(self.image, self.rect)
`
### 模拟档板反弹（碰撞检测）

`
ball_list = pygame.sprite.spritecollide(board, ball, False)
`

## 第四步

### 添加计分功能

score_now = 0                   # 当前得分

score_high = 0                  # 最高得分

score_font = pygame.font.Font('res/fangsun.ttf', 20)

t = score_font.render('当前得分：%d' % score_now, True, (224, 224, 224))

r = t.get_rect()

r.topleft = score_now_lefttop

screen.blit(t, r)

### 添加声音效果

pop_sound = pygame.mixer.Sound('res/pop.wav')

pop_sound.set_volume(0.3)

pop_sound.play()

