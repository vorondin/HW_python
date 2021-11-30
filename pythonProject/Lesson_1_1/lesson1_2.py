sekvvod = int(input("Введите секунды: "))
min = (sekvvod % 3600) // 60
h = sekvvod // 3600
sec = (sekvvod % 3600) % 60
print(f"введенное значение состоит из часов {h}, минут  {min}, секунд  {sec}")
