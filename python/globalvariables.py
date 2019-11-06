def help_screen():
    """
    displays information about how the program works
    accepts no parameter
    return nothing
    """
    print("Add: adds two numbers")
    print("subtract: subtract twoo numbers")
    print("print:displays the result of the latest operation")
    print("help:display this help screen")
    print("quit:exit the program")
def menu():
    """
    displays the menu.
    
    accepts no parameter.
    and return the user input.
    """
    return input("=== A)dd S)ubtract p)rint H)elp Q)uit ===")
result=0.0
arg1=0.0
arg2=0.0
def get_input():
    global arg1, arg2
    arg1= float(input("enter the arg1"))
    arg2= float(input("enter the arg2"))
def report():
    print(result)
def add():
    global result
    result= arg1 + arg2
def subtract():
    global result
    result= arg1-arg2

def main():
    """
    runs a command loop that allows user to perform simple arithimetic
    """
    result = 0.0
    done= False
    while not done:
        choice= menu()
        if choice=="A" or choice=="a":
            get_input()
            add()
            report()
        elif choice=="S" or choice=="s":
            get_input()
            subtract()
            report()
            
        elif choice=="p" or choice=="P":
            print(result)    
        elif choice=="H" or choice=="h":
            help_screen()
        elif choice=="Q" or choice=="q":
            done= True
        
main()    
