import cProfile
import timeit

def sub_function(n):
    """Sub function that calculates the factorial of n"""
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    """Function that calls sub_function for numbers 0-9"""
    data = []
    for j in range(10):
        data.append(sub_function(j))
    return data

def third_function():
    """Function that calculates the square of numbers from 0 to 999"""
    return [i**2 for i in range(100000000)]

if __name__ == "__main__":

    # 3. 
    cProfile.run('test_function()')
    cProfile.run('third_function()')

"""
Answers to the questions:

1. Profiler is a tool that measures the time and frequency of function calls in a program, this also allows performance analysis. 

2. Profiling differs from benchmarking in that profiling provides a detailed execution times per function, 
while benchmarking measures overall execution time for performance comparison.

4. When the program was ran, the third_function() took 0.048 seconds, which is significantly higher. This is because it computes squares 
for 100 million numbers, which is an expensive operation. I think this is where most of the execution time is spent - third_function(). 
"""
