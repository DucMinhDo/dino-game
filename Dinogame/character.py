import pygame
import random


class DINO:
    def __init__(self, file, x, y, vy, ay):
        self.file = file
        self.x = x
        self.y = y
        self.y0 = y
        self.vy = vy
        self.vy0 = vy
        self.ay = ay

    def move(self, delay):
        self.delay = delay
        self.y -= self.vy * self.delay
        self.vy -= self.ay * delay

    def death(self):
        pass


class OBSTACLES:
    def __init__(self, file, x, y, vx):
        self.character = random.choice(file)
        self.file = file
        self.x = x
        self.x0 = x
        self.y = y
        self.vx = vx

    @property
    def vx(self):
        return self.__vx

    @vx.setter
    def vx(self, value):
        self.__vx = value

    def move(self, main, delay):
        self.x -= self.vx * delay
        if self.x <= -100:
            self.x = self.x0
            self.character = random.choice(self.file)
