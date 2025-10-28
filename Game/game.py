import random

if __name__ == "__main__":
    # classes
    import pygame
    from window import Window
    from window import Background
    from window import Box
    from player import Player
    from platform import Platform
    from enemy import Enemy
    from text import Text
    from pencil import Pencil
    import colors

    pygame.init()
    

    start_screen = True
    end_screen = False


    WINDOW = Window("Test", 800, 600, 30)
    BACKGROUND1 = Background("media/background.png")
    BACKGROUND2 = Background("media/background.png", BACKGROUND1.getWidth())
    #2 background sprites allow for smooth looping

    START_TEXT = Text("Press 'ENTER' To Start")
    START_TEXT.setPosition(WINDOW.getVirtualWidth()//2 - START_TEXT.getWidth()//2, 400)

    end_text_messages = ["Don't Try And Tackle Too Much Work At Once, You'll Get Burnt Out", "Try And Find A Good School To Life Balance",
                         "Remember, School Isn't Everything, Try Going Out With Friends Every Once In A While", "Grades Aren't Everything, Make Some New Connections"]

    message_num = 0
    END_TEXT = Text(end_text_messages[message_num], font_size= 20)
    END_TEXT.setPosition(WINDOW.getVirtualWidth() // 2 - END_TEXT.getWidth() // 2, 400)

    score = 0
    seconds = 1
    SCORE = Text(f"SCORE: {score}")
    SCORE.setPosition(500, 25)

    PLAYER = Player()
    PLAYER.setSpeed(10)
    PLAYER.setScale(0.5)
    PLAYER.setUpWASDmove()
    ENEMY = Enemy("teacher")
    ENEMY.setSpeed(9)
    ENEMY.setPosition(0, WINDOW.getVirtualHeight() - ENEMY.getHeight())
    wsarr = []
    wsactive = []
    examarr = []
    examactive = []
    examdir = []
    pencilarr = []
    pencilactive = []
    pencildir = []
    STRESS_BAR = Box(1, 10)
    STRESS_BAR.setPosition(50, 50)
    STRESS_BAR.setColor(colors.Color.BLUE)

    PLATFORMS = []
    row = 1
    column = 1
    for i in range(10):
        PLATFORMS.append(Platform())

    PLATFORMS[0].setPosition(80, 330)
    PLATFORMS[1].setPosition(720, 330)
    PLATFORMS[2].setPosition(80, 510)
    PLATFORMS[3].setPosition(720, 510)
    PLATFORMS[4].setPosition(400, 420)
    PLATFORMS[5].setPosition(1040, 420)
    PLATFORMS[6].setPosition(400, 240)
    PLATFORMS[7].setPosition(1040,240)
    PLATFORMS[8].setPosition(80, 150)
    PLATFORMS[9].setPosition(720, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        time =  pygame.time.get_ticks() / 1000
        print(time)

        while end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            START_TEXT.setPosition(WINDOW.getVirtualWidth()//2 - START_TEXT.getWidth()//2, 200)

            PRESSED_KEYS = pygame.key.get_pressed()
            if PRESSED_KEYS[pygame.K_RETURN] == True:
                end_screen = False
                start_screen = True

            if PRESSED_KEYS[pygame.K_SPACE] == True:
                if message_num == len(end_text_messages) - 1:
                    message_num = 0
                else:
                    message_num +=1
                    END_TEXT.updateText(end_text_messages[message_num])
                    END_TEXT.setPosition(WINDOW.getVirtualWidth() // 2 - END_TEXT.getWidth() // 2, 400)
                    
                print(message_num)
                    

            WINDOW.clearScreen()
            WINDOW.getScreen().blit(BACKGROUND1.getSurface(), BACKGROUND1.getPosition())
            WINDOW.getScreen().blit(BACKGROUND2.getSurface(), BACKGROUND2.getPosition())
            WINDOW.getScreen().blit(SCORE.getSurface(), SCORE.getPosition())
            WINDOW.getScreen().blit(END_TEXT.getSurface(), END_TEXT.getPosition())
            WINDOW.getScreen().blit(START_TEXT.getSurface(), START_TEXT.getPosition())
            WINDOW.updateFrame()


        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PLAYER.setStress(1)
            score = 0
            PLAYER.setPosition(0,0)
            ENEMY.setPosition(0, WINDOW.getVirtualHeight() - ENEMY.getHeight())

            PRESSED_KEYS = pygame.key.get_pressed()
            if PRESSED_KEYS[pygame.K_RETURN] == True:
                start_screen = False

            WINDOW.clearScreen()
            WINDOW.getScreen().blit(BACKGROUND1.getSurface(), BACKGROUND1.getPosition())
            WINDOW.getScreen().blit(BACKGROUND2.getSurface(), BACKGROUND2.getPosition())
            WINDOW.getScreen().blit(START_TEXT.getSurface(), START_TEXT.getPosition())
            WINDOW.updateFrame()

        BACKGROUND1.marquee(-BACKGROUND1.getWidth(), BACKGROUND2.getX() + BACKGROUND2.getWidth() - 5)
        BACKGROUND2.marquee(-BACKGROUND2.getWidth(), BACKGROUND1.getX() + BACKGROUND1.getWidth() - 5)

        PRESSED_KEYS = pygame.key.get_pressed()
      
        PLAYER.WASDmove(PRESSED_KEYS)
        
            
        # PLAYER.setRunningAnimation()
        if not PLAYER.getImageDir():
            PLAYER.setSpeed(13)
        else:
            PLAYER.setSpeed(10)
        PLAYER.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        if PRESSED_KEYS[pygame.K_e] == True: # press S to shoot projectile
            if time - PLAYER.getprevtime() >= 1:
                PLAYER.setprevtime(time) 
                PENCIL = Pencil()
                PENCIL.setSpeed(10)
                PENCIL.setPosition(PLAYER.getX(), PLAYER.getY())
                pencilarr.append(PENCIL)
                pencilactive.append(1)
                pencildir.append(PLAYER.getDirX())        #makes enemy move back and forth
        ENEMY.move()
        ENEMY.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        if time - ENEMY.getprevtime() >= 5: 
            prob = random.randrange(1,4) # choose int from 1 - 3
            ENEMY.setprevtime(time)
            if prob == 1: # 33% chance its an exam
                ENEMYEXAM = Enemy("exam")

                ENEMYEXAM.setPosition(ENEMY.getX(), ENEMY.getY())
                ENEMYEXAM.propel()
                examarr.append(ENEMYEXAM)
                examactive.append(1) # currently active 
            else:
                ENEMYWS = Enemy("worksheet")

                ENEMYWS.setPosition(ENEMY.getX(), ENEMY.getY())
                ENEMYWS.propel()
                wsarr.append(ENEMYWS)
                wsactive.append(1) # currently active 
        for i in range(len(pencilarr)):
            PENCIL = pencilarr[i]
            PENCIL.dogravity()
            PENCIL.move(pencildir[i]) # move in players direction
            PENCIL.rotateImage(pencildir[i])
            PENCIL.updatePosition()
            if PENCIL.touchedEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight()) == True:
                pencilactive[i] = 0
  
        for i in range(len(wsarr)):
            if wsactive[i] == 1:
                ENEMYWS = wsarr[i]
                ENEMYWS.dogravity()
                ENEMYWS.updatePosition()
                if(ENEMYWS.getY() == WINDOW.getVirtualHeight() - ENEMYWS.getHeight()):
                    ENEMYWS.setX(ENEMYWS.getX() - PLATFORMS[0].getSpeed()) # stays on platform until it disappears
                    ENEMYWS.setAnimation()
                
                if ENEMYWS.isCollision(PLAYER.getWidth(), PLAYER.getHeight(), PLAYER.getPosition()) and PLAYER.getIFrames() == 0:
                    PLAYER.addStress(100)
                    wsactive[i] = 0
                    
                for j in range(len(pencilarr)):
                    PENCIL = pencilarr[j]
                    if pencilactive[j] == 1 and ENEMYWS.isCollision(PENCIL.getWidth(), PENCIL.getHeight(), PENCIL.getPosition()):
                        # make both disappear
                        pencilactive[j]=0
                        wsactive[i]=0
        # ene,y collision physics
        if ENEMY.isCollision(PLAYER.getWidth(), PLAYER.getHeight(), PLAYER.getPosition()) and PLAYER.getIFrames() == 0:
            PLAYER.addStress(100)

        STRESS_BAR.setWidth(PLAYER.getStress())
        STRESS_BAR.updateDimensions()
        PLAYER.IFrameCountdown()
        PLAYER.countDown()

        if PLAYER.getStress() >= 300:
            end_screen = True

        #platform physics
        for PLATFORM in PLATFORMS:
            PLATFORM.marqueeX(WINDOW.getVirtualWidth() + 250)
            if PLATFORM.isCollision(PLAYER.getWidth(), PLAYER.getHeight(), PLAYER.getPosition()):
                PLAYER.setPosition(PLAYER.getX(), PLATFORM.getY() - PLAYER.getHeight())
                PLAYER.marqueeX(PLATFORM.getSpeed(), WINDOW.getVirtualWidth())
                PLAYER._jumped = False
            for i in range(len(wsarr)):
                ENEMYWS = wsarr[i]
                if ENEMYWS.getYVelocity() >= 0 and PLATFORM.isCollision(ENEMYWS.getWidth(), ENEMYWS.getHeight(), ENEMYWS.getPosition()):
                    ENEMYWS.setAnimation()
                    ENEMYWS.setYVelocity(0)
                    ENEMYWS.setPosition(ENEMYWS.getX(), PLATFORM.getY() - ENEMYWS.getHeight())
                    ENEMYWS.setX(ENEMYWS.getX() - PLATFORM.getSpeed()) # stays on platform until it disappears
                    ENEMYWS._jumped = False

        #awards player with points every second
        if not end_screen:
            if int(time) == seconds:
                score += 5
                seconds += 1
            print(score, seconds)

            SCORE.updateText(f"SCORE: {score}")

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(BACKGROUND2.getSurface(), BACKGROUND2.getPosition())
        WINDOW.getScreen().blit(BACKGROUND1.getSurface(), BACKGROUND1.getPosition())
        for PLATFORM in PLATFORMS:
            WINDOW.getScreen().blit(PLATFORM.getSurface(), PLATFORM.getPosition())
        for i in range(len(wsarr)):
            if wsactive[i] == 1:
                WINDOW.getScreen().blit(wsarr[i].getSurface(), wsarr[i].getPosition())
        for i in range(len(pencilarr)):
            if pencilactive[i] == 1:
                WINDOW.getScreen().blit(pencilarr[i].getSurface(), pencilarr[i].getPosition())
        WINDOW.getScreen().blit(ENEMY.getSurface(), ENEMY.getPosition())
        WINDOW.getScreen().blit(PLAYER.getSurface(), PLAYER.getPosition())
        WINDOW.getScreen().blit(STRESS_BAR.getSurface(), STRESS_BAR.getPosition())
        WINDOW.getScreen().blit(SCORE.getSurface(), SCORE.getPosition())
        WINDOW.updateFrame()