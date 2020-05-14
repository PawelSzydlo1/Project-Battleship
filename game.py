import pygame
from constant import *
from logic import *

pygame.init()
random.seed()

FONT1=pygame.font.SysFont("Times New Roman", 80)
FONT2=pygame.font.SysFont("Times New Roman", 50)

#inicjowanie planszy komputera
AI_list=[[] for i in range(0,10,1)]
#inicjowanie planszy gracza
Player_list=[[] for i in range (0,10,1)]
for i in range(0,10):
    for j in range(0,10):
        Player_list[i].append(0)
        AI_list[i].append(0)



#wypełnienie planszy gracza

def draw_player():
    #counter zlicza ustawione statki
    counter=0
    for i in range(0, 10):
        for j in range(0, 10):
            Player_list[i][j]=0

    while counter==0: #ustawianie czteromasztowca
        counter+=1
        x1,y1=random_position(0,9)
        Player_list[x1][y1]=1
        #ustawianie czteromasztowca
        set_4ship(Player_list,x1,y1)
        #ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(Player_list)
    #ustawianie trójmasztowców
    while counter < 3:
        x2,y2=random_position(0,9)
        o=Neighbour(Player_list,x2,y2,1)
        if o.neighbour()==0 and Player_list[x2][y2]==0:
            Player_list[x2][y2]=1
            s=Ship_3(Player_list,x2,y2,random_direction(x2,y2,2))
            if s.set_ship():
                counter+=1
                #uzupełnienie sąsiadów wartością 2
                put_2(Player_list)
            else:
                Player_list[x2][y2]=0
    #ustawianie dwumasztowców
    while counter < 6:
        x3,y3=random_position(0,9)
        o1=Neighbour(Player_list,x3,y3,1)
        if o1.neighbour()==0 and Player_list[x3][y3]==0:
            Player_list[x3][y3]=1
            s1=Ship_2(Player_list,x3,y3,random_direction(x3,y3,1))
            if s1.set_ship():
                counter+=1
                put_2(Player_list)
            else:
                Player_list[x3][y3]=0

    #ustawianie jednomasztowców
    while counter <10:
        x4,y4=random_position(0,9)
        o2=Neighbour(Player_list,x4,y4,1)
        if o2.neighbour()==0 and Player_list[x4][y4]==0:
            Player_list[x4][y4]=1
            counter+=1
            put_2(Player_list)

#uzupełnienie planszy komputera
def draw_AI():
    # counter zlicza ustawione statki
    counter = 0
    for i in range(0, 10):
        for j in range(0, 10):
            AI_list[i][j] = 0

    while counter == 0:  # ustawianie czteromasztowca
        counter += 1
        x1, y1 = random_position(0, 9)
        AI_list[x1][y1] = 1
        # ustawianie czteromasztowca
        set_4ship(AI_list, x1, y1)
        # ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(AI_list)
    # ustawianie trójmasztowców
    while counter < 3:
        x2, y2 = random_position(0, 9)
        o = Neighbour(AI_list, x2, y2, 1)
        if o.neighbour() == 0 and AI_list[x2][y2] == 0:
            AI_list[x2][y2] = 1
            s = Ship_3(AI_list, x2, y2, random_direction(x2, y2, 2))
            if s.set_ship():
                counter += 1
                # uzupełnienie sąsiadów wartością 2
                put_2(AI_list)
            else:
                AI_list[x2][y2] = 0
    # ustawianie dwumasztowców
    while counter < 6:
        x3, y3 = random_position(0, 9)
        o1 = Neighbour(AI_list, x3, y3, 1)
        if o1.neighbour() == 0 and AI_list[x3][y3] == 0:
            AI_list[x3][y3] = 1
            s1 = Ship_2(AI_list, x3, y3, random_direction(x3, y3, 1))
            if s1.set_ship():
                counter += 1
                put_2(AI_list)
            else:
                AI_list[x3][y3] = 0

    # ustawianie jednomasztowców
    while counter < 10:
        x4, y4 = random_position(0, 9)
        o2 = Neighbour(AI_list, x4, y4, 1)
        if o2.neighbour() == 0 and AI_list[x4][y4] == 0:
            AI_list[x4][y4] = 1
            counter += 1
            put_2(AI_list)

def Player_1():

    draw_player()

    while True:

        input(pygame.event.get())
        SCREEN.blit(BACKGROUND, (0,0))

        text("Ships ready for battle, Captain!", FONT1, WIDTH/2, HEIGHT*0.75/8,WHITE)
        text("To reset ships' positions, click \"RESET\" button", FONT2, WIDTH/2, HEIGHT*1.5/8,WHITE)


        for i in range (HEIGHT_1_B, HEIGHT_1_E, BUTTON_HEIGHT_1+2):
            for j in range (WIDTH_1_B,WIDTH_1_E,BUTTON_WIDTH_1+2):
                button_main(SCREEN,j,j+BUTTON_WIDTH_1,i,i+BUTTON_HEIGHT_1,RED,WHITE,None)
                if Player_list[(i - HEIGHT_1_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_1_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == 1:
                    SCREEN.blit(SHIP,(j,i))



        pygame.display.flip()


