# Exercise 2 - Interpolation Search

## Answers

### 1. Mention at least two aspects that make interpolation search better than binary search.
- **Faster when data is uniformly distributed**: Interpolation can achieve an average-case complexity of \(O(\log \log n)\) compared to \(O(\log n)\) when using binary search.
- **Can adapt to data distribution**: In binary search, it always splits the array in half, interpolation search "calculates" the position based on values, that can reduce the number of comparisons. 

### 2. Interpolation search assumes that data is uniformly distributed. What happens if this data follows a different distribution? Will the performance be affected? Why? 
If the data is not uniformly distributed, position estimations may be inaccurate and this can lead to increased search time, and in the worst case, resulting to \(O(n)\), which is the same as linear search. This is because in interpolation search, the key assumption is that the values are evenly spaced, which allows it to approximate the index effectively. This in return results in more iterations.

### 3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?
The part of the code that would be affected is: 
  ```python
  position = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
  ```
Given this, a different functon should be used to approximate `position` which should be based on the actual distribution of data. 

### 4. When is linear search your only option for searching data as binary and interpolation search may fail? 
Binary and interpolation search both require sorted data. If the data is unsorted, only linear search can be used.
If data is heavily grouped or there is an irregular pattern, interpolation search might perform worse than linear search.

### 5. In which case will linear search outperform both binary and interpolation search, and why? 
Linear search may be faster when dealing with small datasets due to lower overhead compared to interpolation and binary search.
Linear search can also outperform both binary and iterpolation search if the given data are nearly sorted or partially sorted, beacuse linear search cab find it in constant time, while other ones require extra computations. 

### 6. Is there a way to improve binary and interpolation search to solve this issue? 
Yes. It can be done by combining linear search with binary or interpolation search. Another way is to modify interpolation search to use a different positional estimation formula based on the actual data distribution. 


