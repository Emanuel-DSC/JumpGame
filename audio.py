import pygame
import os
import random
from pygame import mixer

mixer.init()

jfx = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\Jump.wav')
jump_fx = pygame.mixer.Sound(jfx)
jump_fx.set_volume(0.5)

dfx = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\gameover_loud.wav')
death_fx = pygame.mixer.Sound(dfx)
death_fx.set_volume(0.5)

im = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\musics\Of Far Different Nature - 0 to 100 (CC-BY).ogg')
introMusic = pygame.mixer.Sound(im)
introMusic.set_volume(0.3)

ib = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\Execute_02.ogg')
iniciarButton = pygame.mixer.Sound(ib)
iniciarButton.set_volume(0.3)

cb = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\Bleep_05.ogg')
creditosButton = pygame.mixer.Sound(cb)
creditosButton.set_volume(0.3)

ps = open(r'C:\Users\manu_\PycharmProjects\JumpGame\Assets\sounds\1up1.wav')
points = pygame.mixer.Sound(ps)
points.set_volume(0.5)


# musica de fundo
def radio():
    path = "C:/Users/manu_/PycharmProjects/JumpGame/Assets/sounds/musics"
    file = os.path.join(path, random.choice(os.listdir(path)))
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.1)
    mixer.music.play(-1, 0, 0)