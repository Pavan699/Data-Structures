'''
@Author: Pavan Nakate
@Date: 2021-11-11 10:29
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemoveItem : Remove one item from set
'''
def create_set():
    """
    Description:
        This Function remove one item from set by using remove() function
    Parameter:
        None
    Return:
        None
    """
    try:
        # Name set
        str_set = {'Pavan','DD','KD','Rushi'}
        print("Before removing : ",str_set)
        str_set.remove('KD') # add element at any position
        print("After removing : ",str_set)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_set()