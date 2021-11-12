'''
@Author: Pavan Nakate
@Date: 2021-11-12 12:21
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SliceTuple  
'''
def slice_tuple():
    """
    Description:
        This Function slice the tuple ans print it 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5,11,22,33,44,55,111,222,333,444,555)
        # slicing starts from 5 to end
        print(num_tuple[5:])
        # slicing starts from 0 and ends at 10th index
        print(num_tuple[:10]) 
        # slicing from 1 to 4
        print(num_tuple[5:10])  
        # slicing from start to end using step sizes of 3
        print(num_tuple[::3]) 
        # Slicing from end to start(reverese the tuple)
        print(num_tuple[-1::-1]) 
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    slice_tuple()
