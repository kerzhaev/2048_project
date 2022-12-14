
from logics import *
import pygame
import sys
from database import get_best, cur

GAMERS_DB = get_best()

def draw_top_gamers():
    font_top = pygame.font.SysFont('simsun', 20)
    font_gamer = pygame.font.SysFont('simsun', 18)
    text_head = font_top.render('Best tries: ', True, COLOR_TEXT)
    screen.blit(text_head, (250, 5)) # отрисовываем лучшие попытки игры
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (230, 28 + 28 * index))  # отрисовываем лучшие попытки игры


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)  # рисуем окно
    font = pygame.font.SysFont('stxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    font_delta = pygame.font.SysFont('simsun', 32)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20,35))
    screen.blit(text_score_value, (175, 35)) # прикрепили переменную к экрану
    if delta >0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (160, 80))  # прикрепили переменную к экрану
    pretty_print(mas)
    draw_top_gamers()
    # отрисовка квадратиков
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            # находим левые верхние края блоков
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
COLOR_TEXT = (255,127,0)
COLORS = {
    0: (130,130,130),
    2: (255,255,255),
    4: (255,255,128),
    8: (255,255,64),
    16: (255,255,32),
    32: (255,255,16),
    64: (255,255,8),
    128: (255,255,4),
    256: (255,255,2),
    512: (255,255,0),
    1024: (255,255,255)
}

WHITE = (255,255,255)
GRAY = (130,130,130)
BLACK = (0,0,0)


BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK  + (BLOCKS+1) * MARGIN
HEIGTH = WIDTH + 110
TITLE_REC = pygame.Rect(0,0,WIDTH,110)
score = 0

mas[1][2]=2
mas[3][0]=4

print(get_empty_list(mas))
pretty_print(mas)

# for gamer in get_best():
#     print(gamer)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption('2048')
draw_interface(score)
pygame.display.update() # рисуем интерфейс после первого вызова функции
while is_zero_in_mas(mas) or can_move(mas):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta

            # input()# только когда нижимается кнопка, то производятся действия в цикле
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or4(mas, x, y)
            print(f'Мы заполнили элемент под номером {random_num}')
            draw_interface(score, delta)

            pygame.display.update() # применяем вышеописанные изменения




