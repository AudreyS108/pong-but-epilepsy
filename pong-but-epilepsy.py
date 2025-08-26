#PLAN:
#1. Have main pong game which is functional {DONE}
#2. Add epilepsy effect by flashing the screen with random rgb colors {DONE}
#3. Add a "First to ___ points wins" system + game over screen declaring the winner. {DONE}
#4. Create a main menu to start game {DONE}
#5. Add Epilepsy and non epilepsy modes {DONE}
#6. Possibly add a "How to play" screen {DONE}
#7. Possibly add a pong bot with AI - single player {DONE}
#8. Optional: Add sound effects and music
#Thats it for now


import pygame
import sys
import random
from time import sleep

pygame.init()
# Setting up screen dimensions
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
screen.fill("black")
pygame.display.set_caption("Pong but epilepsy")
clock = pygame.time.Clock()

# da paddles
PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

p1score = 0
p2score = 0

ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

def MainMenu():
    font = pygame.font.SysFont("Arial", 60)
    fontsmall = pygame.font.SysFont("Arial", 30)

    while True:
        pygame.display.set_caption("Pong but epilepsy - Main Menu")
        screen.fill("black")

        MousePosition = pygame.mouse.get_pos()

        MenuText = font.render("Pong but epilepsy", True, "white")
        MenuRect = MenuText.get_rect(center=(width/2 + 20, 75))

        mx,my = pygame.mouse.get_pos()

        PlayButton = pygame.Rect(width/2 - 125, 150, 300, 55)
        ChaosPlayButton = pygame.Rect(width/2 - 125, 250, 300, 55)

        BotNormButton = pygame.Rect(width/2 - 125, 350, 300, 55)
        BotEpButton = pygame.Rect(width/2 - 125, 450, 300, 55)

        HowToplaybutton = pygame.Rect(width/2 - 125, 550, 300, 55)
        QuitButton = pygame.Rect(width/2 - 125, 650, 300, 55)


        playbuttontext = fontsmall.render("Play Normal Mode", True, "black")
        chaosbuttontext = fontsmall.render("Play Epilepsy Mode", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        BotNormText = fontsmall.render("Normal Bot Mode", True, "black")
        BotEptext = fontsmall.render("Epilepsy Bot Mode", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        HowToplaytext = fontsmall.render("How to Play", True, "black")
        quitbuttontext = fontsmall.render("Quit Game", True, "black")

        PBrect = playbuttontext.get_rect(center = ((width/2 + 25), 175))
        CBrect = playbuttontext.get_rect(center = ((width/2 + 20), 275))

        NormBrect = playbuttontext.get_rect(center = ((width/2 + 30), 375))
        EpBrect = playbuttontext.get_rect(center = ((width/2 + 25), 475))

        HTPBrect = playbuttontext.get_rect(center = ((width/2 + 60), 575))
        QBrect = playbuttontext.get_rect(center = ((width/2 + 70), 675))


        if PlayButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", PlayButton)
        else:
            pygame.draw.rect(screen, "white", PlayButton)

        if ChaosPlayButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", ChaosPlayButton)
        else:
            pygame.draw.rect(screen, "white", ChaosPlayButton)
    
        if BotNormButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", BotNormButton)
        else:
            pygame.draw.rect(screen, "white", BotNormButton)

        if BotEpButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", BotEpButton)
        else:
            pygame.draw.rect(screen, "white", BotEpButton)

        if HowToplaybutton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", HowToplaybutton)
        else:
            pygame.draw.rect(screen, "white", HowToplaybutton)

        if QuitButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", QuitButton)
        else:
            pygame.draw.rect(screen, "white", QuitButton)
  
        screen.blit(MenuText, MenuRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #detects when mouse button is down runs through buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayButton.collidepoint(event.pos):
                    play()
                elif ChaosPlayButton.collidepoint(event.pos):
                    chaosplay()
                elif BotNormButton.collidepoint(event.pos):
                    botnorm()
                elif BotEpButton.collidepoint(event.pos):
                    botEp()
                elif HowToplaybutton.collidepoint(event.pos):
                    howtoplay()
                elif QuitButton.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(playbuttontext, PBrect)
        screen.blit(chaosbuttontext, CBrect)
        screen.blit(BotNormText, NormBrect)
        screen.blit(BotEptext, EpBrect)
        screen.blit(HowToplaytext, HTPBrect)
        screen.blit(quitbuttontext, QBrect)

        pygame.display.update()
        clock.tick(200)

def play():
    global p1score
    global p2score

    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Normal Mode")

# da paddles
    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

    #Winning scores
        if p1score >= 10 or p2score >= 10:
            endscreen()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_s]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
        elif keyspressed[pygame.K_w]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2

    # Player Two controls
        if keyspressed[pygame.K_DOWN]:
            if PlayerTwo.bottom < height:
                PlayerTwo.top += 2 
        elif keyspressed[pygame.K_UP]:
            if PlayerTwo.top > 0:
                PlayerTwo.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-1, -2])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-1, 1])
            p2score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)

        if ball.x >= width: #right side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p1score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # normal mode
        screen.fill("black")

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player 1: " + str(p1score)), True, "white")
        p2text = font.render(str("Player 2: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)

def chaosplay():
    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Epilepsy Mode")

# da paddles

    global p1score
    global p2score

    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

        if p1score >= 10 or p2score >= 10:
            endscreen()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_w]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
        elif keyspressed[pygame.K_s]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2

    # Player Two controls
        if keyspressed[pygame.K_UP]:
            if PlayerTwo.bottom < height:
                PlayerTwo.top += 2 
        elif keyspressed[pygame.K_DOWN]:
            if PlayerTwo.top > 0:
                PlayerTwo.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-2, -1])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/234
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p2score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)

        if ball.x >= width: #right side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p1score += 1 #update the score
            print("Player 1 score:", p1score, ", Player 2 score:", p2score)
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # epilepsy mode:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player 1: " + str(p1score)), True, "white")
        p2text = font.render(str("Player 2: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)

def endscreen():
    
    global p1score
    global p2score
    
    font = pygame.font.SysFont("Arial", 60)
    screen.fill("black")

    winnertext = font.render("Player __ wins!", True, "white")
    print(p1score)
    print(p2score)
    
    # Display the winner
    if p1score >= 10:
        winnertext = font.render("Player 1 wins! (nice)", True, "white")
    elif p2score >= 10:
       winnertext = font.render("Player 2 wins! (lol)", True, "white")
    
    print(winnertext)

    winnerrect = winnertext.get_rect(center=(width/2, height/2 - 200))
    
    # Display the final scores
    scoretext = font.render(f"Final Score - Player 1: {p1score}, Player 2: {p2score}", True, "white")
    scorerect = scoretext.get_rect(center=(width/2, height/2 + 50))

    SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
    Spacerect = SpaceText.get_rect(center=(width/2, height - 100))

    screen.blit(winnertext, winnerrect)
    screen.blit(scoretext, scorerect)
    screen.blit(SpaceText, Spacerect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()

def endscreen2():
     
    global p1score
    global p2score
    
    font = pygame.font.SysFont("Arial", 60)
    screen.fill("black")

    winnertext = font.render("Player __ wins!", True, "white")
    print(p1score)
    print(p2score)
    
    # Display the winner
    if p1score >= 10:
        winnertext = font.render("Player wins! (W IN THE CHAT)", True, "white")
    elif p2score >= 10:
       winnertext = font.render("Bot wins! (haha imagine)", True, "white")
    
    print(winnertext)

    winnerrect = winnertext.get_rect(center=(width/2, height/2 - 200))
    
    # Display the final scores
    scoretext = font.render(f"Final Score - Player: {p1score}, Bot: {p2score}", True, "white")
    scorerect = scoretext.get_rect(center=(width/2, height/2 + 50))

    SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
    Spacerect = SpaceText.get_rect(center=(width/2, height - 100))

    screen.blit(winnertext, winnerrect)
    screen.blit(scoretext, scorerect)
    screen.blit(SpaceText, Spacerect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()

def howtoplay():
    font = pygame.font.SysFont("Arial", 30)
    
    
    screen.fill("black")

    Text = font.render("The aim of the game is to score points by deflecting the ball with your paddle better than your opponent.", True, "white")
    rect = Text.get_rect(center=(width/2, height - 650))

    NormText = font.render("In Normal mode:", True, "white")
    Normrect = NormText.get_rect(center=(width/2, height - 550))

    NormTextTwo = font.render("Press UP or W to go up, and DOWN or S to go down.", True, "white")
    NormrectTwo = NormTextTwo.get_rect(center=(width/2, height - 500))

    EpModeText = font.render("In Epilepsy mode the controls are reversed:", True, "white")
    EpModerect = EpModeText.get_rect(center=(width/2, height - 450))

    EpModeTextOne = font.render("Press UP or W to go down, and DOWN or S to go up.", True, "white")
    EpModerectOne = EpModeTextOne.get_rect(center=(width/2, height - 350))

    EpModeTextTwo = font.render("(This is just to make you rage more lol)", True, "white")
    EpModerectTwo = EpModeTextTwo.get_rect(center=(width/2, height - 300))

    EpModeTextThree = font.render("First to score 10 points wins!", True, "white")
    EpModerectThree = EpModeTextThree.get_rect(center=(width/2, height - 200))

    SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
    Spacerect = SpaceText.get_rect(center=(width/2, height - 100))

    screen.blit(NormText, Normrect)
    screen.blit(NormTextTwo, NormrectTwo)
    screen.blit(EpModeText, EpModerect)
    screen.blit(EpModeTextTwo, EpModerectTwo)
    screen.blit(EpModeTextOne, EpModerectOne)
    screen.blit(EpModeTextThree, EpModerectThree)
    screen.blit(SpaceText, Spacerect)

    screen.blit(Text, rect) 

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()

def botnorm():
    global p1score
    global p2score

    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Normal Mode")

# da paddles
    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

    #Winning scores
        if p1score >= 10 or p2score >= 10:
            endscreen2()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_s]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 
        elif keyspressed[pygame.K_w]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-1, -2])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-1, 1])
            p2score += 1 #update the score
            print("Player score:", p1score, ", Bot score:", p2score)

        if ball.x >= width: #right side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p1score += 1 #update the score
            print("Player score:", p1score, ", Bot score:", p2score)
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    # BOT CONTROLS:
        if PlayerTwo.y < ball.y:
            PlayerTwo.top += 2.3
        if PlayerTwo.y > ball.y:
            PlayerTwo.bottom -= 2.3

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # normal mode
        screen.fill("black")

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player: " + str(p1score)), True, "white")
        p2text = font.render(str("Bot: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)

def botEp():
    global p1score
    global p2score

    font = pygame.font.SysFont("Arial", 30)

    pygame.display.set_caption("Pong but epilepsy - Normal Mode")

# da paddles
    PlayerOne = pygame.Rect(110, (height/2) - 50, 10, 100)
    PlayerTwo = pygame.Rect(width - 110, (height/2) - 50, 10, 100)

#Player scores
    p1score = 0
    p2score = 0

    ball = pygame.Rect((width/2) - 10, (height/2) - 10, 20, 20)
    xspeed, yspeed = random.choice([-1, 1]), random.choice([-1, 1])

    while True:
    
    # --------Quit Pygame window--------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                MainMenu()
    #--- end pygame window quit

    #Winning scores
        if p1score >= 10 or p2score >= 10:
            endscreen2()

    # --------Paddle movement!----------

        keyspressed = pygame.key.get_pressed()

    # Player One controls
        if keyspressed[pygame.K_w]:
            if PlayerOne.bottom < height:
                PlayerOne.top += 2 # Flipped controls contrary to real world logistics: designed to be extra confusing
        elif keyspressed[pygame.K_s]:
            if PlayerOne.top > 0:
                PlayerOne.bottom -= 2
    
    # --------Ball physics------------
        if ball.y >= height:
            yspeed = random.choice([-1, -2])
        if ball.y <= 0:
            yspeed = random.choice([1, 2])

        if ball.x <= 0: #Left side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-1, 1])
            p2score += 1 #update the score
            print("Player score:", p1score, ", Bot score:", p2score)

        if ball.x >= width: #right side
            ball.center = width/2, height/2
            xspeed = random.choice([-1, 1])
            yspeed =  random.choice([-2, -1, 1, 2])
            p1score += 1 #update the score
            print("Player score:", p1score, ", Bot score:", p2score)
    
        if ball.colliderect(PlayerOne) and ball.x < PlayerOne.right:
            xspeed = 1
        if ball.colliderect(PlayerTwo) and ball.x < PlayerTwo.left:
            xspeed = -1

        ball.x += xspeed * 1.4
        ball.y += yspeed * 1.4

    # BOT CONTROLS:
        if PlayerTwo.y < ball.y:
            PlayerTwo.top += 2.3
        if PlayerTwo.y > ball.y:
            PlayerTwo.bottom -= 2.3

    #------------SCREEN FILLS:-----------
    # Screen must be filled to prevent any weird trails
    # normal mode
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # ----------SCORES DISPLAY-----------
        scoreboardtext = font.render("Scoreboard", True, "white")
        p1text = font.render(str("Player: " + str(p1score)), True, "white")
        p2text = font.render(str("Bot: " + str(p2score)), True, "white")
    
        scoreboardrect = scoreboardtext.get_rect(center=(width/2, 50))
        p1_rect = p1text.get_rect(center=(width/2 - 200, 80))
        p2_rect = p2text.get_rect(center=(width/2 + 200, 80))

        SpaceText = font.render("Press SPACE to return to the main menu", True, "white")
        Spacerect = SpaceText.get_rect(center=(width/2, height - 100))


    # draw the player paddles
        pygame.draw.rect(screen, "white", PlayerOne)
        pygame.draw.rect(screen, "white", PlayerTwo)
        pygame.draw.circle(screen, "white", ball.center, 10)

        screen.blit(p1text, p1_rect)
        screen.blit(p2text, p2_rect)
        screen.blit(scoreboardtext, scoreboardrect)
        screen.blit(SpaceText, Spacerect)

        pygame.display.update()
    # clock.tick : Frames per second
        clock.tick(300)


MainMenu()
