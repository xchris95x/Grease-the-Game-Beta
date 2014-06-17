import pygame, sys, os, time, random
from random import randint    
from pygame.locals import *

# set up pygame
pygame.init()

def collision(sqr1, sqr2):
    if ((isPointInsideRect(sqr1.left, sqr1.top, sqr2)) or
        (isPointInsideRect(sqr1.left, sqr1.bottom, sqr2)) or
        (isPointInsideRect(sqr1.right, sqr1.top, sqr2)) or
        (isPointInsideRect(sqr1.right, sqr1.bottom, sqr2))):
            return True
    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

    


# set up the window
basicFont = pygame.font.SysFont(None, 30)

windowSurface = pygame.display.set_mode((800, 500), 0, 32)
pygame.display.set_caption('GREASE THE GAME')

playing = False

background = pygame.image.load(os.path.join("bkgrd.png"))
background_rect = pygame.Rect(800,0,800,500)

background2 = pygame.image.load(os.path.join("bkgrd.png"))
background2_rect = pygame.Rect(0,0,800,500)

black = (0,0,0)
white = (255,255,255)

######################## GAME OVER PICTURE!! ################
gameover = pygame.image.load(os.path.join("gameover.png"))
gameover.convert()
gameover_rect = pygame.Rect(200,370, 200,200)


############################# PLAYER #######################################
player1 = pygame.image.load(os.path.join("man_1.png"))
player1.convert()
invspeed = 1
invx = 1
invy = 300
sprite_rect = pygame.Rect(invx, invy, 200, 200)
#create invader 2
player2 = pygame.image.load(os.path.join("man_2.png"))
player2.convert()
#create invader 3
player3 = pygame.image.load(os.path.join("man_3.png"))
player3.convert()
#create invader 4
player4 = pygame.image.load(os.path.join("man_4.png"))
player4.convert()
sprite1 = 1
########################




########################## GUN! VOILENCE!! SAVE OUR CHILDREN!!!! ####################################
gun1 = pygame.image.load(os.path.join("1_gun.png"))
gun1.convert()
gunx = sprite_rect.left + 60
guny = sprite_rect.top + -25
gun1_rect = pygame.Rect(gunx, guny, 100, 40)

gun2 = pygame.image.load(os.path.join("2_gun.png"))
gun2.convert()

gun3 = pygame.image.load(os.path.join("3_gun.png"))
gun3.convert()

gun4 = pygame.image.load(os.path.join("4_gun.png"))
gun4.convert()
shoot = False
firecount = 0

########################## BUllET. DEATH. ERSB BAN!!! #########################################
bullet = pygame.image.load(os.path.join("bullet.png"))
bullet.convert()
bulletspeed = 10
bulletx = 5000
bullety = 5000
bullet_rect = pygame.Rect(bulletx, bullety, 100, 40)

bullet2 = pygame.image.load(os.path.join("bullet2.png"))
bullet.convert()
bulletspeed = 10
bulletx = 5000
bullety = 5000
bullet_rect2 = pygame.Rect(bulletx, bullety, 100, 40)

bullet3 = pygame.image.load(os.path.join("bullet3.png"))
bullet.convert()
bulletspeed = 10
bulletx = 5000
bullety = 5000
bullet_rect3 = pygame.Rect(bulletx, bullety, 100, 40)

bullet4 = pygame.image.load(os.path.join("bullet4.png"))
bullet.convert()
bulletspeed = 10
bulletx = 5000
bullety = 5000
bullet_rect4 = pygame.Rect(bulletx, bullety, 100, 40)

bullet5 = pygame.image.load(os.path.join("bullet5.png"))
bullet.convert()
bulletspeed = 10
bulletx = 5000
bullety = 5000
bullet_rect5 = pygame.Rect(bulletx, bullety, 100, 40)


############################ AI........ LIES.. ITS ALL LIES!!########################

AI11 = pygame.image.load(os.path.join("1.png"))
AI12 = pygame.image.load(os.path.join("2.png"))
AI13 = pygame.image.load(os.path.join("3.png"))

bullet.convert()
AI_rect = pygame.Rect(800, 300, 200,100)

AI21 = pygame.image.load(os.path.join("2.png"))
AI22 = pygame.image.load(os.path.join("3.png"))
AI23 = pygame.image.load(os.path.join("1.png"))

bullet.convert()
AI_rect2 = pygame.Rect(1200, 300,200, 100)

