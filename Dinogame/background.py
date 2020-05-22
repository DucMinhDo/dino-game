import pygame


class THEME:
    def __init__(self, file, x, y, vx, delay):
        self.x = x
        self.y = y
        self.picture = file
        self.vx = vx
        self.delay = delay

    def move_loop(self, main):
        if self.x == 0:
            main.blit(self.picture, (self.x, self.y))
            self.x -= self.vx * self.delay
            main.blit(self.picture, (self.x + 500, self.y))
        else:
            self.x -= self.vx * self.delay
            main.blit(self.picture, (self.x, self.y))
            main.blit(self.picture, (self.x + 500, self.y))
            self.x = 0 if self.x < - 500 else self.x

    @property
    def vx(self):
        return self.__vx

    @vx.setter
    def vx(self, value):
        self.__vx = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value


class SUN:
    def __init__(self, file, x, y):
        self.x = x
        self.y = y
        self.file = file
        self.angle = 0

    def spin(self, super, angle):
        self.angle += angle
        super.blit(pygame.transform.rotate(
            self.file, self.angle), (self.x, self.y))


class CLOUD:
    def __init__(self, file, x, y, vx, delay):
        self.file = file
        self.x = x
        self.y = y
        self.vx = vx
        self.delay = delay

    def make_cloud(self, main):
        if -400 <= self.x <= 500:
            main.blit(self.file, (self.x, self.y))
        else:
            self.x = 500

        self.x -= self.vx * self.delay
