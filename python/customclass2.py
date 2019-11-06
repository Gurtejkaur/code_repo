class myclass:
    def __init__(self,num):
        self._private_var=num
        
def main():
    mc= myclass(10)
    mc._private_var=12
    print(mc._private_var)
    
main()        
        
