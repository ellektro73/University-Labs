def calculate_x():
    try:
        a = float(input("Введіть значення a (від 1 до 100): "))
        b = float(input("Введіть значення b (від 1 до 100): "))

        if not (1 <= a <= 100) or not (1 <= b <= 100):
            print("Помилка: Числа повинні бути в діапазоні від 1 до 100.")
            return

        if a < b:
            x = (a * 3 - 5) / b
            print(f"Обчислення за умовою a < b: X = ({a} * 3 - 5) / {b}")

        elif a == b:
            x = -4
            print(f"Обчислення за умовою a = b: X = -4")

        else:
            x = (a ** 4 + b) / a
            print(f"Обчислення за умовою a > b: X = ({a}^4 + {b}) / {a}")

        print(f"Результат: X = {round(x, 4)}")

    except ValueError:
        print("Помилка: Введіть коректні числові значення.")


if __name__ == "__main__":
    calculate_x()