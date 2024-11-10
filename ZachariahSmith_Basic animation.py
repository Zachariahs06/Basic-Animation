import pygame
import sys

def main():
    # Initialize pygame
    pygame.init()

    # Display setup
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Character with Background")

    # Load and scale the background image
    background_image = pygame.image.load("terrain_atlas.png")  # Ensure this file exists in the same directory
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Load and scale the character image
    character = pygame.image.load("sprite_base.png")
    character = character.convert_alpha()  # Handle transparency
    character = pygame.transform.scale(character, (100, 100))  # Scale character image

    # Set up character variables
    character_x = 320  # Center horizontally
    character_y = 0    # Start from the top of the screen
    character_speed = 5 # Speed of movement

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        # Control the frame rate
        clock.tick(30)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update character position
        character_y += character_speed
        if character_y > screen_height:
            character_y = 0  # Reset to the top if it goes off-screen

        # Refresh the screen
        screen.blit(background_image, (0, 0))  # Draw the background image
        screen.blit(character, (character_x, character_y))  # Draw the character
        pygame.display.flip()  # Update the display

    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
