def multiplication_table():
    size = int(input("Введите размер таблицы умножения: "))
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(i * j, end="\t")
        print()

multiplication_table()
