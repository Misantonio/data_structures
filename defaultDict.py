from collections import defaultdict, Counter

d = {"name": "Misael", "age": 24}

try:
    print(d['height'])
except KeyError as e:
    print("Key does not exists")

def_dict = defaultdict(lambda: "Default Value")
def_dict['name'] = "Misael"
def_dict['age'] = 24

print(def_dict['name'])
print(def_dict['height'])
print("")

s = [('yellow', 1), ('blue', 2), ('yellow', 3)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
print(d.items())
print("")

s = "Mississippi"

d = defaultdict(int)

for k in s:
    d[k]+=1
print(d.items())
print(Counter(s))