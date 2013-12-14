# Name:       Evaluate is a character is a vowel not using the "in" function.
# Purpose:    Learn to use functions
# Date:       12/14/2013 1:35 PM
# Author:     Vladimir Torres-Rivas


def isVowel2( char ):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char in 'aeiouAEIOU':
        return True
    else:
        return False


# A shorter solution
def isVowel3( char ):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char.lower() in 'aeiou'
