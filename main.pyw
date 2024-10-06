# 引用
import pygame as pg
from pygame.locals import *

import random as r

# 初始化
pg.init()

# 定义
s_color = 0, 170, 250
b_color = 0, 0, 0
t_color = 255, 255, 255
m_color = 60, 200, 160
l_color = 100, 100, 100
h_color = 10, 80, 200

correct = pg.mixer.Sound('correct.wav')
wrong = pg.mixer.Sound('wrong.wav')
button = pg.mixer.Sound('button.wav')
correct.set_volume(0.3)
wrong.set_volume(0.3)
button.set_volume(0.05)

font = pg.font.SysFont('微软雅黑', 48)
bg = pg.Surface((300 + 150, 600))
bg.fill(b_color)
tmp = font.render('A - Left', True, l_color)
bg.blit(tmp, ((300 - tmp.get_rect().width) // 2, 150 + 50))
tmp = font.render('D - Right', True, l_color)
bg.blit(tmp, ((300 - tmp.get_rect().width) // 2, 200 + 50))
tmp = font.render('W - Turn', True, l_color)
bg.blit(tmp, ((300 - tmp.get_rect().width) // 2, 250 + 50))
tmp = font.render('S - Quicken', True, l_color)
bg.blit(tmp, ((300 - tmp.get_rect().width) // 2, 300 + 50))
pg.draw.rect(bg, h_color, (300, 0, 150, 600))
tmp = font.render('NEXT:', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 20))
tmp = font.render('SCORE:', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 50 + 15 + 150))
tmp = font.render('Coded', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 350 + 40))
tmp = font.render('By:', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 390 + 40))
tmp = font.render('SYZ', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 430 + 40))
tmp = font.render('With:', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 470 + 40))
tmp = font.render('Python', True, t_color)
bg.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 510 + 40))

class Single:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def blit(self, screen, color = s_color):
        pg.draw.rect(screen, color, (self.x * 30 + 1, \
                                       self.y * 30 + 1, 28, 28))

'''
##
## - 1

#
### - 2

##
#
# -3

###
  # - 4

 #
 #
## - 5

  #
### - 6

#
#
## - 7

###
# - 8

##
 #
 # - 9

 #
### - 10

#
##
# - 11

###
 # - 12

 #
##
 # - 13

#### - 14

#
#
#
# - 15

##
 ## - 16

 #
##
# - 17

 ##
## - 18

#
##
 # - 19

# #
 #
# # - 20

# - 21

 #
# # - 22

#
 #
# - 23

# #
 # - 24

 #
#
 # -25
'''
class S:
    def move(self, d = 2):
        if d == 2:
            self.y += 1
            self.for_unmove = 8
        elif d == 8:
            self.y -= 1
            self.for_unmove = 2
        elif d == 4:
            self.x -= 1
            self.for_unmove = 6
        elif d == 6:
            self.x += 1
            self.for_unmove = 4
    def unmove(self):
        self.move(self.for_unmove)
    def blit(self, screen, color = m_color):
        for each in self.get_group():
            each.blit(screen, color)
    def get_next(self):
        button.play()
        tmp = eval('S' + str(self._next))()
        tmp.x, tmp.y = self.x, self.y
        return tmp
