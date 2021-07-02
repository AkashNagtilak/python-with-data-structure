''' Array Is Collection Of similar data type array is base from derived data type.which stored valude in one objects.
this is seprated by comma in paython we import array class . There are 5 operations can work 
1. Traberse
2.insertion
3.deletion
4.update
5.serch

sysntax of array in paython
array objects = array('type code',[array])

'''
from array import *

array_display = array('i',[1,2,3,4,5])
print('Insert Array :')
array_display.insert(1,0)
print('Array Display')
array_display.remove(5)
print('Array Serach By Index')
print(array_display.index(1))
print("array_display by index")
print(array_display[0])
print('for  loop')
array_display[2] = 6
for array_loop in array_display:
    print(array_loop)



 

