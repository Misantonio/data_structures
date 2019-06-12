from collections import deque

d = deque()

d.append(5)
d.append(2)
d.append(3)
print("A", d)

d.appendleft(3)
d.appendleft(4)
d.appendleft(7)
print("B", d)

print("Count", d.count(3))

d.pop()
print("C", d)

d.popleft()
print("D", d)

d.clear()
print("E", d)

d.append("a")
d.append([1,2,3])
d.extend([1,2,3])
print("F", d)

d.clear()
d.append("a")
d.appendleft([1,2,3])
d.extendleft([1,2,3])
print("G", d)

d.remove(1) # removes first ocurrence
print("H", d)