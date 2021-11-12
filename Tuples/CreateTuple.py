'''
@Author: Pavan Nakate
@Date: 2021-11-12 10:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CreateTuple  
'''
def create_tuple():
    """
    Description:
        This Function create a tuple and print it 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5)
        print("Tuple : ",num_tuple)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_tuple()
