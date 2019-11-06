def is_prime(n):
    from math import sqrt
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    trail_factor = 3
    root = sqrt(n)+ 1
    while trail_factor <=root:
        if n% trail_factor==0:
            return False
        trail_factor += 2
        return True
    
def non_neg(n):
    if n>0:
        return n

def count_elements(lst,predicate):
    count = 0
    for x in lst:
        if predicate(x):
            count+=1            
    return count
def main():
    try:
        print(count_elements([3,71,'x',7,'abcc'],non_neg))
        print(count_elements([3,2,4,7,6],is_prime))
        print(count_elements([3,8,'x',7,'xus'],non_neg))
    except TypeError:
        print("this argument is not accepted")
        

main()

                
    

        
        
        
