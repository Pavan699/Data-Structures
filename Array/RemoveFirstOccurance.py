'''
@Author: Pavan Nakate
@Date: 2021-11-10 12:10
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemoveFirstOccurance : remove the first occurance of the entered element 
'''
from array import * 
def remove_element():
    """
    Description:
        This Function remove the first occurance of the entered element
    Parameter:
        None
    Return:
        None
    """
    try:
        #Array
        arr_nums = array('i',[3,9,5,2,6,1,3,4,5,1,6,9])
        print("Original Array : ",arr_nums)
        element = int(input("Enter the element : "))
        flag = False
        for i in arr_nums:
            if i == element:
                arr_nums.remove(i)
                flag = True
                break
        if flag == False:
            print("Element is Not in the array.")
        else:
            print(f"First Occurance of {element} is removed.")
            print("After Removing : ",arr_nums)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    remove_element()