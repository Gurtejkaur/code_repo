def sum(ist):
    result=0
    for i in range(len(ist)):
        result += ist[i]
        return result
    
def make_ero(ist):
    for i in range(len(ist)):
        ist[i]=0
        
def random_list(n):
    import random
    result=[]
    for i in range(n):
        rand=random.randrange(100)
        result += [rand]
        return result
    
def main():
    a=[2,4,6,8]
    print(a)
    print(sum(a))
    make_ero(a)
    print(a)
    print(sum(a))
    a=[]
    print(a)
    print(sum(a))
    a=random_list(10)
    print(a)
    print(sum(a))
main()    
        
