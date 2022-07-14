import pygame
from spritesheet import SpriteSheet

jumpy = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\platform\char.png')
jumpy_image = pygame.image.load(jumpy).convert_alpha()

bg1 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\bg1.png')
bg_image = pygame.image.load(bg1).convert_alpha()

bg2 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\bg2.png')
bg_image2 = pygame.image.load(bg2).convert_alpha()

bg3 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\bg3.png')
bg_image3 = pygame.image.load(bg3).convert_alpha()

gl = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\1.png')
green_line = pygame.image.load(gl).convert_alpha()

pl = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\2.png')
purple_line = pygame.image.load(pl).convert_alpha()

cbg = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\credtis_bg.png')
credits_bg = pygame.image.load(cbg).convert_alpha()

pl = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\platform\platform.png')
platform_image = pygame.image.load(pl).convert_alpha()

# enemy spritesheet

esi1 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\enemy\blue.png')
enemy_sheet_img = pygame.image.load(esi1).convert_alpha()

esi2 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\enemy\green.png')
enemy_sheet_img2 = pygame.image.load(esi2).convert_alpha()

esi3 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\enemy\pink.png')
enemy_sheet_img3 = pygame.image.load(esi3).convert_alpha()

esi4 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\enemy\white.png')
enemy_sheet_img4 = pygame.image.load(esi4).convert_alpha()

enemy_sheet = SpriteSheet(enemy_sheet_img)
enemy_sheet2 = SpriteSheet(enemy_sheet_img2)
enemy_sheet3 = SpriteSheet(enemy_sheet_img3)
enemy_sheet4 = SpriteSheet(enemy_sheet_img4)

# portal spritesheet

fsi1 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\teleport\fan.png')
fan_sheet_img = pygame.image.load(fsi1).convert_alpha()

fsi2 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\teleport\fan2.png')
fan_sheet_img2 = pygame.image.load(fsi2).convert_alpha()

fsi3 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\teleport\fan3.png')
fan_sheet_img3 = pygame.image.load(fsi3).convert_alpha()

fan_sheet = SpriteSheet(fan_sheet_img)
fan_sheet2 = SpriteSheet(fan_sheet_img2)
fan_sheet3 = SpriteSheet(fan_sheet_img3)

# menu sprites

cm = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\char_mennu.png')
char_menu = pygame.image.load(cm).convert_alpha()

bgm = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\bg\bg1.png')
bg_menu_image = pygame.image.load(bgm).convert_alpha()

si = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\spaceStation.png')
spaceStation_image = pygame.image.load(si).convert_alpha()

mb1 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_off.png')
menu_button1 = pygame.image.load(mb1).convert_alpha()
mb1a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_off.png')
menu_button1aux = pygame.image.load(mb1a).convert_alpha()

mb2 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\creditos_off.png')
menu_button2 = pygame.image.load(mb2).convert_alpha()
mb2a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\creditos_off.png')
menu_button2aux = pygame.image.load(mb2a).convert_alpha()

mb3 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\sair_off.png')
menu_button3 = pygame.image.load(mb3).convert_alpha()
mb3a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\sair_off.png')
menu_button3aux = pygame.image.load(mb3a).convert_alpha()


mb4 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_on.png')
menu_button4 = pygame.image.load(mb4).convert_alpha()
mb4a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_on.png')
menu_button4aux = pygame.image.load(mb4a).convert_alpha()


mb5 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\creditos_on.png')
menu_button5 = pygame.image.load(mb5).convert_alpha()
mb5a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_on.png')
menu_button5aux = pygame.image.load(mb5a).convert_alpha()


mb6 = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\sair_on.png')
menu_button6 = pygame.image.load(mb6).convert_alpha()
mb6a = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\menu\iniciar_on.png')
menu_button6aux = pygame.image.load(mb6a).convert_alpha()