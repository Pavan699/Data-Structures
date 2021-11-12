'''
@Author: Pavan Nakate
@Date: 2021-11-12 01:06
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ReverseTuple  
'''
def reverse_tuple():
    """
    Description:
        This Function print the reversed tuple 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5)
        print("Tuple : ",num_tuple)
        print("Reveresed Tuple : ",num_tuple[-1::-1])
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    reverse_tuple()
