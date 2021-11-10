'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:05
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ReverseArray : Print the reverse array 
'''
from array import * 
def reverse_array():
    """
    Description:
        This Function print the reverse array of the present array
    Parameter:
        None
    Return:
        None
    """
    try:
        #Array with numbers
        nums = array('i',[1,7,3,9,5,2,6])
        print("Original array is : ",nums)
        nums.reverse()#reverse method to reverse
        print("Reverse array is : ",nums)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    reverse_array()