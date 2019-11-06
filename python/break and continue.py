    
sum=0 
done=False
while not done:
    value=int(input("please enter the value"))
    if value<0:
        print("value is negative,ignored")
    else:
        if value!=999:
            print( value,"value is tallying")
            sum+= value
        else:
            done = (value==999)      
    print('sum=',sum)
              
