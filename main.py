# import necessary libraries
import pygame
import random


# settings
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

pygame.font.init()
score_font = pygame.font.SysFont("Comic Sans MS", 30)
score = 0

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialize pygame
pygame.init()

# setting up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# clock
clock = pygame.time.Clock()

# snake and food initialization
snake_pos = [[WIDTH // 2, HEIGHT // 2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True


# generating food
def generate_food() -> list:
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos


food_pos = generate_food()


# drawing on screen
def draw_objects() -> None:
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(
            win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE)
        )

    pygame.draw.rect(
        win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE)
    )
    # render the score
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    win.blit(score_text, (10, 10))  # position of the score
