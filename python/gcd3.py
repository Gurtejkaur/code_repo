num1=int(input('please enter an integer'))
num2 =int(input('please enter another integer'))

print(gcd(num1,num2))       
    
def gcd(n1,n2):
    min = n1 if n1 < n2 else n2
    largest_factor=1
    for i in range(1,min+1):
        if n1%i==0 and n2%i==0:
            largest_factor = i
    return(largest_factor)        
    
