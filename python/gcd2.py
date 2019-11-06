def gcd(n1,n2):
    min = n1 if n1 < n2 else n2
    largest_factor=1
    for i in range(1,min+1):
        if num1%i==0 and num2%i==0:
            largest_factor = i
    return(largest_factor)        
    
def main():
    for num1 in range(0,101):
        for num2 in range (0,101):
            print("gcd of", num1, "and", num2, "is",gcd(num1,num2))
         
main()    
