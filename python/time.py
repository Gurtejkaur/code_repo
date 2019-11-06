print(("please enter four integers"))
num1 = int(input('enter the first integer'))
num2 = int(input('enter the seccond integer'))         
num3 = int(input('enter the third integer'))
num4 = int(input('enter the fourth integer'))
# compute the maximum value.
max = num1
if num2 >= max:
    max = num2
if num3 >= max:
    max = num3
if num4 >= max:
    max = num4
print("maximum integer value is", max)  
