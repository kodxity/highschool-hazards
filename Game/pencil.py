
from image_sprite import ImageSprite

class Pencil(ImageSprite):
    def __init__(self):
        super().__init__(name = "pencil", image_file_location="media/pencil.png", frames = 0, scale = 20)

    def move(self, dir):
        self.setDirX(dir)
        self.setX(self.getX() + self.getSpeed() * dir)
        self.setAnimation()

    def touchedEdge(self, max_width, max_height, min_width=0, min_height=0):
        # makes it so that sprites stop at the border
        if self.getX() > max_width - self.getWidth():
            return True
        if self.getX() < min_width:
            return True

        if self.getY() >= max_height - self.getHeight(): # touches the ground
            return True
 
        if self.getY() < min_height:
            return True
        
        return False

        self.__position = (self.__x, self.__y)