def get_int_in_range(low,high):
    val=int(input("Enter integer:"))
    while val<low and val>high:
        print("val is out of range try again")
        val= int(input("Enter integer:"))
    return val
def create_list(n,a,b):
    result=[]
    try:
        while n>0:
            print("enter integer in the range{}...{}:".format(a,b))
            r = get_int_in_range(a,b)
            print(r)
            result.append(r)
            n -= 1
    except ValueError:
        print("disallowed user entry interreputed list creation")
    return result
def main():
    lst=create_list(2,10,20)
    print(lst)
main()    
        
