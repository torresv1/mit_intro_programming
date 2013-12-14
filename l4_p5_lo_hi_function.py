# Name:       Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x
#             is greater than hi; and x otherwise. For this problem, you can assume that lo < hi.
# Purpose:    Learn to use functions
# Date:       12/14/2013 12:18 PM
# Author:     Vladimir Torres-Rivas

def clip( lo, x, hi ):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return min( max( x, lo ), hi )


