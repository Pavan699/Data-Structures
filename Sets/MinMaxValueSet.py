'''
@Author: Pavan Nakate
@Date: 2021-11-11 12:52
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : MinMaxValueSet : Print the minimum and maximum values from set 
'''
def min_max():
    """
    Description:
        This Function print the minimum and maximum values from set
    Parameter:
        None
    Return:
        None
    """
    try:
        #num Set
        num_set = set([11,2,30,4,59])
        print("Minimum Value : ",min(num_set))
        print("Maximum Value : ",max(num_set))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    min_max()