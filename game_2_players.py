import pygame
import random
from logic import *

pygame.init()
random.seed()

FONT1=pygame.font.SysFont("Times New Roman", 80)
FONT2=pygame.font.SysFont("Times New Roman", 50)
FONT3=pygame.font.SysFont("Times New Roman", 60)
FONT4=pygame.font.SysFont("Times New Roman", 100)
FONT5=pygame.font.SysFont("Times New Roman", 20)
FONT6=pygame.font.SysFont("Times New Roman", 25)
FONT7=pygame.font.SysFont("Times New Roman", 18)

equal=lambda x:x

#inicjalizacja plansz do gry

Player_1_list = [[] for i in range(0, 10,1)]
Player_2_list = [[] for i in range(0, 10,1)]

for i in range(0,10,1):
    for j in range(0,10,1):
        Player_1_list[i].append((lambda x:x)(0))
        Player_2_list[i].append((lambda x: x)(0))


#tworzenie planszy gracza 1

def draw_player_1():

    counter = 0  # liczy, ile jest ustawionych statków

    for i in range(0, 10):
        for j in range(0, 10):
            Player_1_list[i][j]=equal(0)

    while counter==0: #ustawianie czteromasztowca
        counter+=1
        x1,y1=random_position(0,9)
        Player_1_list[x1][y1]=equal(1)
        #ustawianie czteromasztowca
        set_4ship(Player_1_list,x1,y1)
        #ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(Player_1_list)

    #ustawianie trójmasztowców
    while counter < 3:
        x2,y2=random_position(0,9)
        o=Neighbour(Player_1_list,x2,y2,1)
        if o.neighbour()==0 and Player_1_list[x2][y2]==0:
            Player_1_list[x2][y2]=equal(1)
            s=Ship_3(Player_1_list,x2,y2,random_direction(x2,y2,2))
            if s.set_ship():
                counter+=1
                #uzupełnienie sąsiadów wartością 2
                put_2(Player_1_list)
            else:
                Player_1_list[x2][y2]=equal(0)
    #ustawianie dwumasztowców
    while counter < 6:
        x3,y3=random_position(0,9)
        o1=Neighbour(Player_1_list,x3,y3,1)
        if o1.neighbour()==0 and Player_1_list[x3][y3]==0:
            Player_1_list[x3][y3]=equal(1)
            s1=Ship_2(Player_1_list,x3,y3,random_direction(x3,y3,1))
            if s1.set_ship():
                counter+=1
                put_2(Player_1_list)
            else:
                Player_1_list[x3][y3]=equal(0)

    #ustawianie jednomasztowców
    while counter <10:
        x4,y4=random_position(0,9)
        o2=Neighbour(Player_1_list,x4,y4,1)
        if o2.neighbour()==0 and Player_1_list[x4][y4]==0:
            Player_1_list[x4][y4]=equal(1)
            counter+=1
            put_2(Player_1_list)


def draw_player_2():
    counter = 0  # liczy, ile jest ustawionych statków

    for i in range(0, 10):
        for j in range(0, 10):
            Player_2_list[i][j] = equal(0)

    while counter == 0:  # ustawianie czteromasztowca
        counter += 1
        x1, y1 = random_position(0, 9)
        Player_2_list[x1][y1] = equal(1)
        # ustawianie czteromasztowca
        set_4ship(Player_2_list, x1, y1)
        # ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(Player_2_list)

    # ustawianie trójmasztowców
    while counter < 3:
        x2, y2 = random_position(0, 9)
        o = Neighbour(Player_2_list, x2, y2, 1)
        if o.neighbour() == 0 and Player_2_list[x2][y2] == 0:
            Player_2_list[x2][y2] = equal(1)
            s = Ship_3(Player_2_list, x2, y2, random_direction(x2, y2, 2))
            if s.set_ship():
                counter += 1
                # uzupełnienie sąsiadów wartością 2
                put_2(Player_2_list)
            else:
                Player_2_list[x2][y2] = equal(0)
    # ustawianie dwumasztowców
    while counter < 6:
        x3, y3 = random_position(0, 9)
        o1 = Neighbour(Player_2_list, x3, y3, 1)
        if o1.neighbour() == 0 and Player_2_list[x3][y3] == 0:
            Player_2_list[x3][y3] = equal(1)
            s1 = Ship_2(Player_2_list, x3, y3, random_direction(x3, y3, 1))
            if s1.set_ship():
                counter += 1
                put_2(Player_2_list)
            else:
                Player_2_list[x3][y3] = equal(0)

    # ustawianie jednomasztowców
    while counter < 10:
        x4, y4 = random_position(0, 9)
        o2 = Neighbour(Player_2_list, x4, y4, 1)
        if o2.neighbour() == 0 and Player_2_list[x4][y4] == 0:
            Player_2_list[x4][y4] = equal(1)
            counter += 1
            put_2(Player_2_list)




def endgame1():

    pygame.mixer.music.stop
    pygame.mixer.music.load('Fanfare.mp3')
    pygame.mixer.music.play(-1)

    while True:
        input(pygame.event.get())
        SCREEN.blit(VICTORY1, (0,0))

        button_main(SCREEN, WIDTH / 8, WIDTH * 3 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, None)
        text("REPLAY", FONT2, WIDTH / 4, HEIGHT * 7 / 8, BLACK)
        button_main(SCREEN, WIDTH * 5 / 8, WIDTH * 7 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, quit)
        text("QUIT", FONT2, WIDTH * 3 / 4, HEIGHT * 7 / 8, BLACK)

        pygame.display.flip()



def endgame2():

    pygame.mixer.music.stop
    pygame.mixer.music.load('Fanfare.mp3')
    pygame.mixer.music.play(-1)

    while True:

        input(pygame.event.get())
        SCREEN.blit(VICTORY2, (0,0))

        button_main(SCREEN, WIDTH / 8, WIDTH * 3 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, None)
        text("REPLAY", FONT2, WIDTH / 4, HEIGHT * 7 / 8, BLACK)
        button_main(SCREEN, WIDTH * 5 / 8, WIDTH * 7 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, quit)
        text("QUIT", FONT2, WIDTH * 3 / 4, HEIGHT * 7 / 8, BLACK)

        pygame.display.flip()




