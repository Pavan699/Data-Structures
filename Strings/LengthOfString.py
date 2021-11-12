'''
@Author: Pavan Nakate
@Date: 2021-11-12 06:03
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : LengthOfString  
'''
def length_of_string():
    """
    Description:
        This Function prints the length of string
    Parameter:
        None
    Return:
        None
    """
    try:
        name = "Lord Shiva"
        print("Length of string : ",len(name))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    length_of_string()