AI31 = pygame.image.load(os.path.join("3.png"))
AI32 = pygame.image.load(os.path.join("1.png"))
AI33 = pygame.image.load(os.path.join("2.png"))

bullet.convert()
AI_rect3 = pygame.Rect(1600, 300, 200, 100)

AI1speed = 1
AI2speed = 1
AI3speed = 1

AIanim = 1
############### Health System ################

playerhealth = 700
bosshealth = 5000
AIhealth = 700
AIhealth2 = 700
AIhealth3 = 700

hp_rect = pygame.Rect(20,20,playerhealth,30)
bosshp_rect = pygame.Rect(50,50,bosshealth,30)




##################### Movie #1 background ########
movie1bg = pygame.image.load(os.path.join("shop.png"))
movie1bg.convert()
movie1bg_rect = pygame.Rect(0,0,800,500)



############# Gain Health ###############
healthball = pygame.image.load(os.path.join("chickenball.png"))
healthball.convert()
hballx = -1000
hbally = -200
healthball_rect = pygame.Rect(hbally,hballx,50,50)
ballspeed = 10
fall = False


moveleft = False
moveright = False
moveup = False
movedown = False
up = False
down = False
gun_pos = 3

shooting = 0
backgroundcount = 0
gameoverx = False
count = 0



# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


###################### Menu ####################
text1 = "Start Game"
text3 = "Exit"
menuoption1 = basicFont.render(text1, True, WHITE)
menuoption3 = basicFont.render(text3, True, WHITE)
menuoption1Rect = menuoption1.get_rect()
menuoption3Rect = menuoption3.get_rect()
menuoption1Rect.left = 350
menuoption3Rect.left = 350
menuoption1Rect.top = 200
menuoption3Rect.top = 250
#### Menu Background ###########
menu = pygame.image.load(os.path.join("menu.png"))
menu.convert()
menu_rect = pygame.Rect(0,0,800,500)
######### vignette ######
vignette = pygame.image.load(os.path.join("vignette.png"))
vignette.convert()
vignette_rect = pygame.Rect(0,0,0,0)




########## LOGO ##########
logo = pygame.image.load(os.path.join("logo.png"))
logo.convert()
logo_rect = pygame.Rect(200,50,0,0)

####### TITLES #################
title = pygame.image.load(os.path.join("title.png"))
title.convert()
title_rect = pygame.Rect(0,0,0,0)



###### Women at the counter for movie #1 ########

talk = pygame.image.load(os.path.join("talk.png"))
talk.convert()
talk_rect = pygame.Rect(0,0,800,500)
talk1 = "hello, and welcome to the chicken store what can I get you sir?"
talk2 = "sorry sir, new rules and regs...."
talk3 = "We cannot serve people over a certain weight this kind of food."
talk4 = "we can only serve you carrots on a stick."
talking1 = basicFont.render(talk1, True, BLACK)
talking2 = basicFont.render(talk2, True, BLACK)
talking3 = basicFont.render(talk3, True, BLACK)
talking4 = basicFont.render(talk4, True, BLACK)
talking1Rect = talking1.get_rect()
talking2Rect = talking2.get_rect()
talking3Rect = talking3.get_rect()
talking4Rect = talking4.get_rect()
talking1Rect.left = 0
talking1Rect.top = 450
talking2Rect.left = 0
talking2Rect.top = 450
talking3Rect.left = 0
talking3Rect.top = 450
talking4Rect.left = 0
talking4Rect.top = 450

################## Man for movie #1 ###############

closeup = pygame.image.load(os.path.join("mancloseup.png"))
closeup.convert()
closeup_rect = pygame.Rect(500,200,305,306)
manmov = pygame.image.load(os.path.join("1man.png"))
manmov.convert()
manmov_rect = pygame.Rect(200,100,200,200)
################ Text ##############
talk1 = "I would like two chicken buckets please!"
talk2 = "what the hell! Man! I come here every day!"
talk3 = "A certain weight? WHAT?! You made me this way!"
talk4 = "The chicken store made me this way! Ah god I am so angry!!"
talk5 = "I know what just to do... I am going to talk to the boss."
talk6 = "See what he has to say about this, Good day!"
talking11 = basicFont.render(talk1, True, BLACK)
talking22 = basicFont.render(talk2 ,True, BLACK)
talking33 = basicFont.render(talk3, True, BLACK)
talking44 = basicFont.render(talk4, True, BLACK)
talking55 = basicFont.render(talk5 ,True, BLACK)
talking66 = basicFont.render(talk6, True, BLACK)
talking11Rect = talking11.get_rect()
talking22Rect = talking22.get_rect()
talking33Rect = talking33.get_rect()
talking44Rect = talking44.get_rect()
talking55Rect = talking55.get_rect()
talking66Rect = talking66.get_rect()
talking11Rect.left = 0
talking11Rect.top = 450
talking22Rect.left = 0
talking22Rect.top = 450
talking33Rect.left = 0
talking33Rect.top = 450
talking44Rect.left = 0
talking44Rect.top = 450
talking55Rect.left = 0
talking55Rect.top = 450
talking66Rect.left = 0
talking66Rect.top = 450

