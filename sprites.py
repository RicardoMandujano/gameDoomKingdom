import pygame as pg
import random
from os import *
from settings import *
from keyhandler import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.clase = "Paladin"
        self.keys = KeyHandler()
        self.movement_dict = {
                              "up": [0, -1],
                              "down": [0, 1],
                              "right": [1, 0],
                              "left": [-1, 0]
                             }

        self.current_frame = 0
        self.last_folder = "down"
        self.last_update = 0
        self.img_dir = path.join(path.join(game_folder, "img"), self.clase)
        self.images = self.get_images(path.join(self.img_dir, "Standing\down"))
        self.image = self.images[self.current_frame]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.speed = [0, 0]
        self.foldername = ""
        self.isattacking = self.attack()
        if not self.isattacking:
            self.foldername, self.ismoving = self.move()

        if not (self.ismoving or self.isattacking):
            self.standing(self.last_folder)

        self.rect.y += self.speed[1]
        self.rect.x += self.speed[0]
        # if self.rect.bottom > HEIGHT:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0

    def attack(self):
        attack_dir = path.join(self.img_dir, "Attacks")
        isattacking = False
        actionkeyspressed = self.keys.get_keynames(self.keys.action_keyspressed)
        for keyname in actionkeyspressed:
            self.speed = [0, 0]
        if len(actionkeyspressed) > 0:
            folder = path.join(attack_dir, self.last_folder)
            isattacking = True
            self.action(folder)

        return isattacking

    def standing(self, folder):
        stand_dir = ""
        stand_dir = path.join(self.img_dir, "Standing")
        stand_dir = path.join(stand_dir, folder)
        self.action(stand_dir)

    def folder_check(self, folder):
        spc = " "
        index = folder.index(spc) if spc in folder else None
        if index != None:
            s1 = folder[0:index]
            s2 = folder[(index + 1):len(folder)]
            if s2 == "up" or s2 == "down":
                folder = s2 + s1
            else:
                folder = s1 + s2

        return folder

    def move(self):
        mov_dir = path.join(self.img_dir, "Movement")
        folder = ""
        ismoving = False
        movkeyspressed = self.keys.get_keynames(self.keys.mov_keyspressed)
        for keyname in movkeyspressed:
            if folder != "":
                folder += " "
            folder += keyname
            folder = self.folder_check(folder)
            self.last_folder = folder
            self.speed[0] += self.movement_dict[keyname][0]
            self.speed[1] += self.movement_dict[keyname][1]
        if len(movkeyspressed) > 0:
            folder = path.join(mov_dir, folder)
            ismoving = True
            self.action(folder)

        return folder, ismoving

    def get_images(self, frames_dir):
        files_range = listdir(frames_dir)
        images = []
        for i in range(len(files_range) - 1):
            images.append(pg.image.load(path.join(frames_dir, str(i) + ".png")))
            images[i].set_colorkey(WHITE)
        return images

    def action(self, folder):
        self.images = self.get_images(folder)
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
