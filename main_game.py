import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
FPS = 60
FONT_SIZE = 36

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Шрифт для отображения текста
font = pygame.font.Font("assets/fonts/JetBrainsMono-Medium.ttf", FONT_SIZE)

# Список пунктов меню
menu_items = ["Start", "Options", "Quit", "TESTITEM", "TESTITEM", "TESTITEM", "TESTITEM", "TESTITEM", "TESTITEM", "TESTITEM", "TESTITEM"]
selected_item = menu_items[0]  # Изначально выбран первый пункт

# Функция отрисовки меню
def draw_menu():
    screen.fill(BLACK)
    for i, item in enumerate(menu_items):
        color = WHITE if item != selected_item else WHITE  # Инвертируем цвет выбранного элемента
        text_surface = font.render(item, True, color)
        text_rect = text_surface.get_rect(left=50, top=SCREEN_HEIGHT / 2 + i * FONT_SIZE)
        screen.blit(text_surface, text_rect)
        
        if item == selected_item:
            arrow_surface = font.render(">", True, WHITE)
            arrow_rect = arrow_surface.get_rect(right=text_rect.left - 10, centery=text_rect.centery)
            screen.blit(arrow_surface, arrow_rect)
    
    pygame.display.flip()

# Основной цикл программы
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                index = menu_items.index(selected_item)
                selected_item = menu_items[(index - 1) % len(menu_items)]
                print(f'Selected button: {selected_item}')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                index = menu_items.index(selected_item)
                selected_item = menu_items[(index + 1) % len(menu_items)]
                print(f'Selected button: {selected_item}')
            elif event.key == pygame.K_RETURN:
                if selected_item == "Start":
                    print("Test")  # Действие по нажатию Enter на "Start"
                elif selected_item == "Options":
                    pass  # Действие по нажатию Enter на "Options"
                elif selected_item == "Quit":
                    running = False  # Выход из игры

    # Отрисовка меню
    draw_menu()

# Завершение работы Pygame
pygame.quit()
sys.exit()