from math import sqrt
max_value = int(input("display prime is upto what value:"))
value=2
while value <= max_value:
    is_prime = True
    trail_factor =2
    root = sqrt(value)
    while trail_factor <= root:
        if value % trail_factor==0:
            is_prime = False
            break
        trail_factor+=1
    if is_prime:
        print(value,end='')
    value+=1
print()        
            
