# -*- coding: utf-8 -*-
# guess a number between 1 and 100 in ten tries

import random
YES = ['Y','YES']
answer = 'yes'
while False in YES:
    NumToGuess = random.randint(1, 100)
    NumOfTry = 10

    print ("Try to guess a number between 1 and 100 in 10 tries.")

    while NumOfTry != 0:
        try:
            x = int(raw_input ("Please enter a number between 1 and 100:"))
            if x > NumToGuess:
                print (x,"is higher than the number.")
                NumOfTry=NumOfTry-1
                print (NumOfTry, "attempt(s) left")
                print ("")
            elif x < NumToGuess:
                print (x,"is lower than the number.")
                NumOfTry=NumOfTry-1
                print (NumOfTry, "attempt(s) left")
                print ("")
            elif x == NumToGuess:
                print ("You Win, Congratulations!!!")
                NumOfTry=0
        except:
            print ("Please enter a valid number. For example 1, 5 an 44 are valid numbers to input.")
    else:
        print ("The number to guess was: ", NumToGuess)
        answer = raw_input ('Do you want to play again? (yes/no) :')
else:
    print ("Thank you for playing. Goodbye")