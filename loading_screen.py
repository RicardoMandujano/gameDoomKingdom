import pygame as pg
import os
from os import path 
from random import randint

pg.init() #Siempre al inicio
pg.font.init()

#Pantalla, ancho y alto
WIDTH= 800
HEIGHT= 600

#Colores
BLACK = (0,0,0)
WHITE = (255,255,255)

#Frames por segundo
FPS=60

#Obtener directorio actual
directorio_actual= path.dirname(__file__)
dir_img= path.join(directorio_actual, "Fondo")

screen= pg.display.set_mode((WIDTH, HEIGHT))

clock= pg.time.Clock()
now = pg.time.get_ticks()
myfont = pg.font.SysFont('Algerian', 35)

isrunning = False
loading= True

def display_text_animation(string):
       text = ''
       for i in range(len(string)):
              text += string[i]
              text_surface = myfont.render(text, True, WHITE)
              text_rect = text_surface.get_rect()
              screen.blit(text_surface, (190, 560))
              pg.display.update()
              pg.time.wait(190) #Rapidez de la animación

def game_loading():

       lista = os.listdir(directorio_actual)
       cant_fondos= len(lista)
       num_aleatorio=randint(1, cant_fondos)
       #bg = pg.image.load(path.join(dir_img, "f" + str(num_aleatorio) +".jpg"))
       bg = pg.image.load(path.join(dir_img, "f0.jpg"))
       bg = pg.transform.scale(bg, (WIDTH, HEIGHT))
       texto1 = myfont.render("Cargando ", 1, WHITE)

       #display ...
       while loading:
              screen.fill(WHITE)
              screen.blit(bg,(0,0))
              screen.blit(texto1, (0, 560))
              display_text_animation(' ...')
              pg.display.update()
              
              for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()

game_loading()
pg.quit()


