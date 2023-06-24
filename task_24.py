n = int(input("Введите количество кустов: "))
list_1 = []

for i in range(n):
    m = int(input("Введите количество ягод: "))
    list_1.append(m)

list_2 = []

for j in range(n - 1):
    list_2.append(list_1[j - 1] + list_1[j] + list_1[j + 1])

list_2.append(list_1[-2] + list_1[-1] + list_1[0])
print(max(list_2))