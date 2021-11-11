'''
@Author: Pavan Nakate
@Date: 2021-11-11 06:24
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DuplicateItems : remove duplicate items and then print the list  
'''
def remove_duplicates():
    """
    Description:
        This Function remove duplicate items and then print the list
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [1,2,3,4,5,2,4,5,7,1,2,8,0]
        print("Number List : ",numbers)
        print("Without Duplicates : ",list(set(numbers)))       
    except Exception as e:
        print(e)

if __name__ == "__main__":
    remove_duplicates()