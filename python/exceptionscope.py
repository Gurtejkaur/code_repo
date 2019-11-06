def get_int_in_range(low,high):
    val=int(input())
    while val<low or val>high:
        print("val is out of range try again")
        val= int(input())
        return val
def create_list(n,min,max):
    result=[]
    while n>0:
        print("enter integer in the range{}...{}:".format(min,max))
        result.append(get_int_in_range(min,max))
        n-=1
    return result
def main():
    lst=create_list(2,10,20)
    print(lst)
main()    
        
