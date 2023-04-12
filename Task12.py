# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для  этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
import math

# x+y = s => x = s-y
# x*y = p => sy - y**2 - p = 0
print("s * y - y ** 2 - p = 0")
s = int(input("Enter the sum of two numbers "))
p = int(input("Enter the product of two numbers "))

discriminant = s ** 2 - 4 * -1 * - p
print(f"discriminant = {discriminant}")
if discriminant > 0:
    y = abs((- s + math.sqrt(discriminant)) / 2 * -1)
elif discriminant == 0:
    y = - s / 2
else:
    print("the equation has no roots")
x = s - y
print(f"Petya guessed {round(y, 1)} and {round(x, 1)}")


