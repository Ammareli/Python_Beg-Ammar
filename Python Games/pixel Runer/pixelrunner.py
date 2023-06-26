import pygame
from sys import exit
from random import randint,choice
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.player_move_frame = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

        self.image = self.player_move_frame[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.4)
    
    def player_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else: 
            self.player_index += 0.1
            if self.player_index > len(self.player_move_frame): self.player_index = 0
            self.image = self.player_move_frame[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obsticlas(pygame.sprite.Sprite):
    def __init__(self,type) -> None:
        super().__init__()

        if type == "Fly":
            fly_move_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_move_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_move_1,fly_move_2]
            y_pos = 200


        else:
            snail_move_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_move_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_move_1,snail_move_2]
            y_pos = 300
        
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom= (randint(850,1000),y_pos))
    
    def animation_state(self):
        self.index += 0.1
        if self.index >= len(self.frames):self.index = 0
        self.image = self.frames[int(self.index)]
    
    def update(self):
        self.animation_state()
        self.destroy()
        self.rect.x -= 10
    def destroy(self):
        if self.rect.x < -100:
            self.kill()

WIDTH = 800
HEIGHT = 400
PLAYER_GRAVITY = 0
GAME_ACTIVE = False
GAME_TIME = 0
score = 0


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pixel Runner")

# BACKGROUND
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
# Display Screen Fonts
score_font = pygame.font.Font("font/Pixeltype.ttf",30)
game_name_font = pygame.font.Font("font/Pixeltype.ttf",50)

# ITRO SCREEN
player_stand = pygame.image.load("graphics/Player/player_stand.png")
player_stand_rect = player_stand.get_rect(center = (WIDTH//2-30,150))

game_name = game_name_font.render("Pixel Runner",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (WIDTH//2,50))

scaled_player = pygame.transform.rotozoom(player_stand,0,2)

game_message = game_name_font.render("Press Space to start.",False,(111,196,169))
game_message_rect = game_message.get_rect(center = (WIDTH//2, 350))

# Timer

obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer,1500)

fly_timer = pygame.USEREVENT +2
pygame.time.set_timer(fly_timer,200)

snail_timer = pygame.USEREVENT + 3
pygame.time.set_timer(snail_timer,400)

clock = pygame.time.Clock() 

def display_score():

    current = pygame.time.get_ticks()//1000 - GAME_TIME
    score_surface = score_font.render(f"Score :{current}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (WIDTH/2, 50))
    screen.blit(score_surface,score_rect)
    return current

def collition_sprite():
    if pygame.sprite.spritecollide(player.sprite,obsticlas,False):
        obsticlas.empty()
        return False
    else: return  True

# Groups

player = pygame.sprite.GroupSingle()
player.add(Player())

obsticlas = pygame.sprite.Group()


# BackGround Music
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.3)

bg_music.play(loops=-1)

# Game LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if GAME_ACTIVE == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                GAME_ACTIVE = True

                GAME_TIME=pygame.time.get_ticks()//1000
            
        if GAME_ACTIVE:
        
            if event.type == obsticle_timer:
                obsticlas.add(Obsticlas(choice(["Fly","Snail","Snail","Snail"])))


            
    if GAME_ACTIVE:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        score=display_score()
        # Player
        player.draw(screen)
        player.update()
        # enemies
        obsticlas.draw(screen)
        obsticlas.update()
        


        # Collition

        GAME_ACTIVE = collition_sprite()
    
    else:
        screen.fill((94,129,162))
        screen.blit(scaled_player,player_stand_rect)
        screen.blit(game_name,game_name_rect)
        score_surf = game_name_font.render(f"Your score is: {score}",False,(111,196,169))
        score_rect = score_surf.get_rect(center = (400,350))

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_surf,score_rect)

 
    
    pygame.display.update()
    clock.tick(60)