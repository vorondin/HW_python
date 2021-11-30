znach = int(input("введите значение: "))
a = 0
max = 0

while znach > 0 and max < 9:
    a = znach % 10
    max = a if max < a else max
    znach = znach // 10

print(max)
