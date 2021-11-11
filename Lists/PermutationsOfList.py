'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:17
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : PermutationsOfList : print all permutations of the list  
'''
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
        # base condition
        if front >= len(lst):
            print(lst)
            return
        for i in range(front ,len(lst)):
            lst[front], lst[i] = lst[i] ,lst[front]
            permute(lst,front+1)
            lst[front], lst[i] = lst[i] ,lst[front]
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    permute([1,2,3])