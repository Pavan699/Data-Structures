'''
@Author: Pavan Nakate
@Date: 2021-11-12 08:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ReverseString  
'''
def reverse_str():
    """
    Description:
        This Function prints reverse string
    Parameter:
        None
    Return:
        None
    """
    try:
        name = "India"
        print("Original str : ",name)
        print("Reverse str : ",name[-1::-1])
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    reverse_str()
