'''
@Author: Pavan Nakate
@Date: 2021-11-12 10:32
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DifferentDataTypeTuple  
'''
def different_datatype():
    """
    Description:
        This Function create a tuple with different data-type and print it 
    Parameter:
        None
    Return:
        None
    """
    try:
        # different data-type Tuple 
        type_tuple = (1,2.3,'A',"Hello",True)
        print("Tuple with different data-type : ",type_tuple)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    different_datatype()
