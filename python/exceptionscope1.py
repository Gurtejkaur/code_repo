def get_int_in_range(low,high):
    need=True
    while need:
        try:
            val=int(input("Enter integer:"))
            if low > val or val > high:
                print("val is out of range try again")
            else:
                need=False
        except ValueError:
            print("value is not an valid integer,please try again")
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
main()    
        
