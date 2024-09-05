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
window = pygame.display.set_mode((WIDTH, HEIGHT))
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
