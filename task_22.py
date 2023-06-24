n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
set_1 = set()
set_2 = set()
print(type(set_2))
for i in range(n):
    num_1 = int(input("Введите число для первого множества: "))
    set_1.add(num_1)
for j in range(m):
    num_2 = int(input("Введите число для второго множества: "))
    set_2.add(num_2)
print(set_1.intersection(set_2))