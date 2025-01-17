# coding=windows-1251
def showField(field):
    print()
    for i in range(3):
        for j in range(3):
            print(" |" + field[i][j] + "| ", end='')
        print()
        print()
def makeMove(field, player):
    if player == 1:
        sym = 'x'
    else:
        sym = 'o'
    print("Ход игрока:", sym)
    while True:
        data = input("Введите номер строки и номер столбца, в который хотите поставить символ(через пробел): ").split()
        if len(data) != 2:
            print("Неверный ввод! Должно быть введено ровно два числа(через пробел)")
            continue
        if data[0].isdigit() == False or data[1].isdigit() == False:
            print("Неверный ввод! Нужно ввести целые числа")
            continue
        data[0] = int(data[0])
        data[1] = int(data[1])
        if data[0] not in {1, 2, 3} or data[1] not in {1, 2, 3}:
            print("Неверный ввод! Номер строки и номер столбца должны быть в промежутке от 1 до 3")
            continue
        x, y = data[0], data[1]
        if field[x-1][y-1] != " ":
            print("Неверный ввод! Данная ячейка уже занята")
            continue
        
        print("Ход сделан")
        field[x-1][y-1] = sym
        break

field = [["x", "o", " "],
         ["x", " ", "o"],
         ["o", "x", " "]]
makeMove(field, 2)
showField(field)
