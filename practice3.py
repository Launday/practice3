import numpy as np
from numpy import linalg as LA
import os


class Matrix:
    def __init__(self, lists):
        self.matrix = lists

    def output(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += '{}\t'.format(j)
            string = string[:-1] + '\n'
        string = string[:-1]
        print(string)

    def __determ__(self):
        x = LA.det(self.matrix)
        return x

    def __add__(self, obj):
        return self.matrix + obj.matrix

    def __mul__(self, obj):
        if type(obj) == Matrix:
            return self.matrix.dot(obj.matrix)
        else:
            return np.dot(self.matrix, obj)

    def __divide__(self, obj):
        if type(obj) == Matrix:
            return self.__mul__(LA.inv(obj.matrix))
        else:
            return np.divide(self.matrix, obj)

    def __transpose__(self):
        self.matrix = self.matrix.transpose()
        return self.matrix

    def __compare__(self, obj):
        return self.matrix == obj.matrix

    def __degree__(self, dig):
        self.matrix = np.linalg.matrix_power(self.matrix, dig)
        return self.matrix

    def __norm__(self):
        return np.linalg.norm(self.matrix)

    def __type__(self):
        spis = list()
        if len(self.matrix) == len(self.matrix[0]):
            spis.append("квадратная")
            if all(self.matrix[j][j] == 1 for j in range(len(self.matrix))) and all(
                    sum(self.matrix[i] for i in range(len(self.matrix))) == 1):
                spis.append("единичная")
            if all(sum(self.matrix[i]) == self.matrix[i][i] for i in range(len(self.matrix))):
                spis.append("диагональная")
            if all((self.matrix[i][j] == self.matrix[j][i]) for i in range(len(self.matrix)) for j in
                   range(len(self.matrix))):
                spis.append("симметричная")
            if all(self.matrix[i][j] == 0 for i in range(0, len(self.matrix)) for j in range(1 + i, len(self.matrix))):
                spis.append("верхняя треугольная")
            if all(self.matrix[j][i] == 0 for i in range(0, len(self.matrix)) for j in range(1 + i, len(self.matrix))):
                spis.append("нижняя треугольная")
        if all(sum(self.matrix[i] for i in range(len(self.matrix))) == 0):
            spis.append("нулевая")
        print("Эта матрица: ", end='')
        print(*(spis[i] for i in range(len(spis))), sep=', ')


def data_input():
    R = input("Введите количество строк: ")
    C = input("Введите количество столбцов: ")
    try:
        R = int(R)
        C = int(C)
    except ValueError:
        print("Введены недопустимые значения!")
        os.system("PAUSE")
        os.system('cls')
        return data_input()
    print("Введите все числа в одну строку через пробел: ", end='')
    entries = list(input().split())
    if all(i.isdigit() for i in entries) and len(entries) == R * C:
        matrix = np.array(list(map(int, entries))).reshape(R, C)
    else:
        print("Введены неверные данные!")
        os.system("PAUSE")
        os.system('cls')
        matrix = data_input()
    return matrix


def operation_matrix():
    global list_of_matrix
    list_of_commands = ['+', '-', '==', '*', "/", "^", "+=", "*=", "-=", "/=", "^="]
    print(
        "Введите через пробел название первой матрицы, операцию, которую хотите выполнить и название второй матрицы или число\nНапример: a += b"
        "\nВведите help, если хотите увидеть полный список доступных операций или exit, чтобы вернуться в меню.")
    choose = input()
    if choose == 'help':
        print(
            '+ вывести результат сложения двух матриц\n- вывести результат вычитания двух матриц\n* вывести результат умножения двух матриц или матрицы и числа\n/ вывести результат деления двух матриц или матрицы и числа\n^ вывести результат возведения матрицы в степень\n== сравнение двух матриц\nОперации присваивания: +=, -=, *=, /=, ^=')
        os.system("PAUSE")
        os.system('cls')
        return operation_matrix()
    elif choose == 'exit':
        return
    if len(choose.split()) != 3:
        print("Уравнение должно иметь вид, представленный в примере!")
        os.system("PAUSE")
        os.system('cls')
        return operation_matrix()
    first, command, second = choose.split()[0], choose.split()[1], choose.split()[-1]
    if command in list_of_commands:
        if first in list_of_matrix and (second in list_of_matrix or second.isdigit()):
            if command in ('+', '+=', '-', '-='):
                if np.shape(list_of_matrix[first].matrix) == np.shape(list_of_matrix[second].matrix):
                    if command == '+':
                        list_of_matrix['temp'].matrix = list_of_matrix[first].__add__(list_of_matrix[second])
                        list_of_matrix['temp'].output()
                    elif command == '+=':
                        list_of_matrix[first].matrix = list_of_matrix[first].__add__(list_of_matrix[second])
                        list_of_matrix[first].output()
                    elif command == '-':
                        list_of_matrix['temp'].matrix = list_of_matrix[first].__add__(
                            Matrix(list_of_matrix[second].__mul__(-1)))
                        list_of_matrix['temp'].output()
                    elif command == '-=':
                        list_of_matrix[first].matrix = list_of_matrix[first].__add__(
                            Matrix(list_of_matrix[second].__mul__(-1)))
                        list_of_matrix[first].output()
                else:
                    print("Эти две матрицы нельзя сложить/вычесть, они должны быть одинакового размера.")

            elif command == '==':
                if (all(all(list_of_matrix[first].__compare__(list_of_matrix[second])[i]) for i in
                        range(len(list_of_matrix[first].matrix)))):
                    print('Матрица {} равна матрице {}'.format(first, second))
                else:
                    print('Матрица {} не равна матрице {}'.format(first, second))
            elif command == '*' or command == '*=':
                if second.isdigit():
                    if command == '*':
                        list_of_matrix['temp'].matrix = list_of_matrix[first].__mul__(int(second))
                        list_of_matrix['temp'].output()
                    else:
                        list_of_matrix[first].matrix = list_of_matrix[first].__mul__(int(second))
                        list_of_matrix[first].output()
                elif second in list_of_matrix:
                    if np.shape(list_of_matrix[first].matrix)[1] == np.shape(list_of_matrix[second].matrix)[0]:
                        if command == '*':
                            list_of_matrix['temp'].matrix = list_of_matrix[first].__mul__(list_of_matrix[second].matrix)
                            list_of_matrix['temp'].output()
                        else:
                            list_of_matrix[first].matrix = list_of_matrix[first].__mul__(list_of_matrix[second].matrix)
                            list_of_matrix[first].output()
                    else:
                        print(
                            "Эти две матрицы нельзя перемножить, число столбцов первой должно совпадать с числом строк второй.")
            elif command in ('/', '/='):
                if second.isdigit():
                    if command == '/':
                        list_of_matrix['temp'].matrix = list_of_matrix[first].__divide__(int(second))
                        list_of_matrix['temp'].output()
                    else:
                        list_of_matrix[first].matrix = list_of_matrix[first].__divide__(int(second))
                        list_of_matrix[first].output()
                elif second in list_of_matrix:
                    if np.shape(list_of_matrix[first].matrix)[1] == np.shape(list_of_matrix[second].matrix)[0] and \
                            list_of_matrix[second].__determ__() != 0 and np.shape(list_of_matrix[second].matrix)[0] == \
                            np.shape(list_of_matrix[second].matrix)[1]:
                        if command == '/':
                            list_of_matrix['temp'].matrix = list_of_matrix[first].__divide__(list_of_matrix[second])
                            list_of_matrix['temp'].output()
                        else:
                            list_of_matrix[first].matrix = list_of_matrix[first].__divide__(list_of_matrix[second])
                            list_of_matrix[first].output()
                    else:
                        print(
                            "Эти две матрицы нельзя поделить, число столбцов первой должно совпадать с числом строк второй. Определитель второй матрицы != 0 и вторая матрица должна быть квадратной.")
            elif command in ('^', '^='):
                if second.isdigit():
                    if command == '^':
                        list_of_matrix['temp'].matrix = list_of_matrix[first].__degree__(int(second))
                        list_of_matrix['temp'].output()
                    else:
                        list_of_matrix[first].matrix = list_of_matrix[first].__divide__(int(second))
                        list_of_matrix[first].output()
                else:
                    print("Введенная степень не является числом.")
        else:
            print("Такой/их матрицы/ц нет в списке")
    else:
        print("Введена неверная команда!")
    os.system("PAUSE")
    os.system('cls')
    return operation_matrix()


def operation_one_matrix():
    global list_of_matrix
    list_of_operations = ['1', '2', '3', '4', '5', '6']
    print(
        "1) Транспонировать матрицу\n2) Найти обратную матрицу\n3) Вычислить детерминант\n4) Вычислить норму\n5) Определить тип матрицы\n6) Выход")
    choose = input()
    if choose in list_of_operations:
        if choose == '6':
            return
        matr = input("Введите название матрицы ")
        os.system('cls')

        if matr in list_of_matrix:
            if choose == '1':
                print("Транспонированная матрица: ")
                list_of_matrix[matr].matrix = list_of_matrix[matr].__transpose__()
                list_of_matrix[matr].output()
            elif choose == '2':
                print("Обратная матрица: ")
                list_of_matrix[matr].matrix = LA.inv(list_of_matrix[matr].matrix)
                list_of_matrix[matr].output()
            elif choose == '3':
                print("Определитель матрицы: ")
                print(list_of_matrix[matr].__determ__())
            elif choose == '4':
                print("Норма матрицы: ")
                print(list_of_matrix[matr].__norm__())
            elif choose == '5':
                list_of_matrix[matr].__type__()
        else:
            print("Такой матрицы нет в списке")
    else:
        print("Введена неверная команда!")
    os.system("PAUSE")
    os.system('cls')
    return operation_one_matrix()


def menu():
    global list_of_matrix
    print(
        "1) Ввести матрицу и дать ей название\n2) Вывести матрицу\n3) Произвести операцию с двумя матрицами/матрицей и числом\n4) Произвести операцию с одной матрицей\n5) Выход")
    choose = input()
    if choose in ['1', '2', '3', '4', '5']:
        os.system('cls')
        if choose == '1':
            name = str(input("Введите название для матрицы: "))
            if name in list_of_matrix:
                choose2 = str(input('Матрица с таким названием уже существует, заменить ее? (y/n)'))
                if choose2 == 'n':
                    menu()
            list_of_matrix[name] = Matrix(data_input())
        elif choose == '2':
            name = str(input("Введите название матрицы: "))
            if name in list_of_matrix:
                list_of_matrix[name].output()
            else:
                print("Матрицы с таким названием не существует.")
        elif choose == '3':
            operation_matrix()
        elif choose == '4':
            operation_one_matrix()
        elif choose == '5':
            return
    else:
        print('Введена неверная команда!')
    os.system("PAUSE")
    os.system('cls')
    menu()


if __name__ == "__main__":
    global list_of_matrix
    list_of_matrix = {'temp': Matrix(np.array([[4, 4], [3, 3]])), 'f': Matrix(np.array([[3, 4], [3, 3]])),
                      's': Matrix(np.array([[3, 3], [3, 4]])), 'a': Matrix(np.array([[2, 3, 1], [3, 3, 5], [3, 1, 2]]))}
    menu()
