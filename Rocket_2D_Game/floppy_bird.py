import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Game settings
FPS = 60
GRAVITY = 0.25
FLAP_STRENGTH = -5
PIPE_SPEED = 3
PIPE_GAP = 150

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floppy Bird")
clock = pygame.time.Clock()

# Load assets
font = pygame.font.Font(None, 36)
rocket_image = pygame.image.load("rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (40, 30))  # Scale rocket image

# Load background images (these could be layers)
background_layer1 = pygame.image.load("background1.png")
background_layer1 = pygame.transform.scale(background_layer1, (SCREEN_WIDTH, SCREEN_HEIGHT))

background_layer2 = pygame.image.load("background2.png")
background_layer2 = pygame.transform.scale(background_layer2, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.width = 40
        self.height = 30
        self.angle = 0

    def flap(self):
        # This is the single flap action, it is now updated based on spacebar hold
        self.velocity = FLAP_STRENGTH

    def update(self, is_flapping):
        if is_flapping:
            self.velocity = FLAP_STRENGTH  # Apply flap force while space is held down

        self.velocity += GRAVITY
        self.y += self.velocity

        # Adjust angle based on velocity
        if self.velocity < 0:
            self.angle = max(-30, self.angle - 5)  # Tilt up
        else:
            self.angle = min(30, self.angle + 5)  # Tilt down

    def draw(self):
        rotated_image = pygame.transform.rotate(rocket_image, self.angle)
        screen.blit(rotated_image, (self.x, int(self.y)))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.width = 50

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, self.width, SCREEN_HEIGHT))

    def off_screen(self):
        return self.x + self.width < 0

# Check for collisions
def check_collision(bird, pipes):
    if bird.y < 0 or bird.y + bird.height > SCREEN_HEIGHT:
        return True
    for pipe in pipes:
        if (pipe.x < bird.x + bird.width < pipe.x + pipe.width or
                pipe.x < bird.x < pipe.x + pipe.width):
            if bird.y < pipe.height or bird.y + bird.height > pipe.height + PIPE_GAP:
                return True
    return False

# Game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH)]
    score = 0

    running = True
    game_over = False

    # Scrolling background position
    background_x1 = 0
    background_x2 = SCREEN_WIDTH

    while running:
        screen.fill(BLUE)

        # Parallax scrolling background
        background_x1 -= 1  # Layer 1 moves at normal speed
        background_x2 -= 2  # Layer 2 moves at a faster speed for effect

        # Reset the background position when it moves off-screen
        if background_x1 <= -SCREEN_WIDTH:
            background_x1 = SCREEN_WIDTH
        if background_x2 <= -SCREEN_WIDTH:
            background_x2 = SCREEN_WIDTH

        # Draw backgrounds (layer 1 and layer 2)
        screen.blit(background_layer1, (background_x1, 0))
        screen.blit(background_layer1, (background_x1 + SCREEN_WIDTH, 0))
        screen.blit(background_layer2, (background_x2, 0))
        screen.blit(background_layer2, (background_x2 + SCREEN_WIDTH, 0))

        is_flapping = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    is_flapping = True
                if event.key == pygame.K_r and game_over:
                    return True  # Flag to restart the game

        if not game_over:
            bird.update(is_flapping)  # Pass the flapping status to update method
            bird.draw()

            # Update pipes
            for pipe in pipes:
                pipe.update()
                pipe.draw()

            # Add new pipes
            if pipes[-1].x < SCREEN_WIDTH - 200:
                pipes.append(Pipe(SCREEN_WIDTH))

            # Remove off-screen pipes
            pipes = [pipe for pipe in pipes if not pipe.off_screen()]

            # Check for collisions
            if check_collision(bird, pipes):
                game_over = True

            # Display score
            score += 1 / FPS
        else:
            game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        score_text = font.render(f"Score: {int(score)}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Start screen
def start_screen():
    running = True
    while running:
        screen.fill(BLUE)
        title_text = font.render("Welcome to Floppy Bird!", True, WHITE)
        start_text = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

def main():
    start_screen()
    while True:
        if not game_loop():
            break  # Exit the loop if the game ends

if __name__ == "__main__":
    main()
