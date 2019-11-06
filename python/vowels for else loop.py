word = input('enter text')
vowel_count=0
for c in word:
    if c=='a' or c=='e' or c=='i' or c=='0' or c=='u':
        print(c,',',sep='',end='')
        vowel_count+=1
    elif c=='X' or c=='x':
        print('x does not allowed')
        break
else:
    print('(',vowel_count,'vowels)')
        
