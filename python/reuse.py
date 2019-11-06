def oscillate(m,n):
    for i in range(m,n+1):
        if i <= 0 or i > 0:
            yield i
def main():
    for n in oscillate(-3,5):
        print(n,-n, end = ' ')
    print()
    
main()    
    
            

