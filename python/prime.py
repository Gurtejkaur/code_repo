from math import sqrt
def is_prime(n):
    root= round(sqrt(n))+1
    trail_factor =2
    for trial_factor in range(2,root):
        if n% trail_factor==0:
            return False
        return True
