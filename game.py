import pygame
from constant import *
from logic import *

pygame.init()
random.seed()
level = [1, 0, 0]  # poziom trudności

FONT1=pygame.font.SysFont("Times New Roman", 80)
FONT2=pygame.font.SysFont("Times New Roman", 50)
FONT3=pygame.font.SysFont("Times New Roman", 60)
FONT4=pygame.font.SysFont("Times New Roman", 100)
FONT5=pygame.font.SysFont("Times New Roman", 20)
FONT6=pygame.font.SysFont("Times New Roman", 25)
FONT7=pygame.font.SysFont("Times New Roman", 18)

#inicjowanie planszy komputera
AI_list=[[] for i in range(0,10,1)]
#inicjowanie planszy gracza
Player_list=[[] for i in range (0,10,1)]
for i in range(0,10):
    for j in range(0,10):
        Player_list[i].append((lambda x:x)(0))
        AI_list[i].append((lambda x:x)(0))

equal=lambda x:x
#wypełnienie planszy gracza

def draw_player():
    #counter zlicza ustawione statki
    counter=0
    for i in range(0, 10):
        for j in range(0, 10):
            Player_list[i][j]=equal(0)

    while counter==0: #ustawianie czteromasztowca
        counter+=1
        x1,y1=random_position(0,9)
        Player_list[x1][y1]=equal(1)
        #ustawianie czteromasztowca
        set_4ship(Player_list,x1,y1)
        #ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(Player_list)
    #ustawianie trójmasztowców
    while counter < 3:
        x2,y2=random_position(0,9)
        o=Neighbour(Player_list,x2,y2,1)
        if o.neighbour()==0 and Player_list[x2][y2]==0:
            Player_list[x2][y2]=equal(1)
            s=Ship_3(Player_list,x2,y2,random_direction(x2,y2,2))
            if s.set_ship():
                counter+=1
                #uzupełnienie sąsiadów wartością 2
                put_2(Player_list)
            else:
                Player_list[x2][y2]=equal(0)
    #ustawianie dwumasztowców
    while counter < 6:
        x3,y3=random_position(0,9)
        o1=Neighbour(Player_list,x3,y3,1)
        if o1.neighbour()==0 and Player_list[x3][y3]==0:
            Player_list[x3][y3]=equal(1)
            s1=Ship_2(Player_list,x3,y3,random_direction(x3,y3,1))
            if s1.set_ship():
                counter+=1
                put_2(Player_list)
            else:
                Player_list[x3][y3]=equal(0)

    #ustawianie jednomasztowców
    while counter <10:
        x4,y4=random_position(0,9)
        o2=Neighbour(Player_list,x4,y4,1)
        if o2.neighbour()==0 and Player_list[x4][y4]==0:
            Player_list[x4][y4]=equal(1)
            counter+=1
            put_2(Player_list)



#uzupełnienie planszy komputera
def draw_AI():
    # counter zlicza ustawione statki
    counter = 0
    for i in range(0, 10):
        for j in range(0, 10):
            AI_list[i][j] = equal(0)

    while counter == 0:  # ustawianie czteromasztowca
        counter += 1
        x1, y1 = random_position(0, 9)
        AI_list[x1][y1] = equal(1)
        # ustawianie czteromasztowca
        set_4ship(AI_list, x1, y1)
        # ustawianie sąsiadów okrętu na wartość 2 zapobiega ustawianiu innych okrętów dookoła
        put_2(AI_list)
    # ustawianie trójmasztowców
    while counter < 3:
        x2, y2 = random_position(0, 9)
        o = Neighbour(AI_list, x2, y2, 1)
        if o.neighbour() == 0 and AI_list[x2][y2] == 0:
            AI_list[x2][y2] = equal(1)
            s = Ship_3(AI_list, x2, y2, random_direction(x2, y2, 2))
            if s.set_ship():
                counter += 1
                # uzupełnienie sąsiadów wartością 2
                put_2(AI_list)
            else:
                AI_list[x2][y2] = equal(0)
    # ustawianie dwumasztowców
    while counter < 6:
        x3, y3 = random_position(0, 9)
        o1 = Neighbour(AI_list, x3, y3, 1)
        if o1.neighbour() == 0 and AI_list[x3][y3] == 0:
            AI_list[x3][y3] = equal(1)
            s1 = Ship_2(AI_list, x3, y3, random_direction(x3, y3, 1))
            if s1.set_ship():
                counter += 1
                put_2(AI_list)
            else:
                AI_list[x3][y3] = equal(0)

    # ustawianie jednomasztowców
    while counter < 10:
        x4, y4 = random_position(0, 9)
        o2 = Neighbour(AI_list, x4, y4, 1)
        if o2.neighbour() == 0 and AI_list[x4][y4] == 0:
            AI_list[x4][y4] = equal(1)
            counter += 1
            put_2(AI_list)

