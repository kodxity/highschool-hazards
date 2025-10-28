
from my_sprite import MySprite
from colors import Color
import pygame

class Text(MySprite):

    def __init__(self, text, font_family = "Arial", font_size = 36, x = 0, y = 0, color = Color.WHITE):
        MySprite.__init__(self, x = x, y = y)
        self.__text = text
        self.__font_family = font_family
        self.__font_size = font_size
        self.__font = pygame.font.SysFont(self.__font_family, self.__font_size)
        self._surface = self.__font.render(self.__text, True, self._color)
        self.color = color

    def updateText(self, text):
        self.__text = text
        self._surface = self.__font.render(self.__text, True, self._color)

    def setTextColor(self, color: tuple):
        self.__color = color
        self.__surface = self.__font.render(self.__text, True, self.__color)

if __name__ == "__main__":
    from window import  Window
    pygame.init()

    WINDOW = Window("Inheritance")
    TEXT = Text("Inheritance Example")
    TEXT.setPosition(100, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()
        TEXT.WASDmove(PRESSED_KEYS)
        #TEXT.wrapEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        TEXT.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        #TEXT.marqueeX(WINDOW.getVirtualWidth())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT.getSurface(), TEXT.getPosition())
        WINDOW.updateFrame()
