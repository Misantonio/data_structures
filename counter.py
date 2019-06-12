from collections import Counter

c = Counter("Misael Antonio")
print(c)
print(c.most_common(3))
print("")

c = Counter([1,2,5,3,56,67,2,1,3,4,32,56,78,98])
print(c)
print(list(c.elements()))