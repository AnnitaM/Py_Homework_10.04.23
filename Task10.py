# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random

coins_num = int(input("Enter the number of coins "))
side = [random.randint (0,1) for _ in range(coins_num)]
print(side)
count = 0
for i in side:
    if i == 0:
        count += 1
print(f"thenumber of coins to flip is {count}")
