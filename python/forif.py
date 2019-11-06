for i in range(10):
    print(i, end=' ' ) # Print i as served by the range object
    if i == 5:
        i = 20 # Change i inside the loop?
    print('({}) '.format(i), end=' ' )

word= input('enter a word')
for letter in word:
    print(letter)
