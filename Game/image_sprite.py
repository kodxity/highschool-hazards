import pygame
from my_sprite import MySprite

class ImageSprite(MySprite):
        def __init__(self, name, image_file_location, frames, scale):
                super().__init__()
                self.__file_location = image_file_location
                self._surface = pygame.image.load(self.__file_location).convert_alpha()
                self.__image_dirx = True #true is looking to the right
                self.__frames = frames
                
                self.__moving = False # is the object currently moving
                self.__name = name
                self.__image_right = []
                self.__image_left = []
                for i in range(2): # 2 frames for idle
                        img = pygame.image.load(f"media/{self.__name}{i}.png")
                        img = pygame.transform.scale(img, (scale,scale))
                        self.__image_right.append(img)
                        img = pygame.transform.flip(img, True, False)
                        
                        self.__image_left.append(img)

                self.__image_walk_right = []
                self.__image_walk_left = []
                self.__image_jump_right = []
                self.__image_jump_left = []
                self.__deg = 0

        def setScale(self, scale_x, scale_y = None):
                if scale_y == None:
                        scale_y = scale_x
                self._surface = pygame.transform.scale(self._surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))

        def setUpWASDmove(self):
                for i in range(self.__frames):
                        img = pygame.image.load(f"media/{self.__name}walk{i}.png")
                        img = pygame.transform.scale(img, (100,100))
                        self.__image_walk_right.append(img)
                        img = pygame.transform.flip(img, True, False)
                        self.__image_walk_left.append(img)

                for i in range(1): # 1 frame for jump
                        img = pygame.image.load(f"media/{self.__name}jump{i}.png")
                        img = pygame.transform.scale(img, (100,100))
                        self.__image_jump_right.append(img)
                        img = pygame.transform.flip(img, True, False)
                        
                        self.__image_jump_left.append(img)

        def WASDmove(self, pressed_keys):
                
                MySprite.WASDmove(self, pressed_keys)
      
                self.setAnimation()

        def rotateImage(self, dir):
                self._surface = pygame.transform.rotate(self._surface, self.__deg)
                self.__deg -= 1.5 * dir
        def setAnimation(self):       
                self._currframes += 1 
                if self.getDirX() == 1:
                        if self._state == 0:
                                self._surface = self.__image_right[round((self._currframes%20)/20)]
                        elif self._state == 1:
                                self._surface = self.__image_walk_right[self._currframes%self.__frames]
                        else:
                                self._surface = self.__image_jump_right[self._currframes%1]
                else:
                        if self._state == 0:
                                self._surface = self.__image_left[round((self._currframes%20)/20)]
                        elif self._state == 1:
                                self._surface = self.__image_walk_left[self._currframes%self.__frames]
                        else:
                                self._surface = self.__image_jump_left[self._currframes%1]
                

                

        def setImagedDirectionX(self, bool):
                self.__image_dirx = bool

        def switchImageDirectionX(self):
                self._surface = pygame.transform.flip(self._surface, True, False)

        def getImageDir(self):
                return self.__image_dirx

if __name__ == "__main__":
        from window import Window
        pygame.init()

        WINDOW = Window("image sprite")

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                WINDOW.clearScreen()
                WINDOW.updateFrame()
