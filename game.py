from logic import *

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
    #Statki zajmują 20 pól, counter zlicza ustawione pola
    counter=0
    for i in range(0, 10):
        for j in range(0, 10):
            Player_list[i][j]=0



    while counter==0: #ustawianie czteromasztowca
        counter+=1
        x1,y1=random_position(0,9)
        Player_list[x1][y1]=1

    for i in range(0, 10):
        print(Player_list[i])

draw_player()