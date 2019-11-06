from time import perf_counter
from math import sqrt
def count_primes(n):
    start=perf_counter()
    count=0
    for val in range(2,n):
        root= round(sqrt(val))+1
        for trail_factor in range(2,root):
            if val%trail_factor==0:
                break
            else:
                count += 1
            
    stop = perf_counter()
    print("count=",count,"elapsed time=",stop-start,"seconds")
print()
def sever(n):
    start=perf_counter()
    max=n
    nonprimes =n*[False]
    count=0
    nonprimes[0]=nonprimes[1]=True
    for i in range(2,max):
        if not nonprimes[i]:
            count+=1
            
            
        for j in range(2*i,max,i):
            nonprimes[i]=True
        
    stop=perf_counter()
    print("count=",count,"elapsed time=",stop-start,"seconds")

print()
def main():
    count_primes(2000)
    sever(2000)
main()    


        
        
