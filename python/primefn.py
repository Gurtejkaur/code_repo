from math import sqrt
def is_prime(n):
    root= round(sqrt(n))+1
    trail_factor =2
    for trial_factor in range(2,root):
        if n% trail_factor==0:
            return False
        return True
def main():
    max_value = int(input("please enter the number upto prime is tested"))
    for i in range(2, max_value+1):
        if is_prime(i):
            print(i, end = " ")
    print()
main()                    

    
