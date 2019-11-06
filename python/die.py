from random import randrange
def show_die(spots):
    print("+..........+")
    if spots ==1:
        print("|     |")
        print("|    *|")
        print("|     | *")
    elif spots ==2:
        print("|*    |")
        print("|     |")
        print("|    *|")
    elif spots ==3:
        print("|    *|")
        print("|  *  |")
        print("|*    |")
    elif spots ==4:
        print("| **   |")
        print("|      |")
        print("| **   |")
    elif spots ==5:
        print("| **   |")
        print("| *    |")
        print("| **   |")
    elif spots ==6:
        print("| ***|")
        print("|    |")
        print("| *** |")
    else:
        print("**error:illegal die spots ***")
        print("+......+")
def roll():
    return randrange(1,7)
def main():
    for i in range (0,3):
        show_die(roll())
main()
