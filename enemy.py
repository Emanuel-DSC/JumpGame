import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, y, sprite_sheet, scale):
        pygame.sprite.Sprite.__init__(self)
        # define variaveis
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.flip = True
        else:
            self.flip = False

        # carrega imagens da spritesheet
        animation_steps = 7
        for animation in range(animation_steps):
            image = sprite_sheet.get_image(animation, 32, 32, scale, (0, 0, 0))
            image = pygame.transform.flip(image, self.flip, False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)

        # seleciona imagem inicial e cria um retangulo a partir
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()

        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = SCREEN_WIDTH
        self.rect.y = y

    def update(self, scroll, SCREEN_WIDTH):
        # atualiza animacao
        animation_cooldown = 100
        # atualiza imagem dependendo do quadro atual
        self.image = self.animation_list[self.frame_index]
        # checa se passou tempo suficiente desde a ultima atualizacao
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # se a animacao tiver acabado, reseta
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        # mover inimigo
        self.rect.x += self.direction * 2
        self.rect.y += scroll

        # checa se saiu de tela
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()