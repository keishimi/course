import numpy as np

# Создание массива
array = np.array([1, 2, 3, 4, 5])
ar = np.array([[1,2,3, 25],[4,5,6, 52]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

sum_array = np.sum(array)
sqrt_array = np.sqrt(array)

print(f"Массив: {array}")
print(f"Сумма элементов массива: {sum_array}")
print(f"Косинус элементов: {sqrt_array}")
print(f"Размер каждого элемента: {ar.itemsize}")
print(type(ar))
print(b[0, 1:4:2])
