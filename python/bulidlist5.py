def main():
    sum=0.0
    number_of_enteries = 5
    numbers=[]
    print("please enter", number_of_enteries,
          "numbers:")
    for i in range(1,number_of_enteries):
        num = float(input("enter number"+str(i)+":"))
        numbers+= [num]
        sum += num
    print( "numbers enterd:")
    for num in numbers:
        print(num, end=" ")
    print()
    print("average",sum/number_of_enteries)
main()

        
         
