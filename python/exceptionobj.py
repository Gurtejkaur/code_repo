import random

for i in range(10):
    print("begining of the loop iteration",i)
    try:
        r=random.randint(1,4)
        if r==1:
            print(int('fred'))
        elif r==2:
            [][2]=5
        elif r==3:
            print({}[1])
        else:
            print(1/0)
            
    except ValueError as e:
        print("problem with value ==>",type(e),e)
    except ZeroDivisionError as e:
        print(" problem with divison ==>",type(e),e)
    except IndexError as e:
        print("list index is out of range==>",type(e),e)
    except Exception as e: #catch any other type of exception
        print("this progam has encountered a problem==>", type(e),e)
        print("end of loop iteration", i)
      
