import pygame as pg
import random
from Intro import *
from os import path
from sprites import *
from settings import *
from terrain import *
from mob import *

class Game:
    def __init__(self):
        #Initialize game window
        pg.init()
        pg.mixer.init()
        snd_dir = os.path.join(game_folder, "snd")

        #background music
        pg.mixer.music.load(path.join(snd_dir, 'Knight_Artorias.ogx'))
        #pg.mixer.music.set_pos(5.0)

        #volumen
        pg.mixer.music.set_volume(0.1)

        #reproducir musica con loop
        pg.mixer.music.play(loops=-1)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #Start a new game
        self.all_sprites = pg.sprite.Group()
        self.mob_sprites = pg.sprite.Group()
        self.player = Player()
        self.my_map = mymap()
        self.mob = Mob(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        self.mob_sprites.add(self.mob)
        Intro(self)
        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game loop - Update
        self.all_sprites.update()

    def events(self):
        #Game loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
                    pg.quit()
                    quit()

            if event.type == pg.KEYDOWN:
                keyname = pg.key.name(event.key)
                if keyname == "up" or keyname == "down" or keyname == "left" or keyname == "right":
                    self.player.keys.keypressed(keyname, self.player.keys.mov_keyspressed)
                else:
                    self.player.keys.keypressed(keyname, self.player.keys.action_keyspressed)
            if event.type == pg.KEYUP:
                keyname = pg.key.name(event.key)
                if keyname == "up" or keyname == "down" or keyname == "left" or keyname == "right":
                    self.player.keys.keyreleased(keyname, self.player.keys.mov_keyspressed)
                else:
                    self.player.keys.keyreleased(keyname, self.player.keys.action_keyspressed)


    def draw(self):
        #Game loop - Draw
        self.screen.fill(WHITE)
        self.screen.blit(self.my_map, (-80, -40), (0, 0, 960, 680))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #Game splash/start screen
        pass

    def show_go_screen(self):
        #Game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
quit()
