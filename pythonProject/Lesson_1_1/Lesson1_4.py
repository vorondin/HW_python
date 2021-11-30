znach = input("введите значение: ")
a = 0
max = 0

while a < len(znach):
    if max < int(znach[a]):
       max = int(znach[a])
    a += 1
print(max)
