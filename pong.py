import pygame
import random

pygame.init()

clock=pygame.time.Clock()
speed=30


window=pygame.display.set_mode((500,300))

x=100
y=100
r=10
dx=3
dy=3

play_score=0

paddle_x=10
paddle_y=10
paddle_width=3
paddle_height=40


def randomize_pos():
    global x,y,dy
    x=random.randint(int(500/4),500-20)
    y=random.randint(10,300-10)
    if(random.randint(0,2)%2==0):
        dy*=-1

def hit_back():
    if(x+r>500):
        return True
    else:
        return False

def hit_paddle():
    global play_score
    if(x-r<paddle_x+paddle_width and paddle_y<y and y<paddle_y+paddle_height):
        play_score+=10
        return True
    else:
        return False

def hit_sides():
    if(y+r>300 or y-r<0):
        return True
    else:
        return False

def game_over():
    global play_score
    end_game=True
    window.fill((0,0,0))

    font_title=pygame.font.Font(None,36)
    font_instructions=pygame.font.Font(None,24)

    anouncements=font_title.render("GAME OVER",True,(255,255,255))
    announcement_rect = anouncements.get_rect(center=((500/2),(300/3)))
    window.blit(anouncements,announcement_rect)

    final_score="FINAL-SCORE : "+str(play_score)
    sinstructions=font_instructions.render(final_score,True,(255,255,255))
    sinstructions_rect=sinstructions.get_rect(center=((500/2),(300/2)))
    window.blit(sinstructions,sinstructions_rect)

    qinstructions=font_instructions.render("PRESS Q TO QUIT",True,(255,255,255))
    qinstructions_rect=qinstructions.get_rect(center=((500/2),(300/1.5)))
    window.blit(qinstructions,qinstructions_rect)

    rinstructions=font_instructions.render("PRESS R TO RESUME",True,(255,255,255))
    rinstructions_rect=rinstructions.get_rect(center=((500/2),(300/1.3)))
    window.blit(rinstructions,rinstructions_rect)

    pygame.display.flip()

    while end_game:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_q):
                    exit()
                if(event.key == pygame.K_r):
                    end_game = False

pygame.display.set_caption('PONG')

window.fill((0,0,0))

welcome_font=pygame.font.Font(None,30)
start=pygame.font.Font(None,24)
welcome_msg=welcome_font.render("LET'S PLAY PONG",True,(255,255,255))
welcome_msg_rect=welcome_msg.get_rect(center=((500/2),(300/2)))
window.blit(welcome_msg,welcome_msg_rect)
start_msg=start.render("PRESS S TO START",True,(255,255,255))
start_msg_rect=start_msg.get_rect(center=((500/2),(300/1.5)))
window.blit(start_msg,start_msg_rect)
pygame.display.flip()

pygame.time.set_timer(pygame.USEREVENT,10000)

timer_active=True

while(timer_active):
    for event in pygame.event.get():
        if(event.type==pygame.KEYDOWN):
            if(event.key == pygame.K_s):
                timer_active=False
        if(event.type == pygame.USEREVENT):
            timer_active=False

randomize_pos()

while True:
    clock.tick(speed)

    pressed_key=pygame.key.get_pressed()
    if(pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]):
        if(paddle_y+paddle_height+10 <= 300):
            paddle_y+=10
    
    if(pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]):
        if(paddle_y-10>=0):
            paddle_y-=10
        


    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()

    window.fill((0,0,0))

    x=x+dx

    y=y+dy

    pygame.draw.rect(window,(255,255,255),(paddle_x,paddle_y,paddle_width,paddle_height))

    pygame.draw.circle(window,(255,255,255),(x,y),r)

    if(x<r):
        game_over()
        randomize_pos()
        dx=abs(dx)
        play_score=0
    if(hit_back() or hit_paddle()):
        dx*=-1
    if(hit_sides()):
        dy*=-1

    pygame.display.update()
 

     