'''
@Author: Pavan Nakate
@Date: 2021-11-11 08:26
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CopyList : Copy the list into another list and print it  
'''
def copy_list():
    """
    Description:
        This Function copy the list into another list and print it
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [1,2,3,4,5]
        print("Original list : ",numbers)
        list_copy = numbers.copy()
        print("Copied List : ",list_copy)
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    copy_list()