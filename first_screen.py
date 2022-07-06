import pygame
import text
import colors
import images
import audio
import credits_screen
from time import sleep

pygame.font.init()

textMenu = pygame.font.Font('assets/menu/spaceship2100.ttf', 42)
textMenu2 = pygame.font.Font('assets/menu/spaceship2100.ttf', 56)

WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

b1_left, b1_top, b1_width, b1_height = 150, 200, 105, 50
b2_left, b2_top, b2_width, b2_height = 150, 300, 105, 50
b3_left, b3_top, b3_width, b3_height = 150, 400, 105, 50

clock = pygame.time.Clock()


# cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def first_menu():

    # cria a janela
    global menu_button1, menu_button2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    intro = True
    pygame.mixer.init()
    pygame.mixer.music.load('Assets/sounds/musics/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    while intro:

        screen.blit(images.bg_menu_image, (0, 0))
        screen.blit(images.spaceStation_image, (0, 0))
        screen.blit(images.char_menu, (200, 400))
        pygame.draw.rect(screen, WHITE, [b1_left, b1_top, b1_width, b1_height])
        screen.blit(images.menu_button1, (b1_left, b1_top))
        pygame.draw.rect(screen, WHITE, [b2_left, b2_top, b2_width, b2_height])
        screen.blit(images.menu_button2, (b2_left, b2_top))
        pygame.draw.rect(screen, WHITE, [b3_left, b3_top, b3_width, b3_height])
        screen.blit(images.menu_button3, (b3_left, b3_top))
        text.draw_text('The Looping', textMenu, colors.WHITE, 190, 50)
        text.draw_text('Jump', textMenu2, colors.WHITE, 230, 90)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                w = pygame.mouse.get_pos()[0]
                z = pygame.mouse.get_pos()[1]

                # inicia o jogo
                if b1_left < w < (b1_left + b1_width) and b1_top < z < (b1_top + b1_height):
                    pygame.mixer.music.fadeout(1000)
                    sleep(0.5)
                    audio.iniciarButton.play()
                    sleep(1.3)
                    pygame.mixer.music.unload()
                    intro = False

                #vai para a pagina de creditos
                if b2_left < w < (b2_left + b2_width) and b2_top < z < (b2_top + b2_height):
                    pygame.mixer.music.fadeout(1000)
                    sleep(0.5)
                    audio.creditosButton.play()
                    sleep(1.3)
                    pygame.mixer.music.unload()
                    intro = False
                    credits_screen.credits_menu()

                # fecha o jogo
                if b3_left < w < (b3_left + b3_width) and b3_top < z < (b3_top + b3_height):
                    pygame.quit()
                    quit()

            mouse = pygame.mouse.get_pos()

            if b1_left + b1_width > mouse[0] > b1_left and b1_top + b1_height > mouse[1] > b1_top:
                images.menu_button1 = pygame.image.load('assets/menu/iniciar_on.png').convert_alpha()
            else:
                images.menu_button1 = pygame.image.load('assets/menu/iniciar_off.png').convert_alpha()

            if b2_left + b2_width > mouse[0] > b2_left and b2_top + b2_height > mouse[1] > b2_top:
                images.menu_button2 = pygame.image.load('assets/menu/creditos_on.png').convert_alpha()
            else:
                images.menu_button2 = pygame.image.load('assets/menu/creditos_off.png').convert_alpha()

            if b3_left + b3_width > mouse[0] > b3_left and b3_top + b3_height > mouse[1] > b3_top:
                images.menu_button3 = pygame.image.load('assets/menu/sair_on.png').convert_alpha()
            else:
                images.menu_button3 = pygame.image.load('assets/menu/sair_off.png').convert_alpha()

        pygame.display.update()
        clock.tick(60)
