# Q3: Give an expression for the time complexity of the algorithm [0.2 pts]

# func(n) = 1 + 2*func(n-1)
# = 1 + 2 + 4*func(n-2)
# = 1 + 2 + 4 + 8*func(n-3)
# = sum of 2^i for i = 0 to i = n-1.
# = 2^n - 1 
# func(n) = O(2^n)
