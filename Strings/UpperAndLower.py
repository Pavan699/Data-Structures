'''
@Author: Pavan Nakate
@Date: 2021-11-12 07:29
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : UpperAndLower : print the string in Upper and Lower case  
'''
def upper_lower():
    """
    Description:
        This Function print the string in Upper and Lower case 
        of the user input
    Parameter:
        None
    Return:
        None
    """
    try:
        user_input = input("Enter the string : ")
        print("Original input : ",user_input)
        print("Upper case : ",user_input.upper())
        print("Lower case : ",user_input.lower())

    except Exception as e:
        print(e)

if __name__ == "__main__":
    upper_lower()