movie1_count = 0
################################################# MOVIE #2 ####################
##
moviebg2 = pygame.image.load(os.path.join("movie2bg.png"))
moviebg2.convert()
moviebg2_rect = pygame.Rect(0,0,500,800)
#### FOR MOVING MAN, USE PREVIOUS ANIMATION
killhim = "I am gonna bluddy kill him!!!"
killhim1 = basicFont.render(killhim, True, WHITE)
killhim1Rect = killhim1.get_rect()
killhim1Rect.left = 200
killhim1Rect.top = 200



###End of movies

############################## FINAL BIT ########################
finalbg = pygame.image.load(os.path.join("office.png"))
finalbg2 = pygame.image.load(os.path.join("office.png"))
boss = pygame.image.load(os.path.join("boss.png"))
boom = pygame.image.load(os.path.join("boom.png"))
boombullet = pygame.image.load(os.path.join("boombullet.png"))
finalbg2.convert
boombullet.convert()
finalbg.convert()
boss.convert()
boom.convert()
boombullet_rect = pygame.Rect(400,220,50,25)
finalbg_rect = pygame.Rect(0,0,0,0)
finalbg2_rect = pygame.Rect (800,0,0,0)
boss_rect = pygame.Rect (400,200,300,300)
boom_rect = pygame.Rect(sprite_rect.left, sprite_rect.top, 100,100)
upness = random.randint(-5,5)

######## Score System ######
score = 0
score_text = "Your Score:" +str (score)
score_1 = basicFont.render(score_text, True, WHITE)
score_Rect = score_1.get_rect()
score_Rect.left = 200
score_Rect.top = 460

bossspeed = 1
### Colide with AI: -5
## Shoot AI: +10
##Kill AI: +50
## Shoot Boss: +1
## Kill boss: +5000




levelcnt = 0
levelcnt2 = 0
logocount = 0
titlecount = 0
flicker = 0
boombullet_count = 0

pygame.mixer.music.load("gamemusic.wav")

nextlevel = False


# GAME STATE
gamestate = 0

hello = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #Move with keys
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if menuoption1Rect.collidepoint(x, y):
                pygame.mixer.music.play(20)
                gamestate = 1
            
            if menuoption3Rect.collidepoint(x,y):
                pygame.quit()
                sys.exit()
            
                    
    #menu 
    if gamestate == 0:
        windowSurface.blit( menu, menu_rect)
        windowSurface.blit(vignette, vignette_rect)
        windowSurface.blit(menuoption1,menuoption1Rect)
        windowSurface.blit(menuoption3,menuoption3Rect)
        

