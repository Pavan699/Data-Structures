'''
@Author: Pavan Nakate
@Date: 2021-11-12 10:34
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : UnpackTuple : print the values in tuple separate  
'''
def unpack_tuple():
    """
    Description:
        This Function print the values in tuple separate 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5)
        #take equle no. of variables to store
        n1,n2,n3,n4,n5=num_tuple
        print("Variables in tuples are : ",n1,n2,n3,n4,n5)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    unpack_tuple()
