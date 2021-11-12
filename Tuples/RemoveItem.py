'''
@Author: Pavan Nakate
@Date: 2021-11-12 12:02
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemoveItem  
'''
def remove_tuple_item():
    """
    Description:
        This Function remove item form the tuple and print it
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5)
        print("Tuple : ",num_tuple)
        # As we know tuples are immutable
        # So convert it into list and remove the item and then convert the list into tuple
        list_num = list(num_tuple)
        list_num.remove(3)
        print("After removing 3 : ",tuple(list_num)) 
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    remove_tuple_item()
