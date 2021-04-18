import os
import time
language = ''
while language != 'esc':
    print('=====SET KEYBOARD LANGUAGE====')
    language = input('pt -> (for portuguese)\nen -> (for english)\nesc -> to exit:')
    if(language == 'pt'):
        os.system('setxkbmap -model abnt2 -layout br -variant abnt2')
        os.system('clear')
        print('keyboard language set to Portuguese!')
    elif(language == 'en'):
        os.system('setxkbmap -layout us')
        os.system('clear')
        print('keyboard language set to English')
    elif(language == 'esc'):
        print('Byeeeeee')
        time.sleep(2);
        os.system('clear')
    else:
        os.system('clear')
        print('Invalid language option')
