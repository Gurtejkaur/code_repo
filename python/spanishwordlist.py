#word='*'
#while word!= '':
    #word = input("enter the spanish word:")
    #if word=='uno':
        print('one')
    #elif word=='dos':
        print('two')
    #elif word=='hrees':
        print('three')
    #elif word=='cuatro':
        print('four')
    #elif word=='cinco':
        print('five')
    #else:
        #print('???')
        
translator={'uno':'one',
            'dos':'two',
            'hrees':'three'',
            'cuatro':'four',
            'cinaco':'five'}
word='*'
while word!= '':
    word=input('enter the spanish word:')
    if word is in translator:
        print(translator[word])
    else:
        print('???')
            
            
        
