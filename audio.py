import pygame
from pygame import mixer

mixer.init()

jump_fx = pygame.mixer.Sound('assets/sounds/Jump.wav')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/sounds/gameover_loud.mp3')
death_fx.set_volume(0.5)
introMusic = pygame.mixer.Sound('assets/sounds/musics/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
introMusic.set_volume(0.3)
iniciarButton = pygame.mixer.Sound('assets/sounds/Execute_02.ogg')
iniciarButton.set_volume(0.3)
creditosButton = pygame.mixer.Sound('assets/sounds/Bleep_05.ogg')
creditosButton.set_volume(0.3)