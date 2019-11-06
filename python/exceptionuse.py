sum=0
inti = 0
lst=[1,2,3,4,5]
try:
    while True:
        for i in lst:
            sum += lst[i]
            i+=1
except IndexError:
    pass
print("sum=",sum)
    
