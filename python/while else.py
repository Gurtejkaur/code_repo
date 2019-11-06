count=sum=0
print('please provide five numbers')
while count < 5:
    value= float(input('enter number'))
    if value<0:
        break;
    count+=1
    sum+=value
if count<5:
    print("negative numbers are not acceptable")
else:
    print('average = ', sum/count)
