import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Side-Scroller Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the player
player_radius = 25
player_x = player_radius
player_y = screen_height / 2
player_speed = 5
player_gravity = 1

# Set up the obstacles
obstacle_width = 50
obstacle_height = random.randint(100, 400)
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height
obstacle_speed = 5

# Set up the score
score = 0

# Main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Apply gravity to the player
    player_y += player_gravity

    # Check for collision with the top or bottom of the screen
    if player_y - player_radius < 0:
        player_y = player_radius
    elif player_y + player_radius > screen_height:
        player_y = screen_height - player_radius

    # Move the obstacle
    obstacle_x -= obstacle_speed

    # Check for collision with the player
    if obstacle_x < player_x + player_radius and obstacle_x + obstacle_width > player_x - player_radius and \
            obstacle_y < player_y + player_radius and obstacle_y + obstacle_height > player_y - player_radius:
        running = False

    # Check if the obstacle has gone off the screen
    if obstacle_x < -obstacle_width:
        obstacle_x = screen_width
        obstacle_height = random.randint(100, 400)
        obstacle_y = screen_height - obstacle_height
        score += 1

    # Draw the screen
    screen.fill(white)
    pygame.draw.circle(screen, red, (int(player_x), int(player_y)), player_radius)
    pygame.draw.rect(screen, black, (int(obstacle_x), int(obstacle_y), obstacle_width, obstacle_height))
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

