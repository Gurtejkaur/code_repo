d={'Fred':44,'ella':39,'owen':45,'hello':89}
print(d)

for k in d.keys():
    print(k,sep= ",", end = " ")
print()

for k in d:
    print(k,end = " ")
print()

for v in d.values():
    print(v,end=" ")
print()

for k,v in d.items():
    print(k,v)
print()    
