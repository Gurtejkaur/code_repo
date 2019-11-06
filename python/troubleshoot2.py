print(" please help,my computer does not work")
done = False
while not done:
    print(" does the computer makes any sounds")
    choice = input(" or it makes any power")
    if choice == 'n':
        choice = input("is it plugged in")
        if choice=='n':
            print('please plug it in')
        else:
            print('it is plugged in')
            choice = input(' is switch is on')
            if choice=='n':
                print('please, on it')
            else:
                print('switch is on')
                choice = input('is any problem in fuse')
                if choice == 'n':
                    choice = input('is outer circuit is ok')
                    if choice == 'n':
                        print('please consult a technician')
                    else:
                        print('outer circuit is ok')
                else:
                    print(" check the fuse")
                    
    else:
        print("power is on, consult to an technician")
        done= True
