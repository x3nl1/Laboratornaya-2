def multiplication_table():
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(i * j, end="\t")
        print()
        
size = int(input("Введите размер таблицы умножения: "))
multiplication_table()
