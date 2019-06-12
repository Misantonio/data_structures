# This is important for python 2

from collections import OrderedDict

dict1 = {}

dict1['name'] = "Misael"
dict1['age'] = 24
dict1['nationality'] = "Mexican"
dict1['weight'] = 60

print(dict1)

ord_dict1 = OrderedDict()

ord_dict1['age'] = 24
ord_dict1['name'] = "Misael"
ord_dict1['nationality'] = "Mexican"
ord_dict1['weight'] = 60

print(ord_dict1)

print(OrderedDict(dict1) == ord_dict1)