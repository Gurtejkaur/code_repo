def get_int_in_range(low,high):
    val=int(input("Enter integer:"))
    if low > val or val > high:
        print("val is out of range try again")
        val= int(input())
    return val
def create_list(n,a,b):
    result=[]
    while n>0:
        print("enter integer in the range{}...{}:".format(a,b))
        r = get_int_in_range(a,b)
        print(r)
        result.append(r)
        n -= 1
    return result
def main():
    
        lst=create_list(2,10,20)
        print(lst)
try:
    main()
except Exception:
    print("can not create a list")
        
        
