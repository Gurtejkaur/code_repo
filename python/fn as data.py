def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def evaluate (f,x,y):
    return f(x,y)
def main():
    print(add(2,3))
    print(multiply(2,3))
    print(evaluate(add,5,6))
    print(evaluate(multiply,5,6))
main()
