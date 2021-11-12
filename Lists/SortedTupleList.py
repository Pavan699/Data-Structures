
'''
@Author: Pavan Nakate
@Date: 2021-11-11 06:05
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SortedTupleList : Print the list in sorted manner with respect to 2nd tuple element  
'''
def tuple_sort():
    """
    Description:
        This Function print the list in sorted manner with respect to 2nd tuple element
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of tuples
        sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        print("Tuples List : ",sample_list)
        def last(n):
            """
            Description:
                This Function returns last key of the tuple 
            Parameter:
                n as the tuple
            Return:
                returns the last item(-1)
            """
            return n[-1]
        print("Sorted list : ",sorted(sample_list,key=last))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    tuple_sort()