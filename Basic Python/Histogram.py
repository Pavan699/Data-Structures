'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:04
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Histogram : print the number of stars'*' as the number in list
'''
def histogram(lst):
    """
    Description:
        This Function print number stars'*' as the number in list
    Parameter:
        lst -> list of numbers as input
    Return:
        None
    """
    try:
        for i in lst:
            print( i * '*')
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    list_num = [1,2,3,4,5,6,7]
    histogram(list_num)