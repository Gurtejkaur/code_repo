def making_list():
    result = []
    in_val = 0
    done= False
    while not done:
        in_val= int(input("enter value:"))
        if in_val>= 0:
            result += [in_val]
        else:
            done= True
        
    return result
def main():
    col= making_list()
    print(col)
    
main()    
    
    
    
               
