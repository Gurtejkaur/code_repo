from random import randint
from functools import partial
def read_file(filename,n,val):
    count,read = 0,0
    with open("C:\\Users\\Home-PC\\Documents\\myfile.txt")as f:
        for value in f.readlines():
            read += 1
            if read > n:
                break
            if int(value)==value:
                count+=1
        return count
    
def roll(n,value):
    count=0
    for i in range(n):
        roll=randint(1,6)+randint(1,6)
        if roll==value:
            count+=1
    return count

def run_trails(f,n):
    for value in range(2,13):
        print("{:>3}:{:>6}".format(value,f(n,value)))
        
def main():
    number_of_trails=100
    print(".....pesudo number of trails....")
    run_trails(roll,number_of_trails)
    print("...actual experiment data...")
    try:
        run_trails(partial(read_file,'myfile.txt'),number_of_trails)
        
    except FileNotFoundError:
        print("cannot open the file myfile.txt")
        
    except PermissionError:
        print("you donot have access to the file myfile.txt")
    except OSError:
        print("can not read the file myfile.txt")
    except ValueError as e:
        print("data formattingError",type(e),e)
main()        
        
        
        
    
    
    

        
            
            
    
    

