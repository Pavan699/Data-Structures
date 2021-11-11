'''
@Author: Pavan Nakate
@Date: 2021-11-11 05:41
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SumOfAll : Print the sum of all elements in the list  
'''
def sum_of_all():
    """
    Description:
        This Function print the sum of all elements in the list using sum() function
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [1,2,3,4,5]
        print("Number List : ",numbers)
        print("Sum of all items in list : ",sum(numbers))
        
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    sum_of_all()