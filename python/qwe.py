def arthematic_cal(a,b,opr):
    if opr== '+' :
        c=a+b
    elif opr == '-' :
        c=a-b
    elif opr == '*' :
        c=a*b
    elif opr == '/' :
        c=a/b
    yield c



a=eval(input('1st number'))
b=eval(input('2st number'))
opr=input('arthematic opr')

df=arthematic_cal(a,b,opr)
print(next(df))
