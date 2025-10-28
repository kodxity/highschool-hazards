import random

from image_sprite import ImageSprite


platform_sprites = ["media/platform.png", "media/platform2.png", "media/platform3.png"]

class Platform(ImageSprite):
    def __init__(self):
        num = random.randrange(0, 3)
        sprite_image = platform_sprites[num]
        super().__init__("platform", image_file_location=sprite_image, frames = 1, scale = 100)

    def isCollision(self, width, height, pos):
        if pos[0] >= self.getX() - width + 10 and pos[0] <= self.getX() + self.getWidth() \
            and pos[1] + height >= self.getY() and pos[1] + height <= self.getY() + 10:
            return True
        else: return None