from time import perf_counter
max_value = 10000
count=0
start_time = perf_counter()
for value in range(2,max_value+1):
    is_prime = True
    for trail_factor in range(2,value):
        if value % trail_factor==0:
            is_prime = False
            break
        trail_factor+=1
    if is_prime:
        print(value, end=' ')
    count+=1
print()        
elapsed = start_time - perf_counter()
print("count",count,"time",elapsed,"seconds")
