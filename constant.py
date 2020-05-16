import pygame

#główne wymiary okna
WIDTH=1000
HEIGHT=1000
#Kolory
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,215,0)
#wymiary przycisków
BUTTON_WIDTH=250
BUTTON_HEIGHT=125
#wymiary przycisków do statków
BUTTON_WIDTH_1=30
BUTTON_HEIGHT_1=30

                # ustawienie plansz
#plansza do ustawiania statków gracza
WIDTH_1_B = 340
HEIGHT_1_B = 290
WIDTH_1_E = 650
HEIGHT_1_E = 600

#plansza w trybie gry
WIDTH_2_B = 150
HEIGHT_2_B = 300
WIDTH_2_E = 460
HEIGHT_2_E = 610

#plansza w trybie gry
WIDTH_3_B = 530
HEIGHT_3_B = 300
WIDTH_3_E = 840
HEIGHT_3_E = 610


#inicjalizacja okna
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # tło, ekran
#załadowanie pliku z tłem
BACKGROUND = pygame.image.load('Tło.jpg')
SHIP=pygame.image.load("SHIP.png")
SHIP = pygame.transform.scale(SHIP, (BUTTON_WIDTH_1, BUTTON_HEIGHT_1))
DEFEAT=pygame.image.load("defeat.jpg")
DEFEAT = pygame.transform.scale(DEFEAT, (WIDTH, HEIGHT))
VICTORY = pygame.image.load('victory.jpg')
D_SHIP = pygame.image.load('ship_d.png')
D_SHIP = pygame.transform.scale(D_SHIP, (BUTTON_WIDTH_1, BUTTON_HEIGHT_1))
ANCHOR = pygame.image.load('anchor.png')
ANCHOR = pygame.transform.scale(ANCHOR, (BUTTON_WIDTH_1, BUTTON_HEIGHT_1))
VICTORY1 = pygame.image.load('victory1.jpg')
VICTORY2 = pygame.image.load('victory2.jpg')

SCREEN = pygame.display.get_surface()