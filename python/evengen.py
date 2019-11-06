def evens_less_than(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield i
def main():
    for n in evens_less_than(12):
        print(n, end= ' ')
main()        
        
    
