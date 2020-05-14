from game import *
from logic import *
from constant import *

pygame.init()
#Nazwa okna
pygame.display.set_caption("Okręty")
#nałożenie na ekran tła
SCREEN.blit(BACKGROUND, (0,0))


while True:

    input(pygame.event.get())

    button_main(SCREEN,(WIDTH-BUTTON_WIDTH)/2,(WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH,200,325,WHITE,GREEN,quit)

    pygame.display.flip()