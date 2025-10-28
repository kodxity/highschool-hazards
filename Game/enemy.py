
from image_sprite import ImageSprite
import random
class Enemy(ImageSprite):
    def __init__(self, name):

        super().__init__(f"enemy{name}", image_file_location=f"media/enemy{name}.png", frames = 1, scale = 100)
        self.__name = name
        
    def propel(self):
        # propel itself upwards
        self.setYVelocity(random.randrange(-30,-15))
    def move(self):
        if self.getImageDir():
            self.setX(self.getX() + self.getSpeed())
        else:
            self.setX(self.getX() - self.getSpeed())

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.getX() > max_width - self.getWidth():
            self.setImagedDirectionX(False)
            self.switchImageDirectionX()
        if self.getX() < min_width:
            self.setImagedDirectionX(True)
            self.switchImageDirectionX()
