max=500
def main():
    nonprimes =500*[False]
    nonprimes[0]=nonprimes[1]=True
    for i in range(2,max+1):
        if not nonprimes[i]:
            print(i,end= " ")
    for j in range(2*i,max+1,i):
        nonprimes[i]=True
print()
main()

        
        
    
