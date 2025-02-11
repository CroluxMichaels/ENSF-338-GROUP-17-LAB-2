import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import random as rand
import timeit

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

plt.figure()
slope, intercept = np.polyfit(list_sizes, avg_linear_times, 1)
plt.scatter(list_sizes, avg_linear_times)
linevalues = [slope * x + intercept for x in list_sizes]
plt.plot(list_sizes, linevalues, 'r')
plt.xlabel("Size of Vector")
plt.ylabel("Average search time (s)")
plt.show()

plt.figure()
plt.plot(list_sizes, avg_binary_times)

plt.xlabel("Size of Vector")
plt.ylabel("Average search time (s)")
plt.show()

# Question 4:
#
# Function 1 (Linear Search)
# Type of function: linear
# Arguments: list_sizes, which is the number of elements in an ordered vector, and avg_linear_times, which is the time it takes on average
# to find a randomly selected element of the vector using linear search.
# The results are as expected, because the complexity of linear search is O(n), and the time it takes on average increased linearly with
# vector size.

# Function 2 (Binary Search)
# Type of function: logarithmic
# Arguments: list_sizes (same as Function 1), and avg_binary_times, which is similar to avg_linear_times but with binary search.
# The results are also as expected. The complexity of binary search is O(log(n)), so even though the time it took to find a random
# element increases with vector size, it does not increase as quickly as with linear search. This was clearly reflected in the 
# graph, which shows the time taken very slowly increase to the point where it could find the random element more than 100 times
# faster than linear search on average.