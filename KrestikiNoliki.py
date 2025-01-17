def showField(field):
    print()
    for i in range(3):
        for j in range(3):
            print(" |" + field[i][j] + "| ", end='')
        print()
        print()
field = [["x", "o", " "],
         ["x", " ", "o"],
         ["o", "x", " "]]
showField(field)
