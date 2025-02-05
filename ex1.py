import timeit
import matplotlib.pyplot as plt

# Q1. What does this code do? [0.1 pts]
# The code calculates the nth Fibonacci number using recursive approach. The base case is n = 0 and n = 1. 
# Then for other values of n, the function is called recursively and sum the results. 

# Q2. Is this an example of a divide-and-conquer algorithm (think carefully about this one)? [0.1 pts]
# No, this is not an example of divide-and-conquer algorithm because it does not divide the problem into multiplicatively
# smaller pieces. Rather, it repeatedly calls the function to get the expected results. 
# The two 'smaller' problems basically have the same complexity as the original problem but doubling the amount of problems to solve. 

# Q3. Give an expression for the time complexity of the algorithm [0.2 pts]

# func(n) = 1 + 2*func(n-1)
# = 1 + 2 + 4*func(n-2)
# = 1 + 2 + 4 + 8*func(n-3)
# = sum of 2^i for i = 0 to i = n-1.
# = 2^n - 1 
# func(n) = O(2^n)

# Q4. Implement a version of the code which uses memoization to improve performance [0.2 pts]
fiblist = [0, 1]

def fib(n):
    if len(fiblist) > n:
        return fiblist[n]
    else:
        fiblist.append(fib(n-1) + fib(n-2))
        return fiblist[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# Q5. Give an expression for the time complexity of the optimized algorithm [0.2 pts]
# The complexity this time is O(n) because each fibonacci number is calculated exactly once.
# After that it is pulled from the list if needed to calculate higher values of fib.
# Because fib(0) and fib(1) are already known, this results in n-2 operations, meaning a linear 
# relationship between the input size and number of operations.

# Q6. Time the original code and your improved version, for all integers between 0 and 35, 
# and plot the results (output plots must be called ex1.6.1.jpg and ex1.6.2.jpg) [0.2 pts]

functimes = []
fibtimes = []
n = []
for i in range(0, 36):
    n.append(i)
    functimes.append(timeit.timeit(stmt=lambda: func(i), number=1))
    fibtimes.append(timeit.timeit(stmt=lambda: fib(i), number=1))

plt.figure()
plt.plot(n, functimes)
plt.xlabel("Fibonacci Number")
plt.ylabel("Computation Time")
plt.savefig("ex1.6.1.jpg")
plt.figure()
plt.plot(n, fibtimes)
plt.xlabel("Fibonacci Number")
plt.ylabel("Computation Time")
plt.savefig("ex1.6.2.jpg")
