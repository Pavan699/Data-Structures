'''
@Author: Pavan Nakate
@Date: 2021-11-11 12:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : IntersectionSets  
'''
def intersection_sets():
    """
    Description:
        This Function prints the common elements from two sets 
    Parameter:
        None
    Return:
        None
    """
    try:
        #You can define set in two types
        num_set1 = {1,2,3,4,5}
        num_set2 = {1,6,3,0,5,9}
        
        print(num_set1.intersection(num_set2))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    intersection_sets()