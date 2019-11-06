def sum_postive (a):
    if isinstance(a,list): 
        b=0
        for i in a:
            b+=i
    else:
        b="given variable is not list type"
    return b
#print(sum_postive(lst))
def count_evens(lst):
    count=[]
    if isinstance(lst,list):
        for i in lst:
            if i%2==0:
                count.append(i)
        b=len(count)
    else:
        b="given data is not a list"
    return b    
#c=[3,5,4,-1,8,10,9,18,13]        
#print(count_evens(c))
def print_big_enough(a,b):
    if isinstance(a,list) and isinstance(b,int):
        for i in a:
            if i>b:
                print(i)
#c=[45,42,1,2]
#d=5
#print_big_enough(c,d)
def small_number(a):
    if isinstance(a,list):
        b=max(a)
        for i in range(1,b):
             if i not in a:
                 h=i
                 break
    return h
print(small_number([5,3,1]))
print(small_number([5,4,1,2]))
print(small_number([3,2]))


