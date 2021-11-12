'''
@Author: Pavan Nakate
@Date: 2021-11-12 06:24
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ReplaceCharInString  
'''
def replace_char():
    """
    Description:
        This Function prints the length of string
    Parameter:
        None
    Return:
        None
    """
    try:
        string = "restart"
        char = string[0] # save the 1st char
        print("Before Replacing : ",string)
        
        new_string = string.replace(char, '$')
        new_string = char + new_string[1:]#printing from the 2nd char
        print("After Replacing : ",new_string)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    replace_char()
