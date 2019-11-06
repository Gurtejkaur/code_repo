def load_data(filename):
    with open("C:\\Users\\Home-PC\\Desktop\\python auto notes\\jatinder.txt",'r') as f:
        for line in f:
            print(int(line))
                  
def store_data(filename):
    with open("C:\\Users\\Home-PC\\Desktop\\python auto notes\\jatinder.txt",'w') as f:
        number =0
        while number != 999:
            number = int(input("please enter the number"))
            if number != 999:
                f.write(str(number)+'\n')
            else:
                break
def main():
    done = False
    while not done:
        cmd = input('s)ave l)oad Q)uit:')
        if cmd =='s' or cmd =='S':
            store_data(input("please enter the file name"))
        elif cmd =='l' or cmd =='L':
            load_data(input("please enter the file name"))
        elif cmd =='Q' or cmd =='q':
            done = True
            
main()            
