'''
@Author: Pavan Nakate
@Date: 2021-11-12 08:08
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : GetLastPart  
'''
def length_of_string():
    """
    Description:
        This Function prints last part of a specified charater
        charater is a user input
    Parameter:
        None
    Return:
        None
    """
    try:
        string = "Welcome to data-structures in python"
        print("Original string : ",string)
        char = input("Enter a charater : ")
        if char in string:
            last = string.index(char)
            print("Last part form entered char : ",string[last:])
        else:
            print("Charater is not in the string")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    length_of_string()
