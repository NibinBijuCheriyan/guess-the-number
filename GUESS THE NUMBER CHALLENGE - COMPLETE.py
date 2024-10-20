#intro 
print ('welcome to the game of *guess the number*')
print ('guess the number using given hint, YOU HAVE 2 LIVES USE IT WISELY'
       'the number lies between 1 and 3')
#input from user
num=int(input('enter your guess: '))
#logic
if  num==2:
    print ('congratulations you have guessed the number :)')
else:
    print ('sorry you have guessed the wrong number, YOU HAVE *ONE* LIFE LEFT'
           ' press 1 to play again')
restart =int(input(':'))
while  restart==1:
    print ('welcome to the game of *guess the number*')
    print ('guess the number using given hint'
           'the number lies between 1 and 3')
    num =  int(input('enter your guess: '))
    if   num==2:
        print ('congratulations you have guessed the number :)')
    else:
        print ('sorry you have guessed the wrong number')
    break

#outro 
print('thank you for playing ')
