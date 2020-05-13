import random
from abc import ABCMeta, abstractmethod

#losowanie pozycji
def random_position(a, b):
    x = random.randint(a, b)
    y = random.randint(a, b)
    return x, y

#losowanie kierunku ustawiania statku

def random_direction(index1, index2, amount):
    # 0-północ 1-wschód, 2-południe, 3-zachód
    x=random.randint(0,3)
    if index1<amount or index1>9-amount:
        #przypadki narożników
        if index2<amount:
            if index1<amount:
                while x==3 or x==0:
                    x=random.randint(0,3)
            elif index1>9-amount:
                while x==2 or x==3:
                    x=random.randint(0,3)
        elif index2>9-amount:
            if index1<amount:
                while x==0 or x== 1:
                    x=random.randint(0,3)
            elif index1 > 9-amount:
                while x==2 or x==1:
                    x= random.randint(0,3)
        else: # przypadek gdy kolumna jest odpowiednia
            if index1<amount:
                while x==0:
                    x=random.randint(0,3)
            elif index1 >9-amount:
                while x==2:
                    x=random.randint(0,3)
    # dobry wiersz i zła kolumna
    elif (index1>=amount and index1 <=9-amount and (index2<amount or index2 >9-amount)):
        if index2 < amount:
            while x==3:
                x=random.randint(0,3)
        elif index2 > 9-amount:
            while x==1:
                x=random.randint(0,3)

    return x

#ustawianie czteromasztowca
def set_4ship(array,index1, index2):
    # 0-północ 1-wschód, 2-południe, 3-zachód
    x=random_direction(index1,index2,3)
    for i in range(1,4):
        if x==0:
            array[index1-i][index2]=1
        elif x==1:
            array[index1][index2+i]=1
        elif x==2:
            array[index1+i][index2]=1
        elif x==3:
            array[index1][index2-i]=1

#klasa abstrakcyjna

class NeighbourAbs():

    __metaclass__=ABCMeta

    @abstractmethod
    def neighbour(self):
        pass

class Neighbour(NeighbourAbs):
    __array=[]
    __index1=0
    __index2=0
    __t=0

    def __init__(self,array,index1,index2,t):
        self.__array=array
        self.__index1=index1
        self.__index2=index2
        self.__t=t

    def neighbour(self):

        y=0
        if self.__index1==0 or self.__index1==9:
            if self.__index2==0:
                if self.__index1==0:
                    if self.__array[self.__index1+1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1+1][self.__index2+1]==self.__t:
                        y=1
                else: #index1==9
                    if self.__array[self.__index1-1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1-1][self.__index2+1]==self.__t:
                        y=1
            elif self.__index2==9:
                if self.__index1==0:
                    if self.__array[self.__index1+1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2-1]==self.__t:
                        y=1
                    if self.__array[self.__index1+1][self.__index2-1]==self.__t:
                        y=1
                else: #index1==9
                    if self.__array[self.__index1-1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2-1]==self.__t:
                        y=1
                    if self.__array[self.__index1-1][self.__index2-1]==self.__t:
                        y=1
            else: # index2 nie jest skrajny
                if self.__index1==0:
                    if self.__array[self.__index1+1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2-1]==self.__t:
                        y=1
                    if self.__array[self.__index1+1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1+1][self.__index2-1]==self.__t:
                        y=1
                else: #index1==9
                    if self.__array[self.__index1-1][self.__index2]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1][self.__index2-1]==self.__t:
                        y=1
                    if self.__array[self.__index1-1][self.__index2+1]==self.__t:
                        y=1
                    if self.__array[self.__index1-1][self.__index2-1]==self.__t:
                        y=1
        elif (self.__index1!=0 and self.__index1!=9 and (self.__index2==0 or self.__index2==9)):
            if self.__index2==0:
                if self.__array[self.__index1 + 1][self.__index2] == self.__t:
                    y = 1
                if self.__array[self.__index1-1][self.__index2] == self.__t:
                    y = 1
                if self.__array[self.__index1][self.__index2 + 1] == self.__t:
                    y = 1
                if self.__array[self.__index1 + 1][self.__index2 + 1] == self.__t:
                    y = 1
                if self.__array[self.__index1 - 1][self.__index2 + 1] == self.__t:
                    y = 1
            else: #index2==9
                if self.__array[self.__index1 +1][self.__index2] == self.__t:
                    y = 1
                if self.__array[self.__index1-1][self.__index2] == self.__t:
                    y = 1
                if self.__array[self.__index1][self.__index2 - 1] == self.__t:
                    y = 1
                if self.__array[self.__index1 - 1][self.__index2 - 1] == self.__t:
                    y = 1
                if self.__array[self.__index1 + 1][self.__index2 - 1] == self.__t:
                    y = 1

        else: #Srodek planszy
            if self.__array[self.__index1 + 1][self.__index2] == self.__t:
                y = 1
            if self.__array[self.__index1 - 1][self.__index2] == self.__t:
                y = 1
            if self.__array[self.__index1][self.__index2 + 1] == self.__t:
                y = 1
            if self.__array[self.__index1][self.__index2 - 1] == self.__t:
                y = 1
            if self.__array[self.__index1 - 1][self.__index2 + 1] == self.__t:
                y = 1
            if self.__array[self.__index1+1][self.__index2 + 1] == self.__t:
                y = 1
            if self.__array[self.__index1 + 1][self.__index2 - 1] == self.__t:
                y = 1
            if self.__array[self.__index1 - 1][self.__index2 - 1] == self.__t:
                y = 1

        return y

def put_2(array):
    for i in range(0,10):
        for j in range(0,10):
            o=Neighbour(array,i,j,1)
            if array[i][j]==0 and o.neighbour()==1:
                array[i][j]=2

class Ship():
    __metaclass__=ABCMeta

    @abstractmethod
    def set_ship(self):
        pass

class Ship_3(Ship):

    __array=[]
    __index1=0
    __index2=0
    __direction=0

    def __init__(self, array, index1, index2, direction):
        self.__array=array
        self.__index1=index1
        self.__index2=index2
        self.__direction=direction


    def set_ship(self):
        # 0-północ 1-wschód, 2-południe, 3-zachód
        if self.__direction==0 and self.__array[self.__index1-2][self.__index2]==0:
            for i in range(1,3):
                self.__array[self.__index1-i][self.__index2]=1
            return 1
        elif self.__direction==1 and self.__array[self.__index2+2]==0:
            for i in range (1,3):
                self.__array[self.__index1][self.__index2+i]=1
            return 1
        elif self.__direction==2 and self.__array[self.__index1+2][self.__index2]==0:
            for i in range(1,3):
                self.__array[self.__index1+i][self.__index2]=1
            return 1
        elif self.__direction==3 and self.__array[self.__index1][self.__index2-2]==0:
            for i in range(1,3):
                self.__array[self.__index1][self.__index2-i]=1
            return 1
        return 0















