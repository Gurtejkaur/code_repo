def non_neg_int(n):
    result=int(n)
    if result<0:
        raise ValueError(result)
    return result
while True:
    x = non_neg_int(input("please enter the non_negative integer value"))
    if x==999:
        break
    print("you enterd",x)
    
