izd = float(input("Введите сумму издержек фирмы: "))
vir = float(input("Введите выручку: "))
if vir > izd:
    print("Фирма работает в прибыль")
    print("Рентабельность= ", (vir - izd) / vir)
    sot = int(input("Введите количество сотркдников: "))
    print("Прибыль на сотрудника= ", (vir - izd) / sot)
else:
    print("Фирма отработала в убыток")
