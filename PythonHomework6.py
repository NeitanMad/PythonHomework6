def arithmetic_progression(element, difference, n):
    progression = [element + (_ - 1) * difference for _ in range(1, n + 1)]
    return progression


#Задача 30

element = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

some_progression = arithmetic_progression(element, difference, n)
print(some_progression)