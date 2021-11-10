'''
@Author: Pavan Nakate
@Date: 2021-11-10 10:17
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ListCount : print the count of list in dict
'''
def list_count():
    """
    Description:
        This Function print the count of list in dict
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {'A':[1,2,3],'Z':"Hello",'B':[4,5,6],'C':[7,8,9],'D':"Python"}
        count = 0
        for kv in dict_num:
            if type(dict_num[kv]) == list:
                count += 1
        print("List count is : ",count)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    list_count()