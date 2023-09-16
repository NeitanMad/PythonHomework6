def arithmetic_progression(element, difference, n):
    progression = [element + (_ - 1) * difference for _ in range(1, n + 1)]
    return progression


#������ 30

element = int(input("������� ������ ������� ����������: "))
difference = int(input("������� �������� ����������: "))
n = int(input("������� ���������� ���������: "))

some_progression = arithmetic_progression(element, difference, n)
print(some_progression)