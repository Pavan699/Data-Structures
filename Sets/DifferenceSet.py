'''
@Author: Pavan Nakate
@Date: 2021-11-11 12:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DifferenceSet  
'''
def union_sets():
    """
    Description:
        This Function prints the element from set1 which are not in set2
    Parameter:
        None
    Return:
        None
    """
    try:
        #You can define set in two types
        num_set1 = {1,2,3,4,5}
        num_set2 = {1,6,3,0,5,9}
        
        print("Difference Set : ",num_set1 - num_set2)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    union_sets()