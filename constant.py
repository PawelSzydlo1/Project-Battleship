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


#inicjalizacja okna
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # tło, ekran
#załadowanie pliku z tłem
BACKGROUND = pygame.image.load('Tło.jpg')
SHIP=pygame.image.load("SHIP.png")
SHIP = pygame.transform.scale(SHIP, (BUTTON_WIDTH_1, BUTTON_HEIGHT_1))
SCREEN = pygame.display.get_surface()