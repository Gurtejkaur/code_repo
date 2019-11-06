class FunctionTester:
    def __init__(self):
        self.__error_count= self.__total_count=0
        print(".............................")
        print("........testing..............")
        print(".............................")
        
    def check(self,msg,expected,func,*args):
        result=True
        print(" ", msg," ",end="")
        self.__total_count+=1
        
        try:
            actual= func(*args)
            if expected == actual:
                print("ok")
            else:
                self.__error_count=+1
                print("failed! Expected:",expected,"actual:",actual)
                
        except Exception as e:
            self.__error_count+=1
            print("Exception",e)
            result=False
        return result
    
    def report_result(self):
        print("testing statistics")
        print("+-------------------------------------- " )
        print("|", self.__total_count, " tests run" )
        print("|", self.__total_count - self.__error_count, " passed")
        print("|", self.__error_count, " failed")
        print("+-------------------------------------- " )





        
