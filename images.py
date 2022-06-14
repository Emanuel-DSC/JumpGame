import pygame
# carrega imagens
from spritesheet import SpriteSheet

jumpy_image = pygame.image.load('assets/char/char.png').convert_alpha()
bg_image = pygame.image.load('assets/bg/bg1.png').convert_alpha()
bg_image2 = pygame.image.load('assets/bg/bg2.png').convert_alpha()
bg_image3 = pygame.image.load('assets/bg/bg3.png').convert_alpha()
green_line = pygame.image.load('assets/bg/1.png').convert_alpha()
purple_line = pygame.image.load('assets/bg/2.png').convert_alpha()
platform_image = pygame.image.load('assets/platform/platform.png').convert_alpha()
# enemy spritesheet
enemy_sheet_img = pygame.image.load('assets/enemy/blue.png').convert_alpha()
enemy_sheet_img2 = pygame.image.load('assets/enemy/green.png').convert_alpha()
enemy_sheet_img3 = pygame.image.load('assets/enemy/pink.png').convert_alpha()
enemy_sheet_img4 = pygame.image.load('assets/enemy/white.png').convert_alpha()
enemy_sheet = SpriteSheet(enemy_sheet_img)
enemy_sheet2 = SpriteSheet(enemy_sheet_img2)
enemy_sheet3 = SpriteSheet(enemy_sheet_img3)
enemy_sheet4 = SpriteSheet(enemy_sheet_img4)
# portal spritesheet
fan_sheet_img = pygame.image.load('assets/teleport/fan.png').convert_alpha()
fan_sheet = SpriteSheet(fan_sheet_img)
fan_sheet_img2 = pygame.image.load('assets/teleport/fan2.png').convert_alpha()
fan_sheet2 = SpriteSheet(fan_sheet_img2)
fan_sheet_img3 = pygame.image.load('assets/teleport/fan3.png').convert_alpha()
fan_sheet3 = SpriteSheet(fan_sheet_img3)

char_menu = pygame.image.load('assets/menu/char_mennu.png').convert_alpha()
bg_menu_image = pygame.image.load('assets/bg/bg1.png').convert_alpha()
spaceStation_image = pygame.image.load('assets/menu/spaceStation.png').convert_alpha()
menu_button1 = pygame.image.load('assets/menu/iniciar_off.png').convert_alpha()
menu_button2 = pygame.image.load('assets/menu/creditos_off.png').convert_alpha()
menu_button3 = pygame.image.load('assets/menu/sair_off.png').convert_alpha()