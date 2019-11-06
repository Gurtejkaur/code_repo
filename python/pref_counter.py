from time import perf_counter
sum = 0
start_time = perf_counter()
for n in range(1,100000001):
    sum += n 
elapsed = perf_counter()- start_time
print("sum",sum,"time",elapsed)
