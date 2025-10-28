
import pygame
from colors import Color
from my_sprite import MySprite

class Window:
    '''
    Create the window that will load for pygame
    '''

    def __init__(self, title, width = 800, height = 600, fps = 30):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__dimension = (self.__width, self.__height)
        self.__fps = fps
        #self.__bg_color = Color.GREY #drak grey
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(self.__dimension)
        self.__screen.fill((0,0,0))
        pygame.display.set_caption(self.__title)

    def updateFrame(self):
        self.__clock.tick(self.__fps)
        pygame.display.flip()

    def clearScreen(self):
        self.__screen.fill((0,0,0))


    #accessor methods
    def getScreen(self):
        return self.__screen

    def getVirtualWidth(self):
        return self.__width

    def getVirtualHeight(self):
        return self.__height

class Background:
    def __init__(self, image_file, x = 0, y = 0, speed = 4):
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)
        self.__speed = speed
        self._surface = pygame.Surface  # one underscore makes it partially private (subclasses can access)
        self.__file_location = image_file
        self._surface = pygame.image.load(self.__file_location).convert_alpha()

    def setScale(self, scale_x, scale_y=None):
        if scale_y == None:
            scale_y = scale_x
        self._surface = pygame.transform.scale(self._surface, (self.getWidth() * scale_x, self.getHeight() * scale_y))

    def marquee(self, min_width, wrap):
        self.__x -= self.__speed

        if self.__x <= min_width:
            self.__x = wrap

        self.__position = (self.__x, self.__y)

    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self.__position

    def getWidth(self):
        return self.getSurface().get_width()

    def getHeight(self):
        return self.getSurface().get_height()

    def getX(self):
        return self.__x


class Box(MySprite): # class for rectangles

    def __init__(self, width = 1, height = 1):
        MySprite.__init__(self, width=width,height = height) # inherit from Mysprite
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32) # Create surface
        self._surface.fill(self._color) # fill it with its color(default white)




if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("template", 800, 600, 30)
    BACKGROUND1 = Background("media/background.png")
    BACKGROUND2 = Background("media/background.png", BACKGROUND1.getWidth())

    player = Box(75,115)
    player.setSpeed(10)
    player.setPosition(30,400)
    platform = Box(200,30)
    platform.setPosition(400,500)
    while True:
        #pygame retrieves all inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        BACKGROUND1.marquee(-BACKGROUND1.getWidth(), BACKGROUND2.getX() + BACKGROUND2.getWidth() - 5)
        BACKGROUND2.marquee(-BACKGROUND2.getWidth(), BACKGROUND1.getX() + BACKGROUND1.getWidth() - 5)

        key_pressed = pygame.key.get_pressed()
        player.WASDmove(key_pressed)
        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        platform.marqueeX(WINDOW.getVirtualWidth())
        if platform.angledCollision(player.getWidth(),player.getHeight(), player.getPosition()) == "flats":
            player.setPosition(player.getX(), platform.getY() - player.getHeight())
            player.isJumped()
        if platform.angledCollision(player.getWidth(), player.getHeight(), player.getPosition()) == "sides":
            player.setPosition(platform.getX() - player.getWidth(), player.getY())

        WINDOW.clearScreen()
        # background
        WINDOW.getScreen().blit(BACKGROUND2.getSurface(), BACKGROUND2.getPosition())
        WINDOW.getScreen().blit(BACKGROUND1.getSurface(), BACKGROUND1.getPosition())
        # character
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.getScreen().blit(platform.getSurface(),platform.getPosition())
        # platform
        WINDOW.updateFrame()