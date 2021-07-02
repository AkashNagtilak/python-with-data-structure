#set is imutable we cannot modify set and all set in mutable but not one set valvue can mutable
#in the set there support mathamatically operations
#like \ union ,intersection & differance between set -, compare set =< , >=
# we can add in set suing add method and use of discard method we can remove the element from set

DaysA = set(['A','B','C','D','E'])
print(DaysA.add('XXX'))
print(DaysA.discard('A'))

for day in DaysA:
    print(day)
    
DaysB = set(['F','G','H','I','J'])

for days in DaysB:
    print(days)
    
union1 = DaysA | DaysB
print(union1)

intersection1 =DaysA & DaysB
print(intersection1)
    
differance = DaysA - DaysB
print(differance)

if(len(DaysA) <= len(DaysB)):
    print("DaysA is greater",DaysA)
else:
    print('DaysB is grater',DaysB)