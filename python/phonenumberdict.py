contacts={}
running = True
while running:
    command = input('A)dd D)elete L)ookup Q)uit:')
    if command == 'A' or command == 'a':
        name=input('enter new name:')
        print("enter phone number for name",name,end='')
        number = input()
        contacts[name]=number
              
    elif command == 'd' or command == 'D':
        name=input('enter name to delete:')
        del contacts[name]
        
    elif command == 'L' or command == 'l':
        name=input('enter name to lookup:')
        print(name,contacts[name])
        
    elif command == 'Q' or command == 'q':
        running= False
        
    elif command == 'dump':
        print(contacts)
    else:
        print("command is nat valid")
        