class S1(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 1
    def get_group(self):
        g = set()
        for j in range(2):
            for k in range(2):
                g.add(Single(self.x + j, self.y + k))
        return g
class S2(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 3
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 1), (1, 1), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S3(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 4
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (0, 1), (0, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S4(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 5
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (2, 0), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S5(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 2
    def get_group(self):
        g = set()
        tmp = (1, 0), (1, 1), (0, 2), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S6(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 7
    def get_group(self):
        g = set()
        tmp = (2, 0), (0, 1), (1, 1), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S7(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 8
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 1), (0, 2), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S8(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 9
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (2, 0), (0, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S9(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 6
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (1, 1), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S10(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 11
    def get_group(self):
        g = set()
        tmp = (1, 0), (0, 1), (1, 1), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S11(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 12
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 1), (1, 1), (0, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S12(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 13
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (2, 0), (1, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S13(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 10
    def get_group(self):
        g = set()
        tmp = (1, 0), (0, 1), (1, 1), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S14(S):
    def __init__(self):
        self.x, self.y = 3, -1
        self._next = 15
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (2, 0), (3, 0)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S15(S):
    def __init__(self):
        self.x, self.y = 4, -4
        self._next = 14
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 1), (0, 2), (0, 3)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S16(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 17
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 0), (1, 1), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S17(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 16
    def get_group(self):
        g = set()
        tmp = (1, 0), (0, 1), (1, 1), (0, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S18(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 19
    def get_group(self):
        g = set()
        tmp = (1, 0), (2, 0), (0, 1), (1, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S19(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 18
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 1), (1, 1), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S20(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 20
    def get_group(self):
        g = set()
        tmp = (0, 0), (0, 2), (1, 1), (2, 0), (2, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S21(S):
    def __init__(self):
        self.x, self.y = 4, -1
        self._next = 21
    def get_group(self):
        return {Single(self.x, self.y)}
class S22(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 23
    def get_group(self):
        g = set()
        tmp = (1, 0), (0, 1), (2, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S23(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 24
    def get_group(self):
        g = set()
        tmp = (0, 0), (1, 1), (0, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S24(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 25
    def get_group(self):
        g = set()
        tmp = (0, 0), (2, 0), (1, 1)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S25(S):
    def __init__(self):
        self.x, self.y = 4, -3
        self._next = 22
    def get_group(self):
        g = set()
        tmp = (1, 0), (0, 1), (1, 2)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S26(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 27
    def get_group(self):
        g = set()
        tmp = (1, 1), (0, 1), (1, 0)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S27(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 28
    def get_group(self):
        g = set()
        tmp = (1, 1), (0, 1), (0, 0)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S28(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 29
    def get_group(self):
        g = set()
        tmp = (0, 1), (1, 0), (0, 0)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
class S29(S):
    def __init__(self):
        self.x, self.y = 4, -2
        self._next = 26
    def get_group(self):
        g = set()
        tmp = (1, 1), (1, 0), (0, 0)
        for j, k in tmp:
            g.add(Single(self.x + j, self.y + k))
        return g
ls = S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, \
     S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, \
     S21, S22, S23, S24, S25, S26, S27, S28, S29, S1

# 主函数
def main():
    # 定义
    screen = pg.display.set_mode((450, 600))
    pg.display.set_caption('俄罗斯方块')

    s_ing = r.choice(ls)()
    s_ready = r.choice(ls)
    s_alr = set()
    score = 0

    key_state = False

    i = 0
    clock = pg.time.Clock()
    running = True

    def check_if_next():
        for each in s_ing.get_group():
            if each.y >= 20:
                return True
            for each1 in s_alr:
                if each.x == each1.x and each.y == each1.y:
                    return True
        return False
    def check_if_move():
        for each in s_ing.get_group():
            if each.x < 0 or each.x >= 10:
                return False
        if check_if_next():
            return False
        return True
    def check_if_full():
        nonlocal s_alr
        nonlocal score
        f = False
        delta_score = 100
        tmp = {i:set() for i in range(-10, 20)}
        for each in s_alr:
            tmp[each.y].add(each)
        for each in tmp:
            if len(tmp[each]) == 10:
                f = True
                s_alr -= tmp[each]
                score += delta_score
                delta_score += 50
                for each1 in tmp:
                    if each1 < each:
                        for each2 in tmp[each1]:
                            each2.y += 1
        if(f):
            correct.play()

    # 循环
    while running:
        # 处理事件
        for each in pg.event.get():
            if each.type == QUIT:
                return False

            if each.type == KEYDOWN:
                key_state = each.key, 0
            if each.type == KEYUP:
                key_state = False

        if key_state != False:
            if not(key_state[1] % 30):
                if key_state[0] in (K_w, K_UP):
                    s_ing = s_ing.get_next()
                    for each in range(10):
                        if check_if_move():
                            break
                        s_ing.move(4)
                    else:
                        for each in range(10):
                            s_ing.move(6)
                        for each in range(10):
                            if check_if_move():
                                break
                            s_ing.move(8)
                        else:
                            for each in range(10):
                                s_ing.move(2)
                            s_ing = s_ing.get_next().get_next().get_next()
            
            if not(key_state[1] % 10):
                if key_state[0] in (K_a, K_LEFT):
                    s_ing.move(4)
                elif key_state[0] in (K_d, K_RIGHT):
                    s_ing.move(6)
                if not check_if_move():
                    s_ing.unmove()
                else:
                    button.play()

            if not(key_state[1] % 5):
                if key_state[0] in (K_s, K_DOWN):
                    s_ing.move()
                    if check_if_next():
                        s_ing.unmove()
                        for each in s_ing.get_group():
                            s_alr.add(each)
                        s_ing = s_ready()
                        s_ready = r.choice(ls)
                        check_if_full()
                    else:
                        button.play()
            
            key_state = key_state[0], key_state[1] + 1

        if not(i % 30):
            s_ing.move()
            if check_if_next():
                s_ing.unmove()
                for each in s_ing.get_group():
                    s_alr.add(each)
                s_ing = s_ready()
                s_ready =r.choice(ls)
                check_if_full()

        # 绘制
        screen.blit(bg, (0, 0))
        
        for each in s_alr|{s_ing}:
            each.blit(screen)
        
        for each in s_ready().get_group():
            pg.draw.rect(screen, t_color, (each.x * 15 + 1 + 300, \
                                           (each.y + \
                    max(abs(each1.y) for each1 in s_ready().get_group()) + 1\
                                            ) * 15 + 1 + 50, 13, 13))
        tmp = font.render(str(score), True, t_color)
        screen.blit(tmp, (300 + (150 - tmp.get_rect().width) // 2, 215 + 40))
        
        # 收尾工作
        pg.display.flip()
        clock.tick(60)
        i += 1

        for each in s_alr:
            if each.y < 0:
                running = False
                break

    # 游戏结束
    wrong.play()
    screen.fill(b_color)
    b_font = pg.font.SysFont('微软雅黑', 72)
    tmp = b_font.render('G A M E   O V E R', True, t_color)
    screen.blit(tmp, ((450 - tmp.get_rect().width) // 2, 130))
    tmp = font.render('YOUR SCORE:', True, t_color)
    screen.blit(tmp, ((450 - tmp.get_rect().width) // 2, 230))
    tmp = b_font.render(str(score), True, t_color)
    screen.blit(tmp, ((450 - tmp.get_rect().width) // 2, 280))
    pg.draw.rect(screen, t_color, (40, 380, 160, 50))
    pg.draw.rect(screen, t_color, (250, 380, 160, 50), 1)
    tmp = font.render('AGAIN(A)', True, b_color)
    screen.blit(tmp, ((160 - tmp.get_rect().width) // 2 + 40, \
                      (50 - tmp.get_rect().height) // 2 + 380))
    tmp = font.render('QUIT(Q)', True, t_color)
    screen.blit(tmp, ((160 - tmp.get_rect().width) // 2 + 250, \
                      (50 - tmp.get_rect().height) // 2 + 380))
    tmp = font.render('Coded By SYZ With Python', True, t_color)
    screen.blit(tmp, (450 - tmp.get_rect().width, 600 - tmp.get_rect().height))
    pg.display.flip()

    while True:
        for each in pg.event.get():
            if each.type == QUIT:
                return False
            if each.type == MOUSEBUTTONUP:
                if each.pos[1] in range(380, 430):
                    if each.pos[0] in range(40, 200):
                        return True
                    elif each.pos[0] in range(250, 410):
                        return False
            if each.type == KEYUP:
                if each.key == K_a:
                    return True
                elif each.key == K_q:
                    return False

# 主线
if __name__ == '__main__':
    while main():
        pass
    pg.quit()
