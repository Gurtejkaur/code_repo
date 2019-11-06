#help my computer does not work
print("does the computer makes any sounds")
choice = input('or it shows any light')
if choice == 'n':
    choice = input('is it plugged in? \n')
    if choice =='n':
        print('plug it in if the problem persists')
        print('please run this program again')
    else: # it is plugged in
        print("it is plugged in") 
        choice = input('is switch is on')
    if choice == 'n':
        print('please on the switch,if the problem persists')
        print('please run this program again')
    else: # switch is on
        print("switch is on")
        choice = input('is the any problem in fuse')
    if choice =='n':
       choice = input('is the outer circut is ok?')
       if choice =='n':
            print('please check the circuit')
       else:
            print('there is no problem in the outer circuit')
    else: 
            print('fuse is not working')
            print('please called to an technician')
else:
    print('power is on, please called to an technician')                
                      
                      


                      
    
                  
            