def Player_1():


    pygame.mixer.music.load('Pirates of the Caribbean - Hes a Pirate (Extended).mp3')
    pygame.mixer.music.play(-1)
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

        # przejście dalej
        button_main(SCREEN, WIDTH / 8, WIDTH * 3 / 8, HEIGHT * 5.25 / 8, HEIGHT * 6.25 / 8, BLUE,GREEN,
                    Continue)
        # losowanie planszy raz jeszcze
        button_main(SCREEN, WIDTH * 5 / 8, WIDTH * 7 / 8, HEIGHT * 5.25 / 8, HEIGHT * 6.25 / 8, BLUE, GREEN,
                    draw_player)

        text("CONTINUE", FONT2, WIDTH / 4, HEIGHT * 5.75 / 8, BLACK)
        text("RESET", FONT3, WIDTH * 3 / 4, HEIGHT * 5.75 / 8, BLACK)

        text("Choose difficulty level",FONT2,WIDTH / 2, HEIGHT * 6.75 / 8, WHITE)

        button_level(SCREEN,WIDTH * 2.25 / 10, WIDTH * 3.75 / 10, HEIGHT * 7 / 8, HEIGHT * 7.5 / 8, BLUE,GREEN,0,level)
        text("EASY", FONT5, WIDTH * 3 / 10, HEIGHT * 7.25 / 8, WHITE)
        button_level(SCREEN, WIDTH * 4.25 / 10, WIDTH * 5.75 / 10, HEIGHT * 7 / 8, HEIGHT * 7.5 / 8, BLUE,GREEN,1,level)
        text("HARD", FONT5, WIDTH * 5 / 10, HEIGHT * 7.25 / 8, WHITE)
        button_level(SCREEN, WIDTH * 6.25 / 10, WIDTH * 7.75 / 10, HEIGHT * 7 / 8, HEIGHT * 7.5 / 8, BLUE,GREEN,2,level)
        text("EXTREME", FONT5, WIDTH * 7 / 10, HEIGHT * 7.25 / 8, WHITE)

        pygame.display.flip()



#wygrana komputera
def endgame1():

    pygame.mixer.music.stop
    pygame.mixer.music.load('FAIL SOUND EFFECT.mp3')
    pygame.mixer.music.play(-1)

    while True:
        input(pygame.event.get())
        SCREEN.blit(DEFEAT, (0,0))

        button_main(SCREEN, WIDTH / 8, WIDTH * 3 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, Player_1)
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
        SCREEN.blit(VICTORY, (0,0))

        button_main(SCREEN, WIDTH / 8, WIDTH * 3 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, Player_1)
        text("REPLAY", FONT2, WIDTH / 4, HEIGHT * 7 / 8, BLACK)
        button_main(SCREEN, WIDTH * 5 / 8, WIDTH * 7 / 8, HEIGHT * 6.5 / 8, HEIGHT * 7.5 / 8, WHITE, WHITE, quit)
        text("QUIT", FONT2, WIDTH * 3 / 4, HEIGHT * 7 / 8, BLACK)

        pygame.display.flip()

