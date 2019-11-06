try:
    f=open("C:\\Users\\Home-PC\\Desktop\\mywife.txt")
    
except OSError:
    print("couldn't open file")
else:
    sum=0
    try:
        for line in f:
            sum += int(line)
    except Exception as er:
        print(er)
        
finally:
    f.close()
    print("sum=",sum)
    
