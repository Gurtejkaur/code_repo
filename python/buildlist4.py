from math import sqrt
def is_prime(n):
    trail_factor = 2
    root = round(sqrt(n))+1
    for trail_factor in range(2,root):
        if n % trail_factor == 0:
            return False
    return True

def prime_sequence(begin,end):
    for value in range (begin,end+1):
        if is_prime(value):
            yield value
def main():
    primes = list(prime_sequence(20,50))
    print(primes)
main()    
    

        
    
    
        