################## Movie #1 #######################
    if gamestate == 1:
            
        if movie1_count > 0 and movie1_count <= 100:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(talk, talk_rect)
            windowSurface.blit(talking1, talking1Rect)

            
        if movie1_count > 100 and movie1_count <= 200:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking11 ,talking11Rect)
            

        if movie1_count > 200 and movie1_count <= 300:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(talk, talk_rect)
            windowSurface.blit(talking2 ,talking2Rect)
            
        if movie1_count >300 and movie1_count <=400:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(talk, talk_rect)
            windowSurface.blit(talking3 ,talking3Rect)
            
        if movie1_count >400 and movie1_count <=500:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(talk, talk_rect)
            windowSurface.blit(talking4 ,talking4Rect)
    
        if movie1_count >500 and movie1_count <= 600:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking22, talking22Rect)

            
        if movie1_count > 600 and movie1_count <= 700:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking33, talking33Rect)
            
        if movie1_count > 700 and movie1_count <= 800:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking44, talking44Rect)
            
        if movie1_count > 800 and movie1_count <= 900:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking55, talking55Rect)
            
        if movie1_count > 900 and movie1_count <= 1100:
            windowSurface.blit(movie1bg , movie1bg_rect)
            windowSurface.blit(vignette, vignette_rect)
            windowSurface.blit(manmov, manmov_rect)
            windowSurface.blit(closeup, closeup_rect)
            windowSurface.blit(talking66, talking66Rect)

        movie1_count += 1

        if movie1_count > 1100:
            if flicker >0 and flicker <=100:
                windowSurface.fill((255,0,0))
            if flicker >100 and flicker <=200:
                windowSurface.fill((255,255,255))
            if flicker > 200 and flicker <=300:
                windowSurface.fill((255,0,0))
            if flicker >300 and flicker <=400:
                windowSurface.fill((255,255,255))
            if flicker >400 and flicker <=500:
                windowSurface.fill((255,0,0))
            if flicker >500 and flicker <=600:
                windowSurface.fill((255,0,0))
            if flicker >600 and flicker <=700:
                windowSurface.fill((255,255,255))
            if flicker > 700 and flicker <=800:
                windowSurface.fill((255,0,0))
            if flicker >800 and flicker <=900:
                windowSurface.fill((255,255,255))
            if flicker >900 and flicker <=1000:
                windowSurface.fill((255,0,0))
                gamestate = 2
            flicker += 1 

        
            
        #####################    START GAME!!!!   #####################
    if gamestate == 2:
        
        
        
        
        if event.type == KEYUP:
            if event.key == ord("a"):
                moveleft = False
            if event.key == ord("d"):
                moveright = False
            if event.key == ord("w"):
                down= False
            if event.key == ord("s"):
                up= False
            if event.key == pygame.K_RCTRL:
                hello = True
        if event.type == KEYDOWN:
            if event.key == ord("a"):
                moveleft = True
            if event.key == ord("d"):
                moveright = True
            if event.key == ord("w"):
                down= True
            if event.key == ord("s"):
                up=True
            if event.key == pygame.K_RCTRL:
                #if shoot == False:
                shooting += 1
                if shooting == 1:
                    bullet_rect.top = gun1_rect.top
                    bullet_rect.left = gun1_rect.right
                if shooting == 2:
                    bullet_rect2.top = gun1_rect.top
                    bullet_rect2.left = gun1_rect.right
                shooting = 0
                shoot = True
                
        
           
       
            
    

            
         #Shoot through the gun
        if shoot == True:
            firecount += 1
        if firecount > 40:
            firecount = 0
            shoot = False
