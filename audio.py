import pygame
import os
import random
from pygame import mixer

mixer.init()

jump_fx = pygame.mixer.Sound('assets/sounds/Jump.wav')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/sounds/gameover_loud.mp3')
death_fx.set_volume(0.5)
introMusic = pygame.mixer.Sound('assets/sounds/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
introMusic.set_volume(0.3)
iniciarButton = pygame.mixer.Sound('assets/sounds/Execute_02.ogg')
iniciarButton.set_volume(0.3)
creditosButton = pygame.mixer.Sound('assets/sounds/Bleep_05.ogg')
creditosButton.set_volume(0.3)


# musica de fundo
def radio():
    path = "C:/Users/manu_/PycharmProjects/JumpGame/Assets/sounds/musics"
    file = os.path.join(path, random.choice(os.listdir(path)))
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.1)
    mixer.music.play(-1, 0, 0)