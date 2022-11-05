import pygame
pygame.init()

win = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("First Game")
bg_img = pygame.image.load('bg.webp').convert()


x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        
    if not(isJump): 
        

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10  :
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    win.fill((0,0,0))
    win.blit(bg_img, (0, 0))
    pygame.draw.rect(win, (250,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()