def Continue():

    draw_AI()
    #losowanie kto zaczyna
    x=random.randint(0,2)
    flag=0

    while True:
        input(pygame.event.get())
        SCREEN.blit(BACKGROUND, (0,0))

        text("START THE BATTLE!", FONT4, WIDTH / 2, HEIGHT * 0.5 / 8, WHITE)
        text("YOU", FONT1, WIDTH_2_B + 5 * (BUTTON_WIDTH_1 + 2), HEIGHT * 2.5 / 10, WHITE)
        text("COMPUTER", FONT1, WIDTH_3_B + 5 * (BUTTON_WIDTH_1 + 2), HEIGHT * 2.5 / 10, WHITE)

        #pozostałe okręty (pola)
        counter1 = 0
        counter2 = 0
        #strzały gracza i Ai
        player_hits = 0
        AI_hits = 0

        for i in range(0,10):
            counter1+=Player_list[i].count(1)
            counter2+=AI_list[i].count(1)
            player_hits+=AI_list[i].count(-1)
            player_hits+=AI_list[i].count(-2)
            AI_hits+=Player_list[i].count(-1)
            AI_hits += Player_list[i].count(-2)

        if flag==0:
            flag+=1
            if x==0:
                if level[0] == 1:
                    hit_by_AI_easy(Player_list)
                elif level[1] == 1:
                    hit_by_AI_normal(Player_list)
                elif level[2] == 1:
                    hit_by_AI_hard(Player_list)


        # ruch AI po ruchu gracza
        if player_hits == AI_hits + 1:
            if level[0] == 1:
                hit_by_AI_easy(Player_list)
            elif level[1] == 1:
                hit_by_AI_normal(Player_list)
            elif level[2] == 1:
                hit_by_AI_hard(Player_list)


        if counter1 == 0:
            sleep(0.2)
            endgame1()

        if counter2 == 0:
            sleep(0.2)
            endgame2()

        text("YOUR FLEET'S POWER: "+str(counter1), FONT6, WIDTH_2_B + 5 * (BUTTON_WIDTH_1 + 2), HEIGHT * 7 / 10, WHITE)
        text("ENEMY FLEET'S POWER "+str(counter2), FONT6, WIDTH_3_B + 5 * (BUTTON_WIDTH_1 + 2), HEIGHT * 7 / 10, WHITE)
        text("Click on a square to shoot!", FONT7,WIDTH / 2, HEIGHT * 7.5 / 10, WHITE)
        text("If you hit enemy's ship, you'll see this picture: ", FONT7, WIDTH / 2, HEIGHT * 8 / 10, WHITE)
        SCREEN.blit(D_SHIP, (WIDTH * 7 / 8, HEIGHT * 7.8 / 10))
        text("If your shoot misses the target, you'll see this picture: ", FONT7, WIDTH / 2, HEIGHT * 8.5 / 10, WHITE)
        SCREEN.blit(ANCHOR, (WIDTH * 7 / 8, HEIGHT * 8.35 / 10))
        text("Each fleet consists of one four-master, two three-masters, three two-masters and four one-masters",FONT7, WIDTH / 2, HEIGHT * 9 / 10, WHITE)


        for i in range(HEIGHT_2_B,HEIGHT_2_E,BUTTON_HEIGHT_1+2):
            for j in range(WIDTH_2_B,WIDTH_2_E,BUTTON_WIDTH_1+2):
                b=Button(SCREEN,j,j+BUTTON_WIDTH_1,i,i+BUTTON_HEIGHT_1,RED,WHITE,None,Player_list,(i-HEIGHT_2_B-2)//(BUTTON_WIDTH_1+2)+1,(j - WIDTH_2_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1)
                b.button()
                if Player_list[(i - HEIGHT_2_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_2_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == 1:
                    SCREEN.blit(SHIP,(j,i)) # pokaż statek
                if Player_list[(i - HEIGHT_2_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_2_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == -1:
                    SCREEN.blit(D_SHIP, (j, i))  # pokaż zniszczony statek
                if Player_list[(i - HEIGHT_2_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_2_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == -2:
                    SCREEN.blit(ANCHOR, (j, i))  # pokaż kotwicę

        for i in range(HEIGHT_3_B,HEIGHT_3_E,BUTTON_HEIGHT_1+2):
            for j in range(WIDTH_3_B,WIDTH_3_E,BUTTON_WIDTH_1+2):
                b1=Button(SCREEN,j,j+BUTTON_WIDTH_1,i,i+BUTTON_HEIGHT_1,RED,WHITE,hit_by_player,AI_list,(i-HEIGHT_3_B-2)//(BUTTON_WIDTH_1+2)+1,(j - WIDTH_3_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1)
                b1.button()
                if AI_list[(i - HEIGHT_3_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_3_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == -1:
                    SCREEN.blit(D_SHIP, (j, i))  # pokaż zniszczony statek
                if AI_list[(i - HEIGHT_3_B - 2) // (BUTTON_WIDTH_1 + 2) + 1][
                    (j - WIDTH_3_B - 2) // (BUTTON_HEIGHT_1 + 2) + 1] == -2:
                    SCREEN.blit(ANCHOR, (j, i))  # pokaż kotwicę

        pygame.display.flip()