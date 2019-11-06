a=[2,3,4,5,6]
print("prefixis of", a , "are:")
for i in range(0,len(a)+1):
    print("<",a[0:i],">")
print("......................")
for i in range(0,len(a)+1):
    print("<",a[i:len(a)+1],">")
    
