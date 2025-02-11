**Exercise 4 Answers**

1. Algorithm to Find Room EY128

Since we only have limited information from the sign, we can use a linear search approach to check each room sequentially until we find EY128.

2. Number of Steps

A "step" in this context could be moving from one room to the next while checking the room number. We could follow the hallway to the left since it indicates rooms 100-130, counting each room until we reach EY128. Since we start from the entrance, this would mean we would take about 15 steps.

3. Scenario Classification

This is neither the best-case nor the worst-case scenario. The best-case scenario would involve finding the room immediately, while the worst-case scenario would require searching the longest possible path before finding the room.

4. Best-Case and Worst-Case Scenarios

The best-case scenario is the room is the first one encountered after following the sign. The worst-case scenario is the room is the last one in the search path. 

5. Optimizing the Algorithm with Memorization

After memorizing the layout, we can improve efficiency by:
- Using interpolation search: estimate the approximate position and get to it immediately instead of checking each room
- Using a binary search approach: after checking each room and memorizing the layout, we now know the order and can possibly divide the hallway into sections and narrow down room EY128 faster
- Using landmarks or reference points: after memorizing the layout, we can use any distinct reference points in the hallways to help navigate quicker
