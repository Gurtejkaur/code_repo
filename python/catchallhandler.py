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
            
    except ValueError:
        print("cannot convert integer")
    except ZeroDivisionError:
        print(" divison by zero is not possible")
    except IndexError:
        print("list index is out of range")
    #except Exception:  catch any other type of exception
        #print("this progam has encountered a problem")
    except:
        print("this program has encounterd a problem")
        
        
    print("end of loop iteration", i)
      
