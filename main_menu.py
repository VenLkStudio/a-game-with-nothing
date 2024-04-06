import pygame
import sys

class Menu:
    def __init__(self, screen, items, x_coord=50, font_size=36, color=(255, 255, 255)):
        self.screen = screen
        self.items = items
        self.x_coord = x_coord
        self.font_size = font_size
        self.color = color
        self.selected_index = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Draw current menu
        for i, item in enumerate(self.items):
            font = pygame.font.Font("assets/fonts/JetBrainsMono-Medium.ttf", self.font_size)
            text_surface = font.render(item, True, self.color)
            text_rect = text_surface.get_rect(left=self.x_coord, top=self.screen.get_height() / 2 + i * 40)
            self.screen.blit(text_surface, text_rect)
            if i == self.selected_index:
                arrow_surface = font.render(">", True, self.color)
                arrow_rect = arrow_surface.get_rect(right=text_rect.left - 10, centery=text_rect.centery)
                self.screen.blit(arrow_surface, arrow_rect)
        pygame.display.flip()

    def move_up(self):
        self.selected_index = (self.selected_index - 1) % len(self.items)

    def move_down(self):
        self.selected_index = (self.selected_index + 1) % len(self.items)

    def get_selected_item(self):
        return self.items[self.selected_index]

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Main menu items
main_menu_items = ["Start", "Options", "Quit"]
# Options menu items
options_menu_items = ["Option 1", "Option 2", "Option 3"]

# Create main menu object
main_menu = Menu(screen, main_menu_items)
# Create options menu object
options_menu = Menu(screen, options_menu_items, x_coord=200)

# Flag indicating whether the options menu is shown
show_options_menu = False

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not show_options_menu:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    main_menu.move_up()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    main_menu.move_down()
                elif event.key == pygame.K_RETURN:
                    if main_menu.get_selected_item() == "Start":
                        print("Test")  # Action for "Start"
                    elif main_menu.get_selected_item() == "Options":
                        show_options_menu = True
                    elif main_menu.get_selected_item() == "Quit":
                        running = False  # Quit the game
            else:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    options_menu.move_up()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    options_menu.move_down()
                elif event.key == pygame.K_RETURN:
                    print(f"Selected option: {options_menu.get_selected_item()}")
                    show_options_menu = False  # Hide options menu and return to main menu

    # Draw menu
    if not show_options_menu:
        main_menu.draw()
    else:
        options_menu.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
