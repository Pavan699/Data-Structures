'''
@Author: Pavan Nakate
@Date: 2021-11-09 11:00
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-09 11:00
@Title : Document : print the syntax and info about the function
'''
import math
def print_info():
    """
    Description:
        This Function print the syntax and info about the function
    Parameter:
        None
    Return:
        None
    """
    try:
        #print the info about abs() function
        help(abs)
        #print the info about pow() function
        help(pow)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_info()