import os
from os import path
from settings import *
import pygame
from Intro import *

pygame.init()

def tutorial2():
       img_dir = path.join(game_folder, "img")

       clock = pygame.time.Clock()
       GameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
       tuto = pygame.image.load(os.path.join(img_dir, "tutorial.jpg")).convert()
       tuto = pygame.transform.scale(tuto, (WIDTH, HEIGHT))
       tuto_rect = tuto.get_rect()

       def text_button(text, font, color):

              textbutton = font.render(text, True, color)
              return textbutton, textbutton.get_rect()

       def button_back(x, y, width, height, text, events, hover_color, color):
        #Getting mouse position
               mouse = pygame.mouse.get_pos()
               click = pygame.mouse.get_pressed()
        #Creating the button
               r = pygame.Rect(x, y, width, height)
               r.center = (x/2, y/1.5)
               pygame.draw.rect(GameDisplay, color, r)
        #If mouse is hovering the button, light it up
               if r.x <= mouse[0] <= r.x + width and r.y <= mouse[1] <= r.y + height:
                  pygame.draw.rect(GameDisplay, hover_color, r)
                  if click[0] == 1:
                         Intro()
                 
        #Creating text for the button
               font = pygame.font.SysFont("Arial", 25)
               textbutton, textrect = text_button(text, font, WHITE)
        #Centering text
               textrect.center = (r.x + (width/2), r.y + (height/2))
               GameDisplay.blit(textbutton, textrect)
               
       done = False

       while not done:
              events = pygame.event.get()
              GameDisplay.fill(WHITE)
              GameDisplay.blit(tuto, tuto_rect)
              mouse = pygame.mouse.get_pos()
              for event in events:
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

              button_back(170, 850, 150, 50, "Regresar", events, DOWN_RED, LIGHT_BLACK)
              
              #GameDisplay.blit(tuto, tuto_rect)

              pygame.display.update()

pygame.quit()


