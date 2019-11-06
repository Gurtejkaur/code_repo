try:
    f=open("C:\\Users\\Home-PC\\Desktop\\mywife.txt")
    sum=0
    try:
        for line in f:
            r=line.strip()
            sum += int(r)
            
    except Exception as er:
        print(er)
    print("sum=",sum)
        
except OSError:
    print("couldn't open file")
        

    
    
