''' It is very similer to deque in deque give fuctionality append and pop from left or right '''

import collections

DoubleEnded = collections.deque(['Mon','Tue','Thu'])
DoubleEnded.append("right")

print("deque list")
print(DoubleEnded)

print("Deque from right")
DoubleEnded.appendleft("Left")
print(DoubleEnded)

print("Pop From right")
DoubleEnded.pop()
print(DoubleEnded)

print("Pop form left")
DoubleEnded.popleft()
print(DoubleEnded)

