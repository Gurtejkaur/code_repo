def fun1():
    try:
        print("try code")
    except:
        print("exception handling code")
    else:
        print("no exception raised code")
        x=int('a')
        
def fun2():
    try:
        print("try code")
        print("no exception raised code")
        x=int('a')
    except:
        print("exception handling code")
        
print("calling fun2")
fun2()
print('......')
print("calling fun1")
fun1()
