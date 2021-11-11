'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:01
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemovePositions : print a specified list after removing the 0th, 4th and 5th elements.  
'''
def remove_positions():
    """
    Description:
        This Function print a specified list after removing the 0th, 4th and 5th elements.
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of colors
        colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        print("Before : ",colors)
        colors.remove('Red')
        colors.remove('Pink')
        colors.remove('Yellow')
        print("After : ",colors) 

    except Exception as e:
        print(e)

if __name__ == "__main__":
    remove_positions()