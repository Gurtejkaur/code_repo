translator={'uno':'one',
            'dos':'two',
            'hrees':'three',
            'cuatro':'four',
            'cinaco':'five'}
word='*'
while word!= '':
    word=input('enter the spanish word:')
    if word in translator:
        print(translator[word])
    else:
        print('???')
          
