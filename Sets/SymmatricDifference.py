'''
@Author: Pavan Nakate
@Date: 2021-11-11 12:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SymmetricDifference  
'''
def symmetric_difference():
    """
    Description:
        This Function prints the element from both the sets which are not unique
    Parameter:
        None
    Return:
        None
    """
    try:
        num_set1 = {1,2,3,4,5}
        num_set2 = {1,6,3,0,5,9}
        
        print(" Symmentric Difference is : ",num_set1.symmetric_difference(num_set2))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    symmetric_difference()