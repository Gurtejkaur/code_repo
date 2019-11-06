def gen(n):
    for i in range(n):
        yield i**2
        
for t in zip([1,2,3,4,5,6,7],gen(4)):
    print(t)
print()    
    

    
