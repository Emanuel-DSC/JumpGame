import pygame
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ff = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\font\Reboot.ttf')

def textinicial(msg, cor, tamf, x, y):
    fontfinal = pygame.font.Font(ff, tamf)
    text0 = fontfinal.render(msg, True, cor)
    screen.blit(text0, [x, y])


# texto na tela
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))