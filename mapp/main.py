import collections
dict1 = {"Akash":"Nagtilak","Rushikesh":"Nagtilak"}
dict2 = {"Ishan":"Lokhande","Mufasa":"Dog"}

res= collections.ChainMap(dict1,dict2)

for key,value in res.items():
    print('######################################')
    #print("{} = {}".format(key,value))
    print("{}".format(key))
    print('#####################################')
    print("{}".format(value))
print()