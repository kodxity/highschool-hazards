import pygame
from colors import Color

class MySprite:
    """
    Abstract sprite class to build other sprites

    """

    def __init__(self, width=0, height=0, x=0, y=0, speed=5, color=Color.WHITE):
        self.__width = width
        self.__height = height
        self._dimensions = (self.__width, self.__height)  # partially protected as we use it in box.py
        self.__x = x
        self.__y = y
        self.__yvel = 0 # velocity
        self._jumped = False # bool whether player has jumped or not(jumping/gravity)
        self._running = False # is object currently running
        self._state = 0 # 0 = idle, 1 = moving, 2 = jumping
        
        self.__position = (self.__x, self.__y)
        self._color = color
        self._surface = pygame.Surface  # make partially avaliable
        self.__xspeed = speed
        self.__yspeed = speed
        self.__dir_x = 1
        self.__dir_y = 1
        self._currframes = 0
        self.__prevtime = 0


    def setprevtime(self, time):
        self.__prevtime = time
    def getprevtime(self):
        return self.__prevtime
    
    # Modifier Methods (setter methods)

    def marqueeX(self, max_x, min_x=0):
        # move x coordinate
        self.__x -= self.__xspeed # make it move in left direction

        
        if self.__x < min_x - self._surface.get_width():
            self.__x = max_x

        self.updatePosition()  # update position
    
        
    def WASDmove(self, pressed_keys):
        if pressed_keys[pygame.K_w] == True and self._jumped == False:
            # gravity
            self.__yvel = -15 # jumps high up
            self._jumped = True
   
        ran = 0
        if pressed_keys[pygame.K_a] == True:  # letter a on the Keyboard
            self.__xspeed = 13
            self.__x -= self.__xspeed
            
            self._running = True
            ran = 1
            self.__dir_x = -1
        if pressed_keys[pygame.K_s] == True:
            self.__y += self.__yspeed
        if pressed_keys[pygame.K_d] == True:  # letter d on the Keyboard
            self.__xspeed = 10
            self.__x += self.__xspeed

            self._running = True
            ran = 1
            self.__dir_x = 1
        
        if self._jumped == True:
            self._state = 2 
        elif pressed_keys[pygame.K_a] == True or pressed_keys[pygame.K_d] == True : # is not running
            self._state = 1 # running
        else:
            self._running = False
            self._state = 0 # reset back to idle

        self.dogravity()
        self.updatePosition()

    def dogravity(self):
        # add gravity(jumps high up, then slowly falls back down)
        self.__yvel += 1
        if self.__yvel > 10:
            self.__yvel = 10
        self.__y += self.__yvel

        if self.__y > 600 - self._surface.get_height(): # touches the ground
            self._jumped = False # can jump now
            self.__yvel = 0
            self.__y = 600- self._surface.get_height()

    def isJumped(self):
        self._jumped = not self._jumped

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        # makes it so that sprites stop at the border
        if self.__x > max_width - self._surface.get_width():
            self.__x = max_width - self._surface.get_width()
        if self.__x < min_width:
            self.__x = min_width

        if self.__y > max_height - self._surface.get_height(): # touches the ground
            self._jumped = False # can jump now
            self.__yvel = 0
            self.__y = max_height - self._surface.get_height()
 
        if self.__y < min_height:
            self.__y = min_height

        self.__position = (self.__x, self.__y)
  
    def setColor(self, new_color):
        """
        Set new color. This only changes the variable, it does not change the surface
        :param new_color: tuple
        :return: None
        """

        self._color = new_color
        self._surface.fill(self._color)

    def setX(self, x):  # set x position
        self.__x = x
        self.updatePosition()

    def setY(self, y):  # set y position
        self.__y = y
        self.updatePosition()

    def setDirX(self, dir_x):  # set x direction
        self.__dir_x = dir_x
        self.updatePosition()

    def setDirY(self, dir_y):  # set y direction
        self.__dir_y = dir_y
        self.updatePosition()

    def setSpeed(self, speed):
        self.__xspeed = speed
        self.__yspeed = speed

    def setPosition(self, x, y):  # set position of sprite
        self.__x = x
        self.__y = y
        self.updatePosition()

    def setYVelocity(self, value):
        self.__yvel = value

    def updatePosition(self):  # update position of sprite
        self.__position = (self.__x, self.__y)

    def setWidth(self, new_width):
        self.__width = new_width

    def updateDimensions(self):
        self._dimensions = (self.__width, self.__height)
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32)  # Create surface
        self._surface.fill(self._color)



    # Accessor Methods (getter methods)

    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self.__position

    def getX(self):  # get x coordinate
        return self.__x

    def getY(self):  # get y coordinate
        return self.__y

    def getWidth(self):  # get width of sprite
        return self._surface.get_width()

    def getHeight(self):  # get height of sprite
        return self._surface.get_height()

    def getDirX(self):
        return self.__dir_x

    def getSpeed(self):
        return self.__xspeed

    def getJumping(self):
        return self._jumped

    def getYVelocity(self):
        return self.__yvel
    def isCollision(self, width, height, pos):
        if pos[0] >= self.__x - width and pos[0] <= self.__x + self.getWidth() and pos[1] >= self.__y - height and pos[
            1] <= self.__y + self.getHeight():
            return True
        else:
            return False

    def angledCollision(self, width, height, position):
        #ball hits top or bottom of box
        if position[0] >= self.__x - width + 10 and position[0] <= self.__x + self.getWidth() - 10 \
        and position[1] >= self.__y - height and position[1] <= self.__y + self.getHeight():
            return "flats"
        #ball hits the sides of the box
        elif position[0] >= self.__x - width  and position[0] <= self.__x + self.getWidth() \
        and position[1] >= self.__y - height + 10 and position[1] <= self.__y + self.getHeight() - 10:
            return "sides"
        else: return False
