my_list=[1,2,3,4,5,6,7]
my_tuple=(1,2,3,4,5,6,7)

print("the list:",my_list)
print("the tuple:",my_tuple)

print("the first element in the list is",my_list[0])
print("the first element in the tuple is",my_tuple[0])

print("all elements in the list:")
for elem in my_list:
    print(elem, end=" ")
print()

print("all elements in the tuple:")
for elem in my_tuple:
    print(elem, end=" ")
print()

print("list_slice:",my_list[2:5])
print("tuple_slice:",my_tuple[2:5])

print("Try to modify the firt element in the list:" )
my_list[0] = 9
print("the list:",my_list)

print("Try to modify the firt element in the tuple:" )
my_list[0] = 9
print("the list:",my_tuple)

