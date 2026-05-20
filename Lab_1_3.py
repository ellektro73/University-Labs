try:
    n = int(input("Введіть ціле число N (1 < N < 9): "))

    if 1 < n < 9:
        print("Рисунок:")
        for i in range(1, n + 1):
            for j in range(n, i - 1, -1):
                print(j, end="")

            print()
    else:
        print("Число не входить у діапазон від 2 до 8.")

except ValueError:
    print("Помилка: введіть ціле число.")