import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import random as rand
import timeit
import math

def linear_search(arr, key):
    found = -1
    for i in range(0, len(arr)):
        if arr[i] == key:
            found = i
            break
    return found

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid
            continue
        else:
            low = mid + 1
            continue
    return -1 

def logarithmic(x, a, b):
    return a*math.log(x) + b

list_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
avg_linear_times = []
avg_binary_times = []

# Bear in mind that this program takes about a minute to run. This is what happens when you have to run the linear search
# algorithm 100,000 times for arrays of more than 30,000 elements.


for i in list_sizes:
    print(f"Computing for ordered vector of {i} elements")
    vector = []
    linear_times = []
    binary_times = []
    for j in range(0, i):
        vector.append(j)
    for n in range(0, 1000):
        find = rand.randrange(0, i)
        linear_times.append(timeit.timeit(stmt=lambda: linear_search(vector, find), number=100)/100)
        binary_times.append(timeit.timeit(stmt=lambda: binary_search(vector, find), number=100)/100)
    avg_linear_times.append(sum(linear_times)/len(linear_times))
    avg_binary_times.append(sum(binary_times)/len(binary_times))
print(avg_linear_times)
print(avg_binary_times)


# Ask about it tomorrow in the lecture. This one is not making a lot of sense yet, because it takes a long time to run it!
# Here is a shorter version of the same code...


"""
for i in list_sizes:
    print(f"Computing for ordered vector of {i} elements")
    vector = []
    for j in range(0, i):
        vector.append(j)
    find = rand.randrange(0, i)
    avg_linear_times.append(timeit.timeit(stmt=lambda: linear_search(vector, find), number=100)/100)
    avg_binary_times.append(timeit.timeit(stmt=lambda: binary_search(vector, find), number=100)/100)
print(avg_linear_times)
print(avg_binary_times)
"""
plt.figure()
slope, intercept = np.polyfit(list_sizes, avg_linear_times, 1)
plt.scatter(list_sizes, avg_linear_times)
linevalues = [slope * x + intercept for x in list_sizes]
plt.plot(list_sizes, linevalues, 'r')
plt.xlabel("Size of Vector")
plt.ylabel("Average search time (s)")
plt.show()

plt.figure()

"""
bin_constants = sp.optimize.curve_fit(logarithmic, list_sizes, avg_binary_times)
bin_fit_a = bin_constants[0][0]
bin_fit_b = bin_constants[0][1]

binary_fit = []
for i in list_sizes:
    binary_fit.append(logarithmic(i, bin_fit_a, bin_fit_b))
plt.plot(list_sizes, binary_fit)
"""

plt.plot(list_sizes, avg_binary_times)

plt.xlabel("Size of Vector")
plt.ylabel("Average search time (s)")
plt.show()