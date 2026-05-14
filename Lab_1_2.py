numbers = [1, 3, 5, 9, 17]

print(f"{'Число':<10} | {'Квадрат':<10} | {'Куб':<10}")
print("-" * 35)

for n in numbers:
    square = n ** 2  # Обчислення квадрата
    cube = n ** 3  # Обчислення куба

    print(f"{n:<10} | {square:<10} | {cube:<10}")