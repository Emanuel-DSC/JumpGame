import pygame
import images
import first_screen
import audio


pygame.font.init()

textMenu = pygame.font.Font('assets/menu/spaceship2100.ttf', 42)
textMenu2 = pygame.font.Font('assets/menu/spaceship2100.ttf', 56)
font_normal = pygame.font.SysFont('Lucida Sans', 20)
font_small = pygame.font.SysFont('Lucida Sans', 15)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

b1_left, b1_top, b1_width, b1_height = 150, 200, 105, 50
b2_left, b2_top, b2_width, b2_height = 150, 300, 105, 50
b3_left, b3_top, b3_width, b3_height = 150, 400, 105, 50

clock = pygame.time.Clock()

# cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def credits_menu():

    # cria a janela
    global menu_button1, menu_button2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    intro = True
    pygame.mixer.init()
    pygame.mixer.music.load('Assets/sounds/musics/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    while intro:

        screen.blit(images.credits_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    intro = False
                    first_screen.first_menu()


        pygame.display.update()
        clock.tick(60)