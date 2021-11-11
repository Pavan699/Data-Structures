'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:17
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : PermutationsOfList : print all permutations of the list  
'''
from itertools import permutations
def permute(lst,front=0):
    """
    Description:
        This Function print all permutations of the list
    Parameter:
        None
    Return:
        None
    """
    try:
        permute_list = list(permutations(lst))
        print(permute_list)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    permute([1,2,3])