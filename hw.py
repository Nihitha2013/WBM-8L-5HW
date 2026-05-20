import pygame
import random
from pygame import mixer

pygame.init()
screen_W, screen_H = 500, 500
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissors")

WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
font = pygame.font.Font(None, 40)

start_button = pygame.Rect(200, 150, 200, 80)
rock_button = pygame.Rect(50, 150, 150, 80)
paper_button = pygame.Rect(225, 150, 150, 80)
scissors_button = pygame.Rect(400, 150, 150, 80)

start_screen = True
result = ""
user_choice = ""
computer_choice = ""

def get_result(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"
background=pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (screen_W, screen_H)
)
mixer.music.load("relaxing-music-no15-273631.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen:
                if start_button.collidepoint(event.pos):
                    start_screen = False
            else:
                if rock_button.collidepoint(event.pos):
                    user_choice = "Rock"
                elif paper_button.collidepoint(event.pos):
                    user_choice = "Paper"
                elif scissors_button.collidepoint(event.pos):
                    user_choice = "Scissors"

                if user_choice:
                    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                    result = get_result(user_choice, computer_choice)

    if start_screen:
        pygame.draw.rect(screen, BLUE, start_button)
        screen.blit(font.render("START", True, WHITE), (start_button.x + 60, start_button.y + 25))
    else:
        pygame.draw.rect(screen, GREEN, rock_button)
        pygame.draw.rect(screen, GREEN, paper_button)
        pygame.draw.rect(screen, GREEN, scissors_button)

        screen.blit(font.render("Rock", True, BLACK), (rock_button.x + 40, rock_button.y + 25))
        screen.blit(font.render("Paper", True, BLACK), (paper_button.x + 40, paper_button.y + 25))
        screen.blit(font.render("Scissors", True, BLACK), (scissors_button.x + 20, scissors_button.y + 25))
        
        if result:
            screen.blit(font.render(f"You: {user_choice}", True, BLACK), (50, 300))
            screen.blit(font.render(f"Computer: {computer_choice}", True, BLACK), (50, 330))
            screen.blit(font.render(result, True, RED if "Lose" in result else (0, 150, 0)), (250, 270))

    pygame.display.flip()

pygame.quit()