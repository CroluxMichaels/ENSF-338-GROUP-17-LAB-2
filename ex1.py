# Q1. 
# The code calculates the nth Fibonacci number using recursive approach. The base case is n = 0 and n = 1. 
# Then for other values of n, the function is called recursively and sum the results. 

# Q2. 
# No, this is not an example of divide-and-conquer algorithm because it does not divide the problem into smaller pieces. 
# Rather, it repeatedly calls the function to get the expected results. They basically have the same complexity as the
# original problem but doubling the amount of problems to solve. 

# Q3: Give an expression for the time complexity of the algorithm [0.2 pts]

# func(n) = 1 + 2*func(n-1)
# = 1 + 2 + 4*func(n-2)
# = 1 + 2 + 4 + 8*func(n-3)
# = sum of 2^i for i = 0 to i = n-1.
# = 2^n - 1 
# func(n) = O(2^n)

# Q4

