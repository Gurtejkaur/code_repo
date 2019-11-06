from math import sqrt
from time import perf_counter
max_value = 10000
count= 0
value = 2 
start_time = perf_counter()
while value <= max_value:
    is_prime = True
    trail_factor=2
    root= sqrt(value)
    while trail_factor <=root:
        if value % trail_factor==0:
            is_prime = False
            break
        trail_factor+=1
    if is_prime:
        print(value, end=' ')
        count+=1
    value+=1
print()        
elapsed = start_time - perf_counter()
print("count",count,"time",elapsed,"seconds")
