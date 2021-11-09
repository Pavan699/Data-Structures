'''
@Author: Pavan Nakate
@Date: 2021-11-09 09:45
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CheckElement : Check the element in the list print True if present or else folse
'''
def check():
    """
    Description:
        This Function check the element in the list print True if present or else folse
    Parameter:
        None
    Return:
        None
    """
    try:
        #list
        list_one = [1,5,8,3]
        #checking the 3 is present or not in list
        print(3 in list_one)
        #checking the -1 is present or not in list
        print(-1 in list_one)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check()