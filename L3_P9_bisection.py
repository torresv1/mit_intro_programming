
# Name:       Guessing a number using bisection
# Purpose:    Learn to use bisection method for quick computing
# Date:       11/03/2013 1:23 AM
# Author:     Vladimir Torres-Rivas

#Defining limits

upper_limit = 100
lower_limit = 0
guess_number = (upper_limit + lower_limit)/2  


#Initial guess

print "Please think of a number between 0 and 100!"
print "Is your secret number {}?".format( guess_number )
answer = str( raw_input( "Enter 'h' to indicate the guess is too high. Enter 'l' to\
 indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " ) )

#Check if the user enter the proper inputs


#Start bisection when going higher

while answer != "c":

    if answer == "h":
        lower_limit = guess_number
        guess_number = ( lower_limit + upper_limit ) / 2
        print "Is your secret number {}?".format( guess_number )
        answer = str( raw_input( "Enter 'h' to indicate the guess is too high. Enter 'l' to\
 indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " ) )

    elif answer == "l":
        upper_limit = guess_number
        guess_number = ( lower_limit + upper_limit ) / 2
        print "Is your secret number {}?".format( guess_number )
        answer = str( raw_input( "Enter 'h' to indicate the guess is too high. Enter 'l' to\
 indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " ) )

    if answer != "h" and answer != "l" and answer != "c":
        print 'Sorry, I did not understand your input.'
        answer = str( raw_input( "Enter 'h' to indicate the guess is too high. Enter 'l' to\
 indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " ) )

print "Game over. Your secret number was:" + " " + str( guess_number )



