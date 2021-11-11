'''
@Author: Pavan Nakate
@Date: 2021-11-11 05:47
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : MultiplyAll : Print the multiplication of all elements in the list  
'''
def multiply_all():
    """
    Description:
        This Function print the multiplication of all elements in the list
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [1,2,3,4,5]
        print("Number List : ",numbers)
        # set multiplication at 1 BCoz can not multiply by 0
        multipication = 1
        for i in numbers:
            multipication = i * multipication
        print("Multiplication of items in list : ",multipication)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    multiply_all()