'''
@Author: Pavan Nakate
@Date: 2021-11-11 04:44
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : FrozenSet  
'''
def frozen_set():
    """
    Description:
        This Function print and use of frozen set 
    Parameter:
        None
    Return:
        None
    """
    try:
        #num Set
        num_set = frozenset([1,2,3,4,5])
        print("Frozen set : ",num_set)
        print("Forzen sets are immutable.")
        print("You can store set inside set by using frozen set")
        frozen = frozenset({1,2,frozenset({3,4}),5})
        print("E.g. : ",frozen)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    frozen_set()