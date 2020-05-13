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


    for i in range(0, 10):
        print(Player_list[i])

draw_player()