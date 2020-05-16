import pygame
import random

pygame.init()
random.seed()

FONT1=pygame.font.SysFont("Times New Roman", 80)
FONT2=pygame.font.SysFont("Times New Roman", 50)
FONT3=pygame.font.SysFont("Times New Roman", 60)
FONT4=pygame.font.SysFont("Times New Roman", 100)
FONT5=pygame.font.SysFont("Times New Roman", 20)
FONT6=pygame.font.SysFont("Times New Roman", 25)
FONT7=pygame.font.SysFont("Times New Roman", 18)

#inicjalizacja plansz do gry

Player_1_list = [[] for i in range(0, 10,1)]
Player_2_list = [[] for i in range(0, 10,1)]

for i in range(0,10,1):
    for j in range(0,10,1):
        Player_1_list[i].append((lambda x:x)(0))
        Player_2_list[i].append((lambda x: x)(0))


print(Player_1_list)
print(Player_2_list)