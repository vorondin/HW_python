start = float(input("Расстояние первого дня: "))
cel = float(input("Цель спортсмена: "))
den = 1
while start <= cel:
    print(den, "-й день:", round(start, 2))
    start = start + start * 0.1
    den += 1
print(den, "-й день:", round(start, 2))
print(" ")
print("Ответ: на", den, "-й день спортсмен достиг результата — не менее ", cel, "км")
