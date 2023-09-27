import time
import random
import numpy as np
import matplotlib.pyplot as plt

np_sort = []
base_sort = []
array1 = []
size_of_arrays=[]
count = 0

for k in range (10, 5000000, 100000):
    array = np.random.sample(k)
    start = time.time()
    np.sort(array)
    end = time.time() - start
    np_sort.append(end)

    for i in range (k):
        array1.append(random.randint(-500,500))
    start = time.time()
    array1.sort()
    end = time.time() - start
    base_sort.append(end)
    size_of_arrays.append(len(array))
    count+=1
    print(count,"/",5000000-10)

plt.plot(size_of_arrays, base_sort, label = 'Python list')
plt.plot(size_of_arrays, np_sort, label = 'NumPy array')
plt.title('Скорость встроенной сортировки и сортировки NumPy')
plt.ylabel('Время')
plt.xlabel('Количество элементов')
plt.grid()
plt.legend()
plt.show()
