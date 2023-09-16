from random import randint

def find_indexes(list, min_value, max_value):
    indexes = []
    for i in range(len(list)):
        if min_value <= list[i] <= max_value:
            indexes.append(i)
    return indexes

def arithmetic_progression(element, difference, n):
    progression = [element + (_ - 1) * difference for _ in range(1, n + 1)]
    return progression


#������ 30

element = int(input("������� ������ ������� ����������: "))
difference = int(input("������� �������� ����������: "))
n = int(input("������� ���������� ���������: "))

some_progression = arithmetic_progression(element, difference, n)
print(some_progression)

#������ 32

list = [randint(-100, 100) for _ in range(10)]

# �������� ��������
min_value = 33
max_value = 200

index = find_indexes(list, min_value, max_value)
print(index)
