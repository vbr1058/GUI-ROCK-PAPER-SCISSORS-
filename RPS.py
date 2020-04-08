import pygame as py,sys
from pygame.locals import *
import time
import random as rd 

width = 600
height = 400
line_color = (10,255,10)
white = (200, 255, 255)
user_choice=0

py.init()
fps = 30
CLOCK = py.time.Clock()
screen = py.display.set_mode((width, height+200),1,32)
py.display.set_caption("ROCK PAPER SCISSOR")

opening=py.image.load("open.jpg")
rock=py.image.load("r.jpg")
paper=py.image.load("p.jpg")
scissor=py.image.load("s.jpg")
pc=py.image.load("pc.jpg")
USER_PHOTO=py.image.load("user.jpg")
PC_PHOTO=py.image.load("pc.jpg")
TIED=py.image.load("tied.jpg")

rock=py.transform.scale(rock,(68,68))
paper=py.transform.scale(paper,(68,68))
scissor=py.transform.scale(scissor,(68,68))
opening = py.transform.scale(opening, (width, height+200))
USER_PHOTO=py.transform.scale(USER_PHOTO,(230,230))
PC_PHOTO=py.transform.scale(PC_PHOTO,(230,230))
TIED=py.transform.scale(TIED,(230,230))

#opening the game window 
def game_opening():
	screen.blit(opening,(0,0))
	py.display.update()
	time.sleep(1.5)
	screen.fill(white)
	#Drawing the horizontal and vertical lines 
	py.draw.line(screen,line_color,(width/2,0),(width/2,height+200),5) #7 in the thickness o the line
	py.draw.line(screen,line_color,(0,(height+200)/3),((width/2),((height+200)/3)),5)
	py.draw.line(screen,line_color,(0,(height+200)/3*2),((width/2),((height+200)/3*2)),5)
	py.draw.line(screen,line_color,(width/2,(height+200)/2),((width),((height+200)/2)),5)
	py.draw.line(screen,line_color,(0,25),(width,25),5)

game_opening()
# placing the rock image
rock= py.transform.scale(rock,(width//6,100)) 
screen.blit(rock,(100,60))
# placing the paper image
paper= py.transform.scale(paper,(width//6,100)) 
screen.blit(paper,(100,60*4))
# placing the paper image
scissor= py.transform.scale(scissor,(width//6,100)) 
screen.blit(scissor,(100,450))

#text on the window
font = py.font.SysFont("comicsansms", 50)
font_h= py.font.SysFont("comicsansms", 20)
text_choice= py.font.SysFont("Times New Roman", 30)

heading=font_h.render("Pick your choice below:",10,(0,0,0))
text = font.render("PC Choice",10, (0, 0, 0)) 
text_rock = text_choice.render("ROCK",10, (0, 0, 0)) 
text_paper = text_choice.render("PAPER",10, (0, 0, 0)) 
text_scissor= text_choice.render("SCISSOR",10, (0, 0, 0)) 
res= font.render("<--Result-->",10,(0,0,0))

#Position of the text on the window
text_rect = text.get_rect(center=(width/2+150, height/2+60))
text_res = res.get_rect(center=(width/2+150, height/2+130))
text_hed = heading.get_rect(center=(width//4, 7))
text1=text_rock.get_rect(center=(width//4, 180))
text2=text_paper.get_rect(center=(width//4, 360))
text3=text_paper.get_rect(center=(135, 565))

#placin the text on the screen
screen.blit(text_paper,text2)
screen.blit(text_rock,text1)
screen.blit(text_scissor,text3)
screen.blit(heading,text_hed)
screen.blit(text, text_rect)
screen.blit(res,text_res)
py.display.update()

#Check there is a input from the user
def userClick():
	x,y=py.mouse.get_pos()
	if(x<width//2 and y<height-200):
		user_choice=1
		print(str(user_choice)+". ROCK")
		return user_choice
	elif(x<width//2 and y<height):
		user_choice=2
		print(str(user_choice)+". PAPER")
		return user_choice
	elif(x<width//2 and y<height+200):
		user_choice=3
		print(str(user_choice)+". SCISSOR")
		return user_choice

#pc Selection of the card 
def PC_choice():
	PcChoice=int(rd.randint(1,3))
	if(PcChoice==1):
		screen.blit(rock,(width/2+100,60))
	elif(PcChoice==2):
		screen.blit(paper,(width/2+100,60))
	elif(PcChoice==3):
		screen.blit(scissor,(width/2+100,60))
	return PcChoice

#computing result
def result(user,pc):
	if(user==pc):
		return 0
	elif((user==1 and pc==2)):
		return 2
	elif(user==1 and pc ==3):
		return 1
	elif((user==2 and pc==1)):
		return 1
	elif(user==2 and pc==3):
		return 2
	elif(user==3 and pc==2):
		return 1
	elif(user==3 and pc==1):
		return 2

#printing the result on the screen 
def print_result(re):
	if(re==0):
		screen.blit(TIED,(width/2+50,360))
		print("Game Tied")
	elif(re==1):
		screen.blit(USER_PHOTO,(width/2+50,360))
		print("user wins this round")
	elif(re==2):
		screen.blit(PC_PHOTO,(width/2+50,360))
		print("pc wins the round")

# run the game loop forever
while(True):
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked
            user=userClick()
            PC=PC_choice()
            re=result(user,PC)
            print_result(re)
    py.display.update()
    CLOCK.tick(fps)