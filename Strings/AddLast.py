'''
@Author: Pavan Nakate
@Date: 2021-11-12 06:33
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : AddLast : Add ing at the end of the string having size 3   
'''
def add_ing_ly(str):
    """
    Description:
        This function is to add 'ing' to string, if ing present then add 'ly'.
    Parameter:
        str: String to which ing or ly to be added.
    Returns:
        changed string.
    """
    try:
        if len(str) > 2:
            if str[-3:] == 'ing':
                str += 'ly'
            else:
                str += 'ing'
            return str
        else:
            print(f"Length of string '{str}' is too small  : " ,end=" ")
            return len(str)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(add_ing_ly('abc'))
    print(add_ing_ly('abcing'))
    print(add_ing_ly('ab'))