############# count to a number then go to gamestate 5#######
        
                
        if levelcnt == 3000:
            gamestate = 5
        levelcnt += 1
        #detect collisions


        if collision (AI_rect, sprite_rect):
            score -= 5
            playerhealth -= 100
            AI_rect.left = 800
            hp_rect = pygame.Rect(20,20,playerhealth,30)
            
            

        if collision (AI_rect2, sprite_rect):
            score -= 5
            playerhealth -= 100
            AI_rect2.left = 1200
            hp_rect = pygame.Rect(20,20,playerhealth,30)
            

        if collision (AI_rect3, sprite_rect):
            score -= 5
            playerhealth -= 100
            AI_rect3.left = 1600
            hp_rect = pygame.Rect(20,20,playerhealth,30)
            

        if collision(bullet_rect,AI_rect)or collision(bullet_rect2,AI_rect):
            score += 10
            AIhealth -= 80
            bullet_rect.left = 5000
            bullet_rect.top = 5000
            bullet_rect2.left = 5000
            bullet_rect2.top = 5000
            bullet_rect3.left = 5000
            bullet_rect3.top = 5000
            bullet_rect4.left = 5000
            bullet_rect4.top = 5000
            bullet_rect5.left = 5000
            bullet_rect5.top = 5000
            
        if AIhealth <= 0:
            score += 50
            AI_rect.left = 800
            AIhealth = 700
            fire = False

        if collision(bullet_rect,AI_rect2)or collision(bullet_rect2,AI_rect2):
            score += 10
            AIhealth2 -= 80
            bullet_rect.left = 5000
            bullet_rect.top = 5000
            bullet_rect2.left = 5000
            bullet_rect2.top = 5000
            bullet_rect3.left = 5000
            bullet_rect3.top = 5000
            bullet_rect4.left = 5000
            bullet_rect4.top = 5000
            bullet_rect5.left = 5000
            bullet_rect5.top = 5000
           
        if AIhealth2 <= 0:
            score += 50
            AI_rect2.left = 1200
            AIhealth2 = 700
            fire = False

        if collision(bullet_rect,AI_rect3)or collision(bullet_rect2,AI_rect3):
            AIhealth3 -= 80
            bullet_rect.left = 5000
            bullet_rect.top = 5000
            bullet_rect2.left = 5000
            bullet_rect2.top = 5000
            bullet_rect3.left = 5000
            bullet_rect3.top = 5000
            bullet_rect4.left = 5000
            bullet_rect4.top = 5000
            bullet_rect5.left = 5000
            bullet_rect5.top = 5000
            
        if AIhealth3 <=0:
            score += 50
            AI_rect3.left = 1600
            AIhealth3 = 700
            fire = False
        


            ######## BACK GROUND SCROLLING###
        if moveleft == True or moveright == True:
            background_rect.left += -1
            background2_rect.left += -1

        if background_rect.right < 0:
            background_rect.left = 800
            backgroundcount =+ 1

        if background2_rect.right < 0:
            background2_rect.left = 800
            backgroundcount += 1

        


            
        #### Movement limit 
        if sprite_rect.left > 0 and sprite_rect.right < 600:
            if moveleft == True:
                sprite_rect.left += -1
            if moveright == True:
                sprite_rect.left += 1
        else:
            if sprite_rect.left <= 0:
                sprite_rect.left =1
            if sprite_rect.right >= 500:
                sprite_rect.right = 499

        #move arm/gun
        if up == True:
            if gun_pos > 1:
                gun_pos -= 1

        if down == True:
            if gun_pos < 4:
                gun_pos += 1

        if gun_pos == 1:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 70
                #trajectory of the bullet
            bullet_rect.top -= -50
            bullet_rect.left += 80

        bullet_rect2.top -= -50
        bullet_rect2.left += 70

        bullet_rect3.top -= -50
        bullet_rect3.left += 60

        bullet_rect4.top -= -50
        bullet_rect4.left += 50

        bullet_rect5.top -= -50
        bullet_rect5.left += 40
        if gun_pos == 2:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 40
        #trajectory of the bullet
            bullet_rect.top -= -20
            bullet_rect.left += 80

            bullet_rect2.top -= -20
            bullet_rect2.left += 70

            bullet_rect3.top -= -20
            bullet_rect3.left += 60

            bullet_rect4.top -= -20
            bullet_rect4.left += 50

            bullet_rect5.top -= -20
            bullet_rect5.left += 40
        if gun_pos == 3:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 10
            #trajectory of the bullet
            bullet_rect.top -= 0
            bullet_rect.left += 80

            bullet_rect2.top -= 0
            bullet_rect2.left += 70

            bullet_rect3.top -= 0
            bullet_rect3.left += 60

            bullet_rect4.top -= 0
            bullet_rect4.left += 50

            bullet_rect5.top -= 0
            bullet_rect5.left += 40

        if gun_pos == 4:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + -20
            #trajectory of the bullet
            bullet_rect.top -= 50
            bullet_rect.left += 80

            bullet_rect2.top -= 50
            bullet_rect2.left += 70

            bullet_rect3.top -= 50
            bullet_rect3.left += 60

            bullet_rect4.top -= 50
            bullet_rect4.left += 50

            bullet_rect5.top -= 50
            bullet_rect5.left += 40

        ############### HEALTH BALL############

        #prepare the ball
        if fall == False:
            balldrop = random.randrange(-1000,1000)

            if (healthball_rect.left <= -1000):
                ballspeed *= -1

            if (healthball_rect.left >= 1000):
                ballspeed *= -1

            healthball_rect.left += ballspeed
            if healthball_rect.left >= balldrop-100 and healthball_rect.left <= balldrop+100:
                fall=True
            
            
        if fall == True:
            healthball_rect.top += 5
                
            if healthball_rect.top > 500:
                healthball_rect.top = hbally
                fall = False

        
        if collision(sprite_rect,healthball_rect):
            healthball_rect.top = hbally  
            playerhealth += 50
            hp_rect = pygame.Rect(20,20,playerhealth,30)


        if playerhealth > 700:
            playerhealth = 700
        
        windowSurface.blit (background, background_rect)
        windowSurface.blit(background2, background2_rect)
        windowSurface.blit(vignette, vignette_rect)
        windowSurface.blit(healthball, healthball_rect)



        #Animate Player

        if moveleft == True or moveright == True:
            if sprite1 <5:
                windowSurface.blit(player1, sprite_rect)
            if sprite1 >=5 and sprite1 <10:
                windowSurface.blit(player2, sprite_rect)
            if sprite1 >=10 and sprite1 <15:
                windowSurface.blit(player3, sprite_rect)
            if sprite1 >=15:
                windowSurface.blit(player4, sprite_rect)
            sprite1 += 1
            if sprite1 >20:
                sprite1 = 0
        else:
            windowSurface.blit(player1, sprite_rect)

        #Animate AI
        AI_rect.left -= 2
        AI_rect.top += AI1speed

        if AI_rect.bottom > 400:
            AI1speed *= -1

        if AI_rect.bottom < 300:
            AI1speed *= -1

        AI_rect2.left -= 2
        AI_rect2.top += AI2speed

        if AI_rect2.bottom > 400:
            AI2speed *= -1

        if AI_rect2.bottom < 300:
            AI2speed *= -1

        AI_rect3.left -= 2
        AI_rect3.top += AI3speed

        if AI_rect3.bottom > 400:
            AI3speed *= -1

        if AI_rect3.bottom < 300:
            AI3speed *= -1

        #draw gun
        if gun_pos == 1 :
            windowSurface.blit(gun4, gun1_rect)
        if gun_pos == 2:
            windowSurface.blit(gun3, gun1_rect)
        if gun_pos == 3:
            windowSurface.blit(gun2, gun1_rect)
        if gun_pos == 4:
            windowSurface.blit(gun1, gun1_rect)

        windowSurface.blit(bullet, bullet_rect)
        windowSurface.blit(bullet2, bullet_rect2)
        windowSurface.blit(bullet3, bullet_rect3)
        windowSurface.blit(bullet4, bullet_rect4)
        windowSurface.blit(bullet5, bullet_rect5)

        if AIanim >= 1 and AIanim < 4:
            windowSurface.blit(AI11, AI_rect)
            windowSurface.blit(AI21, AI_rect2)
            windowSurface.blit(AI31, AI_rect3)
        if AIanim >= 4 and AIanim < 8:
            windowSurface.blit(AI12, AI_rect)
            windowSurface.blit(AI22, AI_rect2)
            windowSurface.blit(AI32, AI_rect3)
        if AIanim >= 8 and AIanim < 12:
            windowSurface.blit(AI13, AI_rect)
            windowSurface.blit(AI23, AI_rect2)
            windowSurface.blit(AI33, AI_rect3)

        if AIanim < 11:
            AIanim += 1
        else:
            AIanim = 1


        ##########health bar
        pygame.draw.rect(windowSurface,(0,255,0),hp_rect)
    
        
        ####### GAME OVER! ####
    
        if playerhealth <= 0:
            time.sleep(1)
            pygame.mixer.music.stop()
            count = 0
            gamestate = 4
