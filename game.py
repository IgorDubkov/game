# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 700
HEIGHT = 700
FPS = 0.5

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Загрузка всей игровой графики
background = pygame.image.load('pole.png').convert()
background_rect = background.get_rect()

class Fon:
    koord = ((30, 665), (108, 653), (177, 647), (251, 648), (322, 642), (390, 641), (462, 648), (528, 653), (601, 659), (674, 656), (669, 584), (602, 583), (527, 577), (460, 569), (392, 573), (322, 571), (249, 577), (179, 576), (108, 573), (33, 582), (33, 509), (111, 510), (181, 508), (253, 505), (322, 503), (389, 501), (462, 505), (531, 503), (603, 515), (671, 515), (669, 439), (600, 444), (522, 436), (460, 434), (386, 435), (318, 435), (246, 442), (178, 440), (103, 437), (37, 440), (32, 374), (107, 372), (178, 373), (245, 371), (320, 370), (387, 371), (468, 372), (527, 367), (603, 370), (670, 369), (669, 296), (598, 296), (531, 302), (466, 306), (385, 304), (318, 304), (247, 305), (180, 302), (106, 305), (31, 306), (35, 235), (108, 234), (178, 234), (249, 234), (319, 233), (388, 234), (454, 236), (524, 237), (602, 234), (666, 233), (663, 166), (593, 171), (523, 169), (454, 166), (385, 167), (315, 166), (244, 167), (181, 167), (109, 168), (38, 165), (35, 100), (112, 103), (180, 106), (252, 101), (320, 99), (389, 98), (457, 96), (523, 97), (587, 101), (665, 98), (662, 33), (586, 32), (522, 32), (454, 33), (379, 31), (315, 34), (247, 36), (175, 36), (107, 38), (41, 38))

class Kubik:
    def brosok(self):
        return random.randint(1, 6)

class Player(pygame.sprite.Sprite):
    def __init__(self, colorr):
        self.colorr = colorr
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.colorr)
        self.rect = self.image.get_rect()
        self.position = 0

    def update(self):
        a, b = Fon.koord[self.position]
        self.rect.center = (a, b)
        print(Kub.brosok())
        for i in range(Kub.brosok()):
            self.position += 1




all_sprites = pygame.sprite.Group()
player = Player(GREEN)
player1 = Player(RED)
Kub = Kubik()
all_sprites.add(player, player1)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
