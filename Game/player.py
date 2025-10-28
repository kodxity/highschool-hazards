
from image_sprite import ImageSprite
import pygame

class Player(ImageSprite):
    def __init__(self):
        super().__init__("player", image_file_location="media/player0.png", frames = 6, scale = 100)
        self.__stress = 1
        self.__i_frames = 0
        self.__heal_timer = 50
        self.__healing = False
        
    def marqueeX(self, speed, max_x, min_x = 0):
        self.setX(self.getX() - speed)  # make it move in left direction

        if self.getX() < min_x - self._surface.get_width():
            self.setX(max_x)

        self.updatePosition()

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        # makes it so that sprites stop at the border
        if self.getX() > max_width - self._surface.get_width():
            self.setX(max_width - self._surface.get_width())
        if self.getX() < min_width:
            self.setX(min_width)

        if self.getY() > max_height - self._surface.get_height(): # touches the ground
            self._jumped = False # can jump now
            self.setYVelocity(0)
            self.setY(max_height - self._surface.get_height())

    def countDown(self):
        if self.__stress >= 50:
            if not self.__healing:
                self.__heal_timer = 100
                self.__healing = True
            if self.__healing:
                self.__heal_timer -= 1
                if self.__heal_timer == 0:
                    self.decreaseStress()
                    self.__healing = False


    def addStress(self, stress):
        self.__stress += stress
        self.__i_frames = 20

    def setStress(self, stress):
        self.__stress = stress

    def decreaseStress(self):
        self.__stress -= 50
        if self.__stress <= 1:
            self.__stress = 1

    def IFrameCountdown(self):
        self.__i_frames -= 1
        if self.__i_frames <= 0:
            self.__i_frames = 0

    def getStress(self):
        return self.__stress

    def getIFrames(self):
        return self.__i_frames
