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
def checkWin(field):
    for i in range(3):
        if field[i][0] == field[i][1] and field[i][1] == field[i][2] and field[i][0] != " ":
            winner = field[i][0]
            for j in range(3):
                field[i][j] = field[i][j].upper()
            return winner
        if field[0][i] == field[1][i] and field[1][i] == field[2][i] and field[0][i] != " ":
            winner = field[0][i]
            for j in range(3):
                field[j][i] = field[j][i].upper()
            return winner
    if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[0][0] != " ":
        winner = field[0][0]
        for j in range(3):
            field[i][i] = field[i][i].upper()
        return winner
    if field[0][2] == field[1][1] and field[1][1] == field[2][0] and field[0][2] != " ":
        winner = field[0][2]
        for j in range(3):
            field[i][2 - i] = field[i][2 - i].upper()
        return winner
field = [["x", "o", " "],
         ["o", "o", "x"],
         ["o", "o", " "]]
checkWin(field)
showField(field)
