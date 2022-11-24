import random
from datetime import datetime
import copy

def bubble(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr1 = [random.randint(0, 100) for i in range(random.randint(1, 100))]
arr2 = copy.copy(arr1)
first_start_time = start_time = datetime.now()
print(f'Несортированный массив: {arr1}')
bubble(arr1)
print(f'Отсортированный массив: {arr1}')
second_start_time = start_time = datetime.now()
print(f'Время выполнения: {second_start_time - first_start_time}')
print(f'Несортированный массив: {arr2}')
arr2.sort()
print(f'Отсортированный массив: {arr2}')
print(f'Время выполнения: {datetime.now() - second_start_time}')