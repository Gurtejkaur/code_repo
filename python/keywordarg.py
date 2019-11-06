'''print("begin")
try:
    x=int(input())
    print(x)
except Exception:
    print("wrong")
else:
    print("wow")
finally:
    print("done")
    
print("end") '''

'''try:
    f()
except Exception:
    print(1)
except ValueError:
    print(2)'''

'''def product(*args):
    result=1
    for elem in args:
        result *= elem
    return result
def main():
    print(product(2.5,2,10))
    print(product(2,8.9))
    print(product())
main() '''

'''def zero_sum(*args):
    sum=0
    for arg in args:
        sum += arg
    if sum == 0:
        return True
    else:
        return False
def main():
    print(zero_sum(2,3,-5))
    print(zero_sum(2,3,-10,4))
    print(zero_sum())
main()'''
d={3:0, 5:1, 10:1, 8:2, 15:4}
print(d)
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values(71):
    print(x)
    
    





    

    
    
    
