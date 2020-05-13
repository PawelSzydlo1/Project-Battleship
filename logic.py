import random

#losowanie pozycji
def random_position(a, b):
    x = random.randint(a, b)
    y = random.randint(a, b)
    return x, y

#losowanie kierunku ustawiania statku

def random_direction(index1, index2, amount):
    # 0-północ 1-wschód, 2-południe, 3-zachód
    x=random.randint(0,3)
    if index1<amount or index2>9-amount:
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


