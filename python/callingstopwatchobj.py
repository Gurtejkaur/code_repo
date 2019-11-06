from time_obj_class import stopwatch
from math import sqrt

def count_primes(n):
    timer=stopwatch()
    timer.start()
    
    count=0
    root= round(sqrt(n))+1
    trail_factor =2
    for trial_factor in range(2,root):
        if n% trail_factor==0:
            break
        else:
            count+=1
    timer.stop()
    print("Count =", count, "Elapsed time for algo1 : " , timer.elapsed(), "seconds" )

def seiven(n):
    timer= stopwatch()
    timer.start()
    
    nonprimes =n*[False]
    nonprimes[0]=nonprimes[1]=True
    count=0
    for i in range(2,n):
        if not nonprimes[i]:
            count+=1
    for j in range(2*i,n,i):
        nonprimes[j]=True
    timer.stop()
    print("Count =", count, "Elapsed time for algo2: " , timer.elapsed(), "seconds" )

def main():
    count_primes(2000000)
    seiven(2000000)
main()    
    
            
