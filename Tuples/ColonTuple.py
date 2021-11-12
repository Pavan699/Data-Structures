'''
@Author: Pavan Nakate
@Date: 2021-11-12 10:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ColonTuple  
'''
from copy import deepcopy
def colon_tuple():
    """
    Description:
        This Function make a deepcopy of the tuple 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Tuple 
        n_tuple = (1,2.3,[],"DD",True)
        print("Tuple : ",n_tuple)

        dc_tuple = deepcopy(n_tuple)
        #Adding items in list
        dc_tuple[2].append(7)
        print("Deepcopy tuple : ",dc_tuple)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    colon_tuple()
