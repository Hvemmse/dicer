
''' This is a images/dice game, programmet in python. only to se if it is possible.

'''

import pygame
import random
import time


# Initialize Pygame
pygame.init()
# Set up the screen
# assigning values to X and Y variable
X = 200
Y = 200

screen_size = (X, Y)
screen = pygame.display.set_mode(screen_size)

# Create a dictionary mapping images/dice values to images/dice images
dice_images = {
    1: pygame.image.load("images/dice1.png"),
    2: pygame.image.load("images/dice2.png"),
    3: pygame.image.load("images/dice3.png"),
    4: pygame.image.load("images/dice4.png"),
    5: pygame.image.load("images/dice5.png"),
    6: pygame.image.load("images/dice6.png"),
}
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

screen.fill(black)
pygame.display.set_caption('Klik | for | Kast')
counter = 0
while (counter) < 5:
    black = (0, 0, 0)
    screen.fill(black)
    pygame.display.flip()
    dice_value = random.randint(1,5)
    screen.blit(dice_images[dice_value], (70, 70))
    pygame.display.flip()
    time.sleep(.4)
    counter = counter + .4

font = pygame.font.Font('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 12)
text = font.render("Velkommen til Terningkast", True,green,black)

textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
black = (0, 0, 0)
screen.fill(black)
font = pygame.font.Font('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 32)
screen.blit(text, textRect)


# Set up a font for displaying the images/dice value
font = pygame.font.Font(None, 36)

# Set up the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            black = (0, 0, 0)
            screen.fill(black)
            pygame.display.flip()
            dice_value = random.randint(1, 6)
            dice_text = font.render(str(dice_value), True, (0, 225, 175))
            screen.blit(dice_images[dice_value], (70, 70))
            screen.blit(dice_text, (150, 150))
            pygame.display.flip()

    # Redraw the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
