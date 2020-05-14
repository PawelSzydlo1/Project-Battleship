from game import *

pygame.init()
#Nazwa okna
pygame.display.set_caption("Okręty")
#nałożenie na ekran tła
SCREEN.blit(BACKGROUND, (0,0))

while True:
    input(pygame.event.get())

    pygame.display.flip()