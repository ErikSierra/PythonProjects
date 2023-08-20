import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 5
player_color = (255, 0, 0)

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3
enemy_color = (0, 0, 255)

# Set up the score
score = 0
score_font = pygame.font.Font(None, 36)

# Set up the game over message
game_over_font = pygame.font.Font(None, 72)

# Game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        score += 1
        enemy_speed += 0.1

    # Check for collisions
    if (enemy_x < player_x + player_width and enemy_x + enemy_width > player_x
            and enemy_y < player_y + player_height and enemy_y + enemy_height > player_y):
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
