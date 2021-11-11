'''
@Author: Pavan Nakate
@Date: 2021-11-11 05:57
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SamLetterCount : Print the count of string having first and last letter should be same  
'''
def count_string():
    """
    Description:
        This Function print the count of string having first and last letter should be same
        list of strings  
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        string_list = ['abc','xyz','aba','1221','kanak']
        print("String List : ",string_list)
        count = 0
        for strg in string_list:
            if strg[0] == strg[-1]:
                count += 1
        print("Count of string having same first and last letter is : ",count)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    count_string()