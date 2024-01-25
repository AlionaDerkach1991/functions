# Функція, що обчислює факторіал кожного елементу списка цілих
import math
list1 = [x for x in range(1, 10)]
list2 = [math.factorial(x) for x in range(1, 10)]
print(list2)