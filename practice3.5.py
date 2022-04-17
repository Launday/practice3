import os

class Triangle:
    def __init__(self, list_of_coordinates, name):
        self.x = list_of_coordinates[0]
        self.y = list_of_coordinates[1]
        self.z = list_of_coordinates[2]
        self.name = name

    def __show__(self):
        print(
            "Тип фигуры: Треугольник\nНазвание: {}\nТочка x = {}\nТочка y = {}\nТочка z = {}\n___________________________________".format(
                self.name, self.x, self.y, self.z))

    def __move__(self, vector):
        vector = list(map(int, vector))
        self.x[0], self.x[1] = self.x[0] + vector[0], self.x[1] + vector[1]
        self.y[0], self.y[1] = self.y[0] + vector[0], self.y[1] + vector[1]
        self.z[0], self.z[1] = self.z[0] + vector[0], self.z[1] + vector[1]

    def __get_type__(self):
        return [[self.x, self.y], [self.y, self.z], [self.x, self.z]]


class Tetragon:
    def __init__(self, list_of_coordinates, name):
        self.x = list_of_coordinates[0]
        self.y = list_of_coordinates[1]
        self.z = list_of_coordinates[2]
        self.w = list_of_coordinates[3]
        self.name = name

    def __show__(self):
        print(
            "Тип фигуры: Четырехугольник\nНазвание: {}\nТочка x = {}\nТочка y = {}\nТочка z = {}\nТочка w = {}\n___________________________________".format(
                self.name, self.x, self.y, self.z, self.w))

    def __move__(self, vector):
        vector = list(map(int, vector))
        self.x[0], self.x[1] = self.x[0] + vector[0], self.x[1] + vector[1]
        self.y[0], self.y[1] = self.y[0] + vector[0], self.y[1] + vector[1]
        self.z[0], self.z[1] = self.z[0] + vector[0], self.z[1] + vector[1]
        self.w[0], self.w[1] = self.w[0] + vector[0], self.w[1] + vector[1]

    def __get_type__(self):
        return [[self.x, self.y], [self.y, self.z], [self.z, self.w], [self.w, self.x]]


def new_figure():
    global list_of_figures
    print("Выберите из списка доступных фигур:\n"
          "1) Создать треугольник\n2) Создать четырехугольник\n"
          "3) Выйти")
    try:
        choose = int(input())
        [1, 2, 3].index(choose)
    except ValueError:
        print("Введенна неверная команда")
        os.system("PAUSE")
        os.system("cls")
        new_figure()

    figure = {}
    if choose == 3:
        return
    name = input("Введите имя для вашей фигуры: ")
    if name in ['exit', 'all']:
        print("Это недопустимое имя для фигуры")
    elif name in list_of_figures:
        choose2 = str(input('Матрица с таким названием уже существует, заменить ее? (y/n)'))
        if choose2 == 'n':
            return new_figure()
    if choose == 1:
        list_of_dots, i = ['x', 'y', 'z'], 0
        while i < 3:
            dot = input("Введите координаты точки {}:".format(list_of_dots[i])).split()
            if len(dot) == 2 and all(j.strip('-').isdigit() for j in dot):
                figure[list_of_dots[i]] = list(map(int, dot))
            else:
                print("Координаты введены неверно.")
                i -= 1
            i += 1
        a = ((figure['x'][0] - figure['y'][0]) ** 2 + (figure['x'][1] - figure['y'][1]) ** 2) ** 0.5
        b = ((figure['y'][0] - figure['z'][0]) ** 2 + (figure['y'][1] - figure['z'][1]) ** 2) ** 0.5
        c = ((figure['z'][0] - figure['x'][0]) ** 2 + (figure['z'][1] - figure['x'][1]) ** 2) ** 0.5
        if a + b > c and a + c > b and b + c > a:
            list_of_figures[name] = Triangle(list(figure[i] for i in list_of_dots), name)
        else:
            print("Невозможно построить треугольник с такими координатами!")
    elif choose == 2:
        list_of_dots, i = ['x', 'y', 'z', 'w'], 0
        while i < 4:
            dot = input("Введите координаты точки {}:".format(list_of_dots[i])).split()
            if len(dot) == 2 and all(j.strip('-').isdigit() for j in dot):
                figure[list_of_dots[i]] = list(map(int, dot))
            else:
                print("Координаты введены неверно.")
                i -= 1
            i += 1
        a = ((figure['x'][0] - figure['y'][0]) ** 2 + (figure['x'][1] - figure['y'][1]) ** 2) ** 0.5
        b = ((figure['y'][0] - figure['z'][0]) ** 2 + (figure['y'][1] - figure['z'][1]) ** 2) ** 0.5
        c = ((figure['z'][0] - figure['x'][0]) ** 2 + (figure['z'][1] - figure['x'][1]) ** 2) ** 0.5
        d = ((figure['y'][0] - figure['w'][0]) ** 2 + (figure['y'][1] - figure['w'][1]) ** 2) ** 0.5
        e = ((figure['w'][0] - figure['x'][0]) ** 2 + (figure['w'][1] - figure['x'][1]) ** 2) ** 0.5
        f = ((figure['z'][0] - figure['w'][0]) ** 2 + (figure['z'][1] - figure['w'][1]) ** 2) ** 0.5
        list_of_variants = {a: [b, c, d, e], b: [a, c, d, f], c: [a, b, e, f], d: [a, b, e, f], e: [a, c, d, f],
                            f: [b, c, d, e]}
        if all((i < sum(list_of_variants[max(list_of_variants)]) - i) for i in
               list_of_variants[max(list_of_variants)]) and all(i > 0 for i in list_of_variants[max(list_of_variants)]):
            list_of_figures[name] = Tetragon(list(figure[i] for i in list_of_dots), name)
        else:
            print("Невозможно построить четырехугольник с такими координатами!")
    os.system("PAUSE")
    os.system("cls")
    return new_figure()


def delete_figure():
    global list_of_figures
    name = input("Введите название фигуры, которую хотите удалить или exit чтобы вернуться в меню.")
    if name == 'exit':
        return
    elif name in list_of_figures:
        del list_of_figures[name]
    else:
        print("Фигуры с таким названием нет в списке.")
        os.system("PAUSE")
        os.system("cls")
        delete_figure()


def show():
    global list_of_figures
    name = input(
        "Введите название фигуры, которую хотите удалить, all, чтобы вывести все доступные фигуры или exit, чтобы вернуться в меню.  ")
    if name == 'exit':
        return
    print('___________________________________')
    if name == 'all':
        for i in list_of_figures:
            list_of_figures[i].__show__()
    elif name in list_of_figures:
        list_of_figures[name].__show__()
    else:
        print("Фигуры с таким названием нет в списке.")
    os.system("PAUSE")
    os.system("cls")
    show()


def move():
    global list_of_figures
    name = input("Введите название фигуры, которую хотите переместить или exit чтобы вернуться в меню.")
    if name == 'exit':
        return
    elif name in list_of_figures:
        coordinates = input("Введите насколько хотите переместить фигуру по x и по y ").split()
        if len(coordinates) == 2 and all(j.strip('-').isdigit() for j in coordinates):
            list_of_figures[name].__move__(coordinates)
            list_of_figures[name].__show__()
        else:
            print("Данные введены неверно.")
    else:
        print("Фигуры с таким названием нет в списке.")
        os.system("PAUSE")
        os.system("cls")
        move()


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


def isintersect():
    global list_of_figures
    name1, name2 = input("Введите названия фигур, о пересечении которых хотите узнать").split()
    if name1 in list_of_figures and name2 in list_of_figures:
        for i in range(len(list_of_figures[name1].__get_type__())):
            for j in range(len(list_of_figures[name2].__get_type__())):
                R = 0
                L1 = line(list_of_figures[name1].__get_type__()[i][0], list_of_figures[name1].__get_type__()[i][1])
                L2 = line(list_of_figures[name2].__get_type__()[j][0], list_of_figures[name2].__get_type__()[j][1])
                R = intersection(L1, L2)
                if R:
                    if list_of_figures[name1].__get_type__()[i][0][0] <= R[0] <= \
                            list_of_figures[name1].__get_type__()[i][1][0] and \
                            list_of_figures[name1].__get_type__()[i][0][1] <= R[1] <= \
                            list_of_figures[name1].__get_type__()[i][1][1] and \
                            list_of_figures[name2].__get_type__()[i][0][0] <= R[0] <= \
                            list_of_figures[name2].__get_type__()[i][1][0] and \
                            list_of_figures[name2].__get_type__()[i][0][1] <= R[1] <= \
                            list_of_figures[name2].__get_type__()[i][1][1]:
                        print("Фигуры пересекаются!")
                        return
        print("Фигуры не пересекаются!")
        return
    else:
        print("Фигуры с таким названием нет в списке.")
        os.system("PAUSE")
        os.system("cls")
        isintersect()


def menu():
    global list_of_figures
    print("Выберите из списка доступных команд:\n"
          "1) Создать объект\n2) Удалить объект\n3) Вывести координаты объекта\n4) Передвинуть объект\n"
          "5) Узнать, пересекаются ли объекты\n6) Выйти")
    try:
        choose = int(input())
        [1, 2, 3, 4, 5, 6].index(choose)
    except ValueError:
        print("Введенна неверная команда")
        os.system("PAUSE")
        os.system("cls")
        menu()
    if choose == 1:
        new_figure()
    elif choose == 2:
        delete_figure()
    elif choose == 3:
        show()
    elif choose == 4:
        move()
    elif choose == 5:
        isintersect()
    elif choose == 6:
        return
    os.system("PAUSE")
    os.system("cls")
    menu()


if __name__ == "__main__":
    global list_of_figures
    list_of_figures = {}
    a = Triangle([[-1, -1], [4, -1], [4, -3]], 'a')
    b = Tetragon([[1, -2], [2, -1], [1, 0], [0, -1]], 'b')
    c = Tetragon([[0, -5], [1, -5], [2, -4], [0, -4]], 'c')
    list_of_figures['a'] = a
    list_of_figures['b'] = b
    list_of_figures['c'] = c
    menu()
