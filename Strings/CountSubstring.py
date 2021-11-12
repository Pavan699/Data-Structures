'''
@Author: Pavan Nakate
@Date: 2021-11-12 08:34
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CountSubstring  
'''
def count_substring():
    """
    Description:
        This Function prints count of substring from the given string
    Parameter:
        None
    Return:
        None
    """
    try:
        string = "String is an immutable sequence data type"
        print("String : ",string)
        sub_str = input("Enter substring to check : ")
        print(f"The count of '{sub_str}' in string is : {string.count(sub_str)}")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    count_substring()
