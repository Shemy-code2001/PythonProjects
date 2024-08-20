import pygame
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball settings
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7 * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)
ball_speed_y = 7 * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)

# Paddle settings
paddle_width, paddle_height = 10, 140
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player_speed = 0
opponent_speed = 7

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Paddle collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Player movement
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

    # Opponent movement
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)
