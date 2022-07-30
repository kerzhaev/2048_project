import random

def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False

def move_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) !=4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0 :
                mas[i][j]*=2 # умножаем элемент в два раза
                mas[i].pop(j+1) # удаляем элемент справа
                mas[i].append(0) # в конец добавляем ноль
    return mas

def move_right(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) !=4:
            row.insert(0,0) # вставляем нули в начало
    for i in range(4): # обходим массив справа налево
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0 :
                mas[i][j]*=2 # умножаем элемент в два раза
                mas[i].pop(j-1) # удаляем элемент справа
                mas[i].insert(0,0) # в конец добавляем ноль
    return mas

def move_up(mas):

    for j in range(4):
        column = []
        for i in range(4): # проходим по рядам
            if mas[i][j] !=0:
                column.append(mas[i][j])
        while len(column)!=4: # место куда надо добавлять нули добавляем в конец
            column.append(0)
        for i in range(3): # обходим элементы, у последнего элемента нет соседа справа
            if column[i] == column[i+1] and column[i]!=0:
                column[i]*=2
                column.pop(i+1)
                column.append(0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas


def move_down(mas):

    for j in range(4):
        column = []
        for i in range(4): # проходим по рядам
            if mas[i][j] !=0:
                column.append(mas[i][j])
        while len(column)!=4: # место куда надо добавлять нули добавляем в начало
            column.insert(0, 0)
        for i in range(3, 0, -1): # обходим элементы, у последнего элемента нет соседа слева
            if column[i] == column[i-1] and column[i]!=0:
                column[i]*=2
                column.pop(i-1)
                column.insert(0,0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas

def can_move(mas):
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i+1][j]:
                True
    return False