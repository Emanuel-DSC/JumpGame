import pygame
import random
import os
from enemy import Enemy
from fan import Fan
import text
import first_screen
import colors
import audio
import images

# inicializa o pygame
pygame.init()

# tamanho da janela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Looping Jump')

# fps
clock = pygame.time.Clock()
FPS = 60

# variaveis do jogo
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('high_score.txt'):
    with open('high_score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0

# fontes
font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)


# desenha linhas de checkpoint(troca de fundo) e as apaga depois
def draw_checkpoints():
    if 1599 < score:
        screen.blit(images.green_line, (20, score - 1899 + SCROLL_THRESH))
        if 1950 < score:
            images.green_line.fill(colors.INVISIBLE)
    if 3200 < score:
        screen.blit(images.purple_line, (20, score - 3500 + SCROLL_THRESH))
        if 3750 < score:
            images.green_line.fill(colors.INVISIBLE)


# painel de informacao
def draw_panel():
    pygame.draw.rect(screen, colors.BLACK, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(screen, colors.WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
    text.draw_text('SCORE: ' + str(score), font_small, colors.WHITE, 0, 0)


# plano de fundo
def draw_bg(bg_scrolling):
    screen.blit(images.bg_image, (0, 0 + bg_scrolling))
    screen.blit(images.bg_image, (0, -600 + bg_scrolling))

    if 1999 < score < 3500:
        screen.blit(images.bg_image2, (0, 0 + bg_scrolling))
        screen.blit(images.bg_image2, (0, -600 + bg_scrolling))

    elif score >= 3500:
        screen.blit(images.bg_image3, (0, 0 + bg_scrolling))
        screen.blit(images.bg_image3, (0, -600 + bg_scrolling))


# jogador
class Player:

    def __init__(self, x, y):
        self.image = pygame.transform.scale(images.jumpy_image, (50, 50))
        self.width = 22
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # reinicia variaveis
        scroll = 0
        dx = 0
        dy = 0

        # pressionar tecla
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = False
        if key[pygame.K_d]:
            dx = 10
            self.flip = True

        # gravidade
        self.vel_y += GRAVITY
        dy += self.vel_y

        # entrar de um lado da tela e sair do outro
        if self.rect.left + dx < 0:
            dx = 350
        if self.rect.right + dx > 400:
            dx = -350

        # checar colisao com plataforma
        for platform in platform_group:
            # colisao vertical
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # checa se esta acima da plataforma
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20
                        audio.jump_fx.play()

        # checa colisao com portal e teleporta o personagem pra cima do mapa
        if pygame.sprite.spritecollide(jumpy, fan_group, False):
            if pygame.sprite.spritecollide(jumpy, fan_group, False, pygame.sprite.collide_mask):
                self.vel_y = - 42
                scroll = -dy

        # checa se o jogador atingiu o topo da tela
        if self.rect.top <= SCROLL_THRESH:
            # se estiver pulando
            if self.vel_y < 0:
                scroll = -dy

        # atualizando a posicao do retangulo (parede)
        self.rect.x += dx
        self.rect.y += dy + scroll

        # atualizar a data
        self.mask = pygame.mask.from_surface(self.image)

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))


# platforma
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(images.platform_image, (width, 30))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scrolling):

        # se for plataforma movel, mover de lado a lado
        if self.moving:
            self.move_counter += 1
            self.rect.x += self.direction * self.speed

        # trocar a posicao se tiver andado completamente ou atingido a parede
        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0

        # atualizar posicao vertical
        self.rect.y += scrolling

        # checar se saiu da tela
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# instancia jogador
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# cria grupo de sprites
platform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
fan_group = pygame.sprite.Group()

# cria plataforma inicial
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)

# chama o menu principal
first_screen.first_menu()

# musicas do jogo
audio.radio()

# loop do jogo
run = True

