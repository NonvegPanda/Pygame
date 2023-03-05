import pygame, sys
import Platformer


 
from pygame.locals import *
def main():
 pygame.init() # initiates pygame
 clock = pygame.time.Clock()


 pygame.display.set_caption('Pygame Platformer')

 WINDOW_SIZE = (800,600)

 screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

 display = pygame.Surface((500,400)) # used as the surface for rendering, which is scaled

 
 
 Run = True
 
 font = pygame.font.Font('freesansbold.ttf', 30)
 font2 = pygame.font.Font('freesansbold.ttf', 20)
 bg1 = pygame.image.load("bg.png")
 bg = pygame.transform.scale(bg1,(500,400))
 videostart = False
 la_finish = False
 


 while Run == True: # game loop
     
    
    
    
    time =pygame.time.get_ticks()
    
    if time > 3000:
        la_finish =  True
    if time < 3000:
        la_finish =  False
    if time > 11000:
        videostart = True
    
    
    

    
    
       
    
    
    
    
    
    la = font.render("LONG AGO...", False, (255, 255, 255))
    rect = la.get_rect()
    rect.center = display.get_rect().center
    display.fill((0,0,0))
    
    if la_finish == False:
     display.blit(la, rect)
     
    if la_finish == True:
         gameover = font.render(" IN A LAND FAR FAR AWAY...", False, (255, 255, 255))
         rect = gameover.get_rect()
         rect.center = display.get_rect().center
         
         display.blit(gameover, rect)
         
    if videostart == True:
        Platformer.main()

    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            Run = False
            pygame.quit()
            sys.exit()
            
            
    
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    
    print(time)
       
    
    

    
main()