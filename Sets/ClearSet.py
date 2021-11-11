'''
@Author: Pavan Nakate
@Date: 2021-11-11 12:44
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ClearSet : delete set 
'''
def clear_set():
    """
    Description:
        This Function clear(delete) set 
    Parameter:
        None
    Return:
        None
    """
    try:
        #num Set
        num_set = set([1,2,3,4,5])
        print("Original set : ",num_set)
        num_set.clear()
        print("Clear set : ",num_set)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    clear_set()