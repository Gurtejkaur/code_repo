from math import sqrt
list = [4,5,9,7,8]
print(list[2])

list[1]=(list[2]+list[3])/2
print(list)

x=16
y=7.3
list[2], list[4]= sqrt(x), x+2*y
print(list)