while run:

    clock.tick(FPS)

    thing_startx = random.randrange(0, 600)
    thing_starty = - 600
    thing_speed = 13
    thing_width = 100
    thing_height = 100

    if not game_over:
        scroll = jumpy.move()

        # desenha plano de fundo
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        draw_bg(bg_scroll)

        # gera plataformas
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(40, 60)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1, 2)
            if p_type == 1 and score > 3000:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_w, p_moving)
            platform_group.add(platform)

        # atualiza plataformas
        platform_group.update(scroll)

        # gera inimigos
        if len(enemy_group) == 0 and score > 1100:
            enemy = Enemy(SCREEN_WIDTH, 120, images.enemy_sheet, 1.5)
            enemy_group.add(enemy)
            if 1899 < score < 3400:
                enemy_group.remove(enemy)
                enemy = Enemy(SCREEN_WIDTH, 120, images.enemy_sheet2, 1.5)
                enemy_group.add(enemy)
            elif score >= 3400:
                enemy_group.remove(enemy)
                enemy = Enemy(SCREEN_WIDTH, 120, images.enemy_sheet3, 1.5)
                enemy_group.add(enemy)
                # aumentar velocidade do meeteoro
                enemy.direction = 3
        # elif score >= 3400:

        # atualiza inimigos
        enemy_group.update(scroll, SCREEN_WIDTH)

        # gera portais
        if len(fan_group) == 0 and score >= 1000:
            fan = Fan(SCREEN_WIDTH, 90, images.fan_sheet, 2.4)
            fan_group.add(fan)
            if 1899 < score < 3400:
                fan_group.remove(fan)
                fan = Fan(SCREEN_WIDTH, 90, images.fan_sheet2, 2.4)
                fan_group.add(fan)
            elif score >= 3400:
                fan_group.remove(fan)
                fan = Fan(SCREEN_WIDTH, 90, images.fan_sheet3, 2.4)
                fan_group.add(fan)

        # atualiza portais
        fan_group.update(scroll, SCREEN_WIDTH)

        # atualiza placar
        if scroll > 0:
            score += scroll

        # desenha uma linha da pontuacao maxima anterior
        pygame.draw.line(screen, colors.WHITE, (0, score - high_score + SCROLL_THRESH),
                         (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
        text.draw_text('RECORDE', font_small, colors.WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

        # desenha marcador de troca de fundo
        draw_checkpoints()

        # desenha sprites
        platform_group.draw(screen)
        enemy_group.draw(screen)
        fan_group.draw(screen)
        jumpy.draw()

        # desenha o painel
        draw_panel()

        # checa fim de jogo
        if jumpy.rect.top > SCREEN_HEIGHT:
            game_over = True
            audio.death_fx.play()
        # checa colisao com inimigos
        if pygame.sprite.spritecollide(jumpy, enemy_group, False):
            if pygame.sprite.spritecollide(jumpy, enemy_group, False, pygame.sprite.collide_mask):
                game_over = True
                audio.death_fx.play()

    else:
        game_over_screen_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        game_over_screen_fade.fill(colors.BLACK)
        game_over_screen_fade.set_alpha(1)
        screen.blit(game_over_screen_fade, (0, 0))
        pygame.mixer.music.fadeout(1000)
        text.draw_text('GAME OVER!', font_big, colors.WHITE, 130, 200)
        text.draw_text('SCORE: ' + str(score), font_big, colors.WHITE, 130, 250)
        text.draw_text('PRESS SPACE TO PLAY AGAIN', font_big, colors.WHITE, 40, 300)
        # atualiza pontuacao maxima
        if score > high_score:
            high_score = score
            with open('high_score.txt', 'w') as file:
                file.write(str(high_score))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # reinicia variaveis
            game_over = False
            score = 0
            scroll = 0
            fade_counter = 0
            # reposiciona o personagem
            jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
            # reseta inimigos                enemy_group.empty()
            # reseta portal
            fan_group.empty()
            # reseta plataformas
            platform_group.empty()
            # cria plataforma inicial
            platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
            platform_group.add(platform)
            # reseta cor do checkpoint
            green_line = pygame.image.load('assets/bg/1.png').convert_alpha()
            purple_line = pygame.image.load('assets/bg/2.png').convert_alpha()
            # reseta musica
            audio.radio()

    # rotina de sincronização
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # atualiza placar maximo
            if score > high_score:
                high_score = score
                with open('high_score.txt', 'w') as file:
                    file.write(str(high_score))
            run = False

    # atualiza tela
    pygame.display.update()

pygame.quit()