############ Game over Menu###############
    if gamestate == 4:
        playerhealth = 700
        sprite_rect.left = 1
        sprite_rect.top = 300 
        AI_rect.left = 800
        AI_rect.top = 300
        AI_rect2.left = 1200
        AI_rect2.top = 300
        AI_rect3.left = 1600 
        AI_rect3.top = 300
        windowSurface.fill((255,0,0))
        windowSurface.blit(vignette, vignette_rect)
        windowSurface.blit(gameover, gameover_rect)
        windowSurface.blit(menuoption1,menuoption1Rect)
        windowSurface.blit(menuoption3,menuoption3Rect)

############# Movie #2 ################
    if gamestate == 5:
        windowSurface.blit(vignette, vignette_rect)
        go = False
        windowSurface.blit(moviebg2 , moviebg2_rect)
        windowSurface.blit(killhim1, killhim1Rect)
        
        
        while go == False:
            sprite_rect.left += 1
            if sprite1 <5:
                windowSurface.blit(player1, sprite_rect)
                
            if sprite1 >=5 and sprite1 <10:
                windowSurface.blit(player2, sprite_rect)
                
            if sprite1 >=10 and sprite1 <15:
                windowSurface.blit(player3, sprite_rect)
                
            if sprite1 >=15:
                windowSurface.blit(player4, sprite_rect)
            
            sprite1 += 1
            go = True
            if sprite1 >20:
                sprite1 = 0
            else:
                windowSurface.blit(player1, sprite_rect)
                
        if sprite_rect.left == 500:
            gamestate = 6

    ######### FINAL STAGE ################
    if gamestate == 6:
        sprite_rect.left = 0
        if event.type == KEYUP:
            if event.key == ord("a"):
                moveleft = False
            if event.key == ord("d"):
                moveright = False
            if event.key == ord("w"):
                down= False
            if event.key == ord("s"):
                up= False
            if event.key == pygame.K_RCTRL:
                hello = True
        if event.type == KEYDOWN:
            if event.key == ord("a"):
                moveleft = True
            if event.key == ord("d"):
                moveright = True
            if event.key == ord("w"):
                down= True
            if event.key == ord("s"):
                up=True
            if event.key == pygame.K_RCTRL:
                #if shoot == False:
                shooting += 1
                if shooting == 1:
                    bullet_rect.top = gun1_rect.top
                    bullet_rect.left = gun1_rect.right
                if shooting == 2:
                    bullet_rect2.top = gun1_rect.top
                    bullet_rect2.left = gun1_rect.right
                shooting = 0
                shoot = True
                #### Movement limit 
        if sprite_rect.left > 0 and sprite_rect.right < 600:
            if moveleft == True:
                sprite_rect.left += -1
            if moveright == True:
                sprite_rect.left += 1
        else:
            if sprite_rect.left <= 0:
                sprite_rect.left =1
            if sprite_rect.right >= 500:
                sprite_rect.right = 499
                
    
         #Shoot through the gun
        if shoot == True:
            firecount += 1
        if firecount > 40:
            firecount = 0
            shoot = False
            
        if bosshealth <= 0:
            fire = False
            score += 5000
            gamestate = 7
            
            ######## BACK GROUND SCROLLING###
        if moveleft == True or moveright == True:
            finalbg_rect.left += -1
            finalbg2_rect.left += -1

        if background_rect.right < 0:
            finalbg_rect.left = 800
            backgroundcount =+ 1

        if background2_rect.right < 0:
            finalbg2_rect.left = 800
            backgroundcount += 1

        


            
        

        #move arm/gun
        if up == True:
            if gun_pos > 1:
                gun_pos -= 1

        if down == True:
            if gun_pos < 4:
                gun_pos += 1

        if gun_pos == 1:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 70
                #trajectory of the bullet
            bullet_rect.top -= -50
            bullet_rect.left += 80

        bullet_rect2.top -= -50
        bullet_rect2.left += 70

        bullet_rect3.top -= -50
        bullet_rect3.left += 60

        bullet_rect4.top -= -50
        bullet_rect4.left += 50

        bullet_rect5.top -= -50
        bullet_rect5.left += 40
        if gun_pos == 2:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 40
        #trajectory of the bullet
            bullet_rect.top -= -20
            bullet_rect.left += 80

            bullet_rect2.top -= -20
            bullet_rect2.left += 70

            bullet_rect3.top -= -20
            bullet_rect3.left += 60

            bullet_rect4.top -= -20
            bullet_rect4.left += 50

            bullet_rect5.top -= -20
            bullet_rect5.left += 40
        if gun_pos == 3:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + 10
            #trajectory of the bullet
            bullet_rect.top -= 0
            bullet_rect.left += 80

            bullet_rect2.top -= 0
            bullet_rect2.left += 70

            bullet_rect3.top -= 0
            bullet_rect3.left += 60

            bullet_rect4.top -= 0
            bullet_rect4.left += 50

            bullet_rect5.top -= 0
            bullet_rect5.left += 40

        if gun_pos == 4:
            gun1_rect.left = sprite_rect.left + 50
            gun1_rect.top = sprite_rect.top + -20
            #trajectory of the bullet
            bullet_rect.top -= 50
            bullet_rect.left += 80

            bullet_rect2.top -= 50
            bullet_rect2.left += 70

            bullet_rect3.top -= 50
            bullet_rect3.left += 60

            bullet_rect4.top -= 50
            bullet_rect4.left += 50

            bullet_rect5.top -= 50
            bullet_rect5.left += 40
        
        windowSurface.blit (finalbg, finalbg_rect)
        windowSurface.blit(finalbg2, finalbg2_rect)
        windowSurface.blit(vignette, vignette_rect)



        #Animate Player

        if moveleft == True or moveright == True:
            if sprite1 <5:
                windowSurface.blit(player1, sprite_rect)
            if sprite1 >=5 and sprite1 <10:
                windowSurface.blit(player2, sprite_rect)
            if sprite1 >=10 and sprite1 <15:
                windowSurface.blit(player3, sprite_rect)
            if sprite1 >=15:
                windowSurface.blit(player4, sprite_rect)
            sprite1 += 1
            if sprite1 >20:
                sprite1 = 0
        else:
            windowSurface.blit(player1, sprite_rect)

            if moveleft == True:
                sprite_rect.left += 1
            if moveright == True:
                sprite_rect.right += 1
        

        #Animate Boss

        boss_rect.left += bossspeed


        if boss_rect.left > 500:
            bossspeed *= -1

        if boss_rect.left < 400:
            bossspeed *= -1
            
        windowSurface.blit(boss, boss_rect)
        
        #animate boss bullet
        boombullet_rect.left -= 10

        boombullet_rect.top += upness

        
        if boombullet_rect.left < 50:
            upness = random.randint(-5,5)        
            boombullet_rect.left = boss_rect.left
            boombullet_rect.top = boss_rect.top + 20
            
    ########### COLLISIONS #####
        if collision (boombullet_rect, sprite_rect):
            upness = random.randint(-5,5)
            boombullet_rect.left = boss_rect.left
            boombullet_rect.top = boss_rect.top + 20
            playerhealth -= 50
            windowSurface.blit(boom, boom_rect)
            bullet_rect.left = 5000
            bullet_rect.top = 5000
            bullet_rect2.left = 5000
            bullet_rect2.top = 5000
            bullet_rect3.left = 5000
            bullet_rect3.top = 5000
            bullet_rect4.left = 5000
            bullet_rect4.top = 5000
            bullet_rect5.left = 5000
            bullet_rect5.top = 5000
            hp_rect = pygame.Rect(20,20,playerhealth,30)
        if playerhealth <= 0:
            gamestate = 4
        

        if collision(bullet_rect,boss_rect)or collision(bullet_rect2,boss_rect):
            score += 10
            bosshealth -= 50
            
            bullet_rect.left = 5000
            bullet_rect.top = 5000
            bullet_rect2.left = 5000
            bullet_rect2.top = 5000
            bullet_rect3.left = 5000
            bullet_rect3.top = 5000
            bullet_rect4.left = 5000
            bullet_rect4.top = 5000
            bullet_rect5.left = 5000
            bullet_rect5.top = 5000
            bosshp_rect = pygame.Rect(20,50,bosshealth /10,30)
            
        
        windowSurface.blit(boombullet,boombullet_rect)
        

        #draw gun
        if gun_pos == 1 :
            windowSurface.blit(gun4, gun1_rect)
        if gun_pos == 2:
            windowSurface.blit(gun3, gun1_rect)
        if gun_pos == 3:
            windowSurface.blit(gun2, gun1_rect)
        if gun_pos == 4:
            windowSurface.blit(gun1, gun1_rect)

        windowSurface.blit(bullet, bullet_rect)
        windowSurface.blit(bullet2, bullet_rect2)
        windowSurface.blit(bullet3, bullet_rect3)
        windowSurface.blit(bullet4, bullet_rect4)
        windowSurface.blit(bullet5, bullet_rect5)
        pygame.draw.rect(windowSurface,(0,255,0),hp_rect)
        pygame.draw.rect(windowSurface,(255,0,0), bosshp_rect)
        
            
    
        
       

    ###################### Logo and score #############
    if gamestate == 7:
        pygame.mixer.music.stop()
        logocount += 1
        windowSurface.fill((0,0,0))
        windowSurface.blit(logo, logo_rect)
        score_1 = basicFont.render("Score = "+str(score), True, WHITE)
        windowSurface.blit(score_1, score_Rect)
        if logocount == 1000:
            gamestate = 8
        

    ####################### Titles ##################
    if gamestate == 8:
        titlecount += 1
        windowSurface.blit(title, title_rect)
        if titlecount == 1500:
            pygame.quit()
            sys.exit()


        
        
        
    
    
        
    pygame.display.update()                                              
    time.sleep(0.0001)
