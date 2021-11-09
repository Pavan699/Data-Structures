'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:12
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ConcatenateList : print as string of elements in list
'''
def concatenate_list():
    """
    Description:
        This Function print the string of elements in a list
    Parameter:
        None
    Return:
        None
    """
    try:
        #list
        list_num = [1,5,8,3,6,2,9,4]
        str_output = ''
        for i in list_num:
            str_output += str(i)
        return str_output
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(concatenate_list())