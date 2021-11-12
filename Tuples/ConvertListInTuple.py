'''
@Author: Pavan Nakate
@Date: 2021-11-12 11:43
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ConvertListInTuple  
'''
def convert_list():
    """
    Description:
        This Function convert list into tuple and print it
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number list 
        num_list = [1,2,3,4,5]
        print("List : ",num_list)

        num_tuple = tuple(num_list)
        print("Tuple : ",num_tuple)
        print(type(num_tuple))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    convert_list()
