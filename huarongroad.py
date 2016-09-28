# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

__module_name__ = 'HuaRongRoad'
__module_description__ = 'A HuaRongRoad written in python'
__version__ = (1, 0, 0)
#屏幕大小
WIDTD_LENGTH = 320
HEIGHT_LENGTH = 480
cur_screen = [1]#1=main menu 2=game 3=rank 4=about
                    
def set_icon(iconname):
    
    icon=pygame.Surface((48,48))
    icon.set_colorkey((0,0,0))
    rawicon=pygame.image.load(iconname)#48x48
    for i in range(0,48):
        for j in range(0,48):
            icon.set_at((i,j), rawicon.get_at((i,j)))
    pygame.display.set_icon(icon)#set

#初始化
pygame.init()
#界面大小
screen = pygame.display.set_mode((WIDTD_LENGTH, HEIGHT_LENGTH))
#设置icon
set_icon('src/icon.png')
#标题
pygame.display.set_caption('华容道  ByZWD') 

menu_bg = pygame.image.load('src/menu_bg.png').convert()
b_start_nor = pygame.image.load('src/b_start_nor.png')
b_start_sele = pygame.image.load('src/b_start_sele.png')
b_rank_nor = pygame.image.load('src/b_rank_nor.png')
b_rank_sele = pygame.image.load('src/b_rank_sele.png')
b_about_nor = pygame.image.load('src/b_about_nor.png')
b_about_sele = pygame.image.load('src/b_about_sele.png')
rank_bg = pygame.image.load('src/rank_bg.png')
about_png = pygame.image.load('src/about.png')
main_bg0 = pygame.image.load('src/main_bg0.png')
level_00 = pygame.image.load('src/level_00.png')
caocao = pygame.image.load('src/p_00_0.png')
zhaoyun_s = pygame.image.load('src/p_01_0.png')
zhaoyun_h = pygame.image.load('src/p_02_0.png')
huangzhong_s = pygame.image.load('src/p_03_0.png')
huangzhong_h = pygame.image.load('src/p_04_0.png')
zhangfei_s = pygame.image.load('src/p_05_0.png')
zhangfei_h = pygame.image.load('src/p_06_0.png')
machao_s = pygame.image.load('src/p_07_0.png')
machao_h = pygame.image.load('src/p_08_0.png')
guanyu_s = pygame.image.load('src/p_09_0.png')
guanyu_h = pygame.image.load('src/p_10_0.png')
soldier_1 = pygame.image.load('src/p_11_0.png')
soldier_2 = pygame.image.load('src/p_11_0.png')
soldier_3 = pygame.image.load('src/p_11_0.png')
soldier_4 = pygame.image.load('src/p_11_0.png')

#第一关初始化
def level1_init():
    screen.blit(level_00, (95, 0))
    screen.blit(caocao, (85, 52))
    screen.blit(huangzhong_s, (10, 52))
    screen.blit(machao_s, (10, 202))
    screen.blit(zhaoyun_s, (235,52))
    screen.blit(zhangfei_s, (235,202))
    screen.blit(guanyu_h, (85,202))
    screen.blit(soldier_1, (10,352))
    screen.blit(soldier_2, (235,352))
    screen.blit(soldier_3, (85,277))
    screen.blit(soldier_4, (160,277))
    
def start_menu():
    cur_screen[0] = 1
    screen.blit(menu_bg, (0, 0))
    screen.blit(b_start_nor, (103, 325))
    screen.blit(b_rank_nor, (100, 355))
    screen.blit(b_about_nor, (101, 385))
def start_sele():
    screen.blit(b_start_sele, (103, 325))
def rank_sele():
    screen.blit(b_rank_sele, (100, 355))
def about_sele():
    screen.blit(b_about_sele, (101, 385))
def start_game():
    cur_screen[0] = 2
    screen.blit(main_bg0, (0, 0))
    level1_init()
def rank():
    cur_screen[0] = 3
    screen.blit(rank_bg, (0, 0))
def about():
    cur_screen[0] = 4
    screen.blit(about_png, (0, 0))
    
#鼠标监听
def mouse_move(mouse_x, mouse_y):
    if cur_screen[0] == 1:
        if mouse_x in range(100,206):
            if mouse_y in range(325,353):
                start_sele()
            elif mouse_y in range(355,382):
                rank_sele()
            elif mouse_y in range(385,413):
                about_sele()
            else:
                start_menu()
    elif cur_screen[0] == 2:
        pass
    elif cur_screen[0] == 3:
        pass
    elif cur_screen[0] == 4:
        pass

def mouse_action(mouse_down_x, mouse_down_y):
    if cur_screen[0] == 1:
        if mouse_down_x in range(100,206):
            if mouse_down_y in range(325,353):
                start_game()
            elif mouse_down_y in range(355,382):
                rank()
            elif mouse_down_y in range(385,413):
                about()
    elif cur_screen[0] == 2:
        if mouse_down_x in range(10,310) and mouse_down_y in range(52,427):
            pass
    elif cur_screen[0] == 3:
        if mouse_down_x in range(260,320) and mouse_down_y in range(432,480):
            start_menu()
    elif cur_screen[0] == 4:
        if mouse_down_x in range(260,320) and mouse_down_y in range(432,480):
            start_menu()
# 游戏循环帧率设置
clock = pygame.time.Clock()

#初始化屏幕
screen.fill(0)
start_menu()

running = True

while running:
    # 控制游戏最大帧率为600
    clock.tick(600)
    #判断
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down_x,mouse_down_y = pygame.mouse.get_pos()
            mouse_action(mouse_down_x, mouse_down_y)
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            mouse_move(mouse_x, mouse_y)
            
    
    
    pygame.display.update()
    
