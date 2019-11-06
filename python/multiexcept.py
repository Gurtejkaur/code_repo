import random

for i in range(10):
    print("begining of the loop iteration",i)
    try:
        r=random.randint(1,3)
        if r==1:
            print(int('fred'))
        elif r==2:
            [][2]=5

        else:
            print(1/0)
            
    except (ValueError,ZeroDivisionError):
        print("problem with integer detection")
    except IndexError:
        print("list index is out of range")
    print("end of loop iteration", i)
      
    
        
