import pygame 
import os
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

WHITE = "#FFFFFF"
BLACK = "#000000"
YELLOW = (255,255,0)
RED=(255,0,0)
FPS = 60
SPACESHIP_WIDTH = 60
SPACESHIP_HEIGHT = 50
VEL = 5
MAX_BULLITS = 5
BULLIT_VEL = 10
RED_HIT = pygame.USEREVENT +1
YELLOW_HIT = pygame.USEREVENT +2

HELTH_FONT = pygame.font.SysFont("Agency FB", 20, True)
WINNER_FONT = pygame.font.SysFont("consolas", 40,True)


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shooter_Pixel") # Sets The Game Title

FIRE_SOUND = pygame.mixer.Sound("Assets\Gun+Silencer.mp3")
HIT_SOUND = pygame.mixer.Sound("Assets\Grenade+1.mp3")

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Assets","spaceship_yellow.png")) # Used to load an image to screen

YELLOW_SPACESHIP = pygame.transform.rotate( pygame.transform.scale(YELLOW_SPACE_SHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) # Used to scale an image according to the pixels of screen

RED_SPACE_SHIP = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACE_SHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

BORDER = pygame.Rect(WIDTH/2 -5,0,10,HEIGHT)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))

def handle_yellow_movement(key_pressed,yellow):
        if key_pressed[pygame.K_a]and yellow.x -VEL >0: #LEFT
            yellow.x -= VEL
        
        if key_pressed[pygame.K_d]and yellow.x +VEL + yellow.width < BORDER.x: #RIGHT
            yellow.x += VEL
        
        if key_pressed[pygame.K_w]and yellow.y -VEL > 0: #UP
            yellow.y -= VEL
        
        if key_pressed[pygame.K_s]and yellow.y +VEL + yellow.width < HEIGHT: #DOWN
            yellow.y += VEL

def handle_red_movement(key_pressed,red):
        if key_pressed[pygame.K_LEFT]and red.x -VEL > BORDER.x + BORDER.width: #LEFT
            red.x -= VEL
        
        if key_pressed[pygame.K_RIGHT]and red.x +VEL + red.width < WIDTH: #RIGHT
            red.x += VEL
        
        if key_pressed[pygame.K_UP]and red.y -VEL > 0: #UP
            red.y -= VEL
        
        if key_pressed[pygame.K_DOWN]and red.y +VEL + red.width < HEIGHT: #DOWN
            red.y += VEL

def handle_bullits(yellow_bullits,red_bullits,yellow,red):
    for bullit in yellow_bullits:
        bullit.x += BULLIT_VEL
        if red.colliderect(bullit):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullits.remove(bullit)
        elif bullit.x > WIDTH:
            yellow_bullits.remove(bullit)
        
    for bullit in red_bullits:
        bullit.x -= BULLIT_VEL
        if yellow.colliderect(bullit):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullits.remove(bullit)
        elif bullit.x < 0:
            red_bullits.remove(bullit)




def draw(red,yellow,yellow_bullits,red_bullits,red_helth,yellow_helth):
    WIN.blit(BACKGROUND,(0,0))        # Fills a Colour BackGround
    pygame.draw.rect(WIN,BLACK,BORDER)

    red_helth_text = HELTH_FONT.render("Health: " + str(red_helth),1,WHITE)
    # x = int(WIDTH -  red_helth_text.get_width()-10)
    WIN.blit(red_helth_text,(WIDTH -  red_helth_text.get_width()- 10,10))
    yellow_helth_text = HELTH_FONT.render("Health: " + str(yellow_helth),1,WHITE)
    WIN.blit(yellow_helth_text,(10,10))

    for bullit in yellow_bullits:
        pygame.draw.rect(WIN,YELLOW,bullit)
        

    for bullit in red_bullits:
        pygame.draw.rect(WIN,RED,bullit)
        

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update() #Updates the main window  

def winnner(text):
    winner_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(winner_text,(WIDTH//2 - winner_text.get_width()//2,HEIGHT//2 - winner_text.get_height()//2))
    pygame.display.update()

    pygame.time.delay(5000)

def main():
    red = pygame.Rect(800,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(60,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow_bullits = []
    red_bullits = []
    
    red_helth = 10
    yellow_helth = 10
    


    clock = pygame.time.Clock() # To control the frame rate of our game
    run = True
    while run:
        clock.tick(FPS) # Risticts the machine to display defind frame rate
        for event in pygame.event.get(): #Trackes the Events OF the Game
            if event.type == pygame.QUIT: # Handles The quit Function
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LCTRL and len(yellow_bullits) < MAX_BULLITS :
                    bullit = pygame.Rect(yellow.x+yellow.width, yellow.y + yellow.height//2-2 ,7,5)
                    yellow_bullits.append(bullit)
                    FIRE_SOUND.play()


            
                if event.key == pygame.K_RCTRL and len(red_bullits) < MAX_BULLITS :
                    bullit = pygame.Rect(red.x,red.y + red.height//2-2, 7,5)
                    red_bullits.append(bullit)
                    FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_helth -=1
                HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_helth -= 1
                HIT_SOUND.play()
        winner_text = ""    
        if red_helth <= 0:
            winner_text = "Yellow Wins"
        if yellow_helth <= 0:
            winner_text = "Red WINS"
        
        if winner_text != "":
            winnner(winner_text)
            break

        

        key_pressed = pygame.key.get_pressed()
        handle_yellow_movement(key_pressed,yellow)
        handle_red_movement(key_pressed,red)
        handle_bullits(yellow_bullits,red_bullits,yellow,red)


        draw(red,yellow,yellow_bullits,red_bullits,red_helth,yellow_helth)   
    


    # pygame.quit() # Quits The Game
    main()

if __name__ == '__main__':
    main()
