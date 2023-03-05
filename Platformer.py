import pygame, sys
import level2


 
from pygame.locals import *
def main():
 pygame.init() # initiates pygame
 clock = pygame.time.Clock()


 pygame.display.set_caption('Pygame Platformer')

 WINDOW_SIZE = (800,600)

 screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

 display = pygame.Surface((500,400)) # used as the surface for rendering, which is scaled

 moving_right = False
 moving_left = False
 vertical_momentum = 0
 air_timer = 0
 Run = True
 game_over = False
 update = True
 font = pygame.font.Font('freesansbold.ttf', 30)
 font2 = pygame.font.Font('freesansbold.ttf', 20)
 bg1 = pygame.image.load("bg.png")
 bg = pygame.transform.scale(bg1,(500,400))
 

 true_scroll = [0,0]

 def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map
    

 game_map = load_map('map')


 grass_img = pygame.image.load('grass.png')
 dirt_img = pygame.image.load('dirt.png')
 portal_img = pygame.image.load('Portall.png')
 


 player_img = pygame.image.load('player (2).png').convert_alpha()
 player_img.set_colorkey((255,255,255))
 
 enemy_img = pygame.image.load('enemys.png').convert_alpha()
 chest_img = pygame.image.load('chest.png').convert_alpha()
 enemy_img.set_colorkey((255,255,255))
 enemy_img.set_colorkey((255,255,255))
 
 player_rect = pygame.Rect(100,100,12,24)
 enemy_rect = pygame.Rect(228,113,16,16)
 chest_rect = pygame.Rect(156,31,16,16)
 level_rect = portal_img.get_rect()
 level_rect.x =1098
 level_rect.y= 387
 
 speedup = False
 current_time= 0
 enemy_move_left = False


 
 def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

 

 def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types



 while Run == True: # game loop
    
    display.blit(bg,(0,0))
    
    pygame.time.get_ticks()
    
    
    

    if player_rect.y > 400:
        game_over = True
        update = False
        print("Death")
    
    

    if player_rect.colliderect(level_rect):
        level2.main()
        
    




    if game_over== True:
        gameover = font.render("Press R to Respawn", False, (255, 255, 255))
        rect = gameover.get_rect()
        rect.center = display.get_rect().center
        display.fill((0,0,0))
        display.blit(gameover, rect)
       
    
    
   
        
    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    
   

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))    
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3
    
    

    player_rect,collisions = move(player_rect,player_movement,tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1

    display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    display.blit(enemy_img,(enemy_rect.x-scroll[0],enemy_rect.y-scroll[1]))
    display.blit(chest_img,(chest_rect.x-scroll[0],chest_rect.y-scroll[1]))
    display.blit(portal_img,(level_rect.x-scroll[0],level_rect.y-scroll[1]))
    
    if player_rect.colliderect(enemy_rect):
        game_over = True
        gameover = font.render("Press R to Respawn", False, (255, 255, 255))
        rect = gameover.get_rect()
        rect.center = display.get_rect().center
        display.blit
        display.blit(gameover, rect)
        
        update = False
    if player_rect.colliderect(chest_rect):
        speedup = True
        
# enemy movement code by surya
    if enemy_rect.x ==32:
        enemy_move_left = False

    if enemy_rect.x ==228:
        enemy_move_left = True

    if enemy_move_left == False:
        enemy_rect = enemy_rect.move([1,0])
    else:
        enemy_rect = enemy_rect.move([-1,0])
    
     
    
   
     
   



    
   
    


    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            Run = False
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_SPACE:
                if air_timer < 6:
                    vertical_momentum = -5
            if event.key == K_UP:
                if air_timer < 6:
                    vertical_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            if event.key == pygame.K_r and game_over == True:
                
                update = True
                main()

    level_show = font2.render("Level : 1", False, (255, 255, 255))
    rect2 = level_show.get_rect()
    rect2.topright = display.get_rect().topright
    display.blit
    display.blit(level_show, rect2)
    
           

             
            
        
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
   
         
    
    pygame.display.update()
    
    def speed():
     clock.tick(60)
    if speedup == False:

        speed()
    if speedup == True:
        clock.tick(90)
    
    print(f"X:{player_rect.x}")
    print(f"Y:{player_rect.y}")
    
    

    
