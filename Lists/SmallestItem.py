'''
@Author: Pavan Nakate
@Date: 2021-11-11 05:41
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SmallestItem : Print the smallest of all elements in the list  
'''
def smallest_item():
    """
    Description:
        This Function print the smallest of all elements in the list using min() function
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [12,10,3,46,95]
        print("Number List : ",numbers)
        print("Sum of all items in list : ",min(numbers))
        
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    smallest_item()