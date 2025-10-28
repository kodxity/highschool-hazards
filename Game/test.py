if __name__ == "__main__":
    import pygame
    from window import Window
    from window import Background
    from player import Player
    from platform import Platform
    from enemy import Enemy

    pygame.init()

    WINDOW = Window("Test", 800, 600, 30)
    BACKGROUND1 = Background("media/background.png")
    BACKGROUND2 = Background("media/background.png", BACKGROUND1.getWidth())

    PLAYER = Player()
    PLAYER.setSpeed(10)

    ENEMY = Enemy()
    ENEMY.setSpeed(9)
    ENEMY.setPosition(0, WINDOW.getVirtualHeight() - ENEMY.getHeight())

    PLATFORM = Platform()
    PLATFORM.setPosition(400,510)
    PLATFORM.setSpeed(7)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        BACKGROUND1.marquee(-BACKGROUND1.getWidth(), BACKGROUND2.getX() + BACKGROUND2.getWidth() - 5)
        BACKGROUND2.marquee(-BACKGROUND2.getWidth(), BACKGROUND1.getX() + BACKGROUND1.getWidth() - 5)

        PRESSED_KEYS = pygame.key.get_pressed()
        PLAYER.WASDmove(PRESSED_KEYS)
        PLAYER.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        ENEMY.move()
        ENEMY.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        PLATFORM.marqueeX(WINDOW.getVirtualWidth())
        if PLATFORM.isCollision(PLAYER.getWidth(), PLAYER.getHeight(), PLAYER.getPosition()):
            PLAYER.setPosition(PLAYER.getX(), PLATFORM.getY() - PLAYER.getHeight())
            PLAYER.marqueeX(PLATFORM.getSpeed() ,WINDOW.getVirtualWidth())
            PLAYER.isJumped()

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(BACKGROUND2.getSurface(), BACKGROUND2.getPosition())
        WINDOW.getScreen().blit(BACKGROUND1.getSurface(), BACKGROUND1.getPosition())
        WINDOW.getScreen().blit(PLATFORM.getSurface(), PLATFORM.getPosition())
        WINDOW.getScreen().blit(ENEMY.getSurface(), ENEMY.getPosition())
        WINDOW.getScreen().blit(PLAYER.getSurface(), PLAYER.getPosition())
        WINDOW.updateFrame()