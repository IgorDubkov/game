# Pygame игра Змеи и лестницы
import pygame
import random

# Параметры графики
WIDTH = 700
HEIGHT = 700
FPS = 2

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Координаты полей игры
KOORD = ((30, 665), (108, 653), (177, 647), (251, 648), (322, 642), 
(390, 641), (462, 648), (528, 653), (601, 659), (674, 656), (669, 584), 
(602, 583), (527, 577), (460, 569), (392, 573), (322, 571), (249, 577), 
(179, 576), (108, 573), (33, 582), (33, 509), (111, 510), (181, 508), 
(253, 505), (322, 503), (389, 501), (462, 505), (531, 503), (603, 515), 
(671, 515), (669, 439), (600, 444), (522, 436), (460, 434), (386, 435), 
(318, 435), (246, 442), (178, 440), (103, 437), (37, 440), (32, 374), 
(107, 372), (178, 373), (245, 371), (320, 370), (387, 371), (468, 372), 
(527, 367), (603, 370), (670, 369), (669, 296), (598, 296), (531, 302), 
(466, 306), (385, 304), (318, 304), (247, 305), (180, 302), (106, 305), 
(31, 306), (35, 235), (108, 234), (178, 234), (249, 234), (319, 233), 
(388, 234), (454, 236), (524, 237), (602, 234), (666, 233), (663, 166), 
(593, 171), (523, 169), (454, 166), (385, 167), (315, 166), (244, 167), 
(181, 167), (109, 168), (38, 165), (35, 100), (112, 103), (180, 106), 
(252, 101), (320, 99), (389, 98), (457, 96), (523, 97), (587, 101), 
(665, 98), (662, 33), (586, 32), (522, 32), (454, 33), (379, 31), 
(315, 34), (247, 36), (175, 36), (107, 38), (41, 38))

font_name = pygame.font.match_font('arial')

# Создаем игру и окно
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змеи и лестницы")
clock = pygame.time.Clock()

# Загрузка всей игровой графики
background = pygame.image.load('pole.png').convert()
background_rect = background.get_rect()



def brosok():
    return random.randint(1, 6)



def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "ЗМЕИ И ЛЕСТНИЦЫ", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Игра с кубиком", 64, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажми кнопку", 64, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

class Player(pygame.sprite.Sprite):
    def __init__(self, colorr):
        self.colorr = colorr
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.colorr)
        self.rect = self.image.get_rect()
        self.position = 0

    def update(self):
        x, y = KOORD[self.position]
        self.rect.center = (x, y)
        print(brosok())
        for i in range(brosok()):
            self.position += 1

all_sprites = pygame.sprite.Group()
player = Player(GREEN)
player1 = Player(RED)
all_sprites.add(player, player1)

# Цикл игры
def main():
    game_over = True
    running = True
    while running:
        if game_over:
            show_go_screen()
            game_over = False
        
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
    
if __name__ == "__main__":
    main()
