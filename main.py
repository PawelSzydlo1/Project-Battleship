from game import *
from logic import *
from constant import *

pygame.init()
FONT=pygame.font.SysFont('Times New Roman', 50)

#Nazwa okna
pygame.display.set_caption("Okręty")
#nałożenie na ekran tła
SCREEN.blit(BACKGROUND, (0,0))


while True:

    input(pygame.event.get())

    button_main(SCREEN,(WIDTH-BUTTON_WIDTH)/2,(WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH,200,325,BLUE,GREEN,quit)
    text("EXIT",FONT,(WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH/2, 200+BUTTON_HEIGHT/2, BLACK)

    pygame.display.flip()