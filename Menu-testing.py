import pygame
import sys
import random

pygame.init()
# Setting up screen dimensions
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

def play():
    screen.fill("black")

def MainMenu():
    while True:
        pygame.display.set_caption("Pong but epilepsy - Main Menu")
        screen.fill("black")

        MousePosition = pygame.mouse.get_pos()

        MenuText = font.render("Pong but epilepsy", True, "white")
        MenuRect = MenuText.get_rect(center=(width/2, 100))

        mx,my = pygame.mouse.get_pos()

        PlayButton = pygame.Rect(width/2 - 100, 200, 200, 50)
        QuitButton = pygame.Rect(width/2 - 100, 400, 200, 50)

        if PlayButton.collidepoint(mx, my):
            pygame.draw.rect(screen, "grey", PlayButton)
        else:
            pygame.draw.rect(screen, "white", PlayButton)

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
                if PlayButton.collidepoint(MousePosition):
                    play()
                elif QuitButton.collidepoint(MousePosition):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(200)

MainMenu()
    