'''
@Author: Pavan Nakate
@Date: 2021-11-10 10:14
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CreateArray : Create an array and print it 
'''
from array import * 
def create_array():
    """
    Description:
        This Function create an array of five elements and print it by using index
    Parameter:
        None
    Return:
        None
    """
    try:
        #Array with five numbers
        arr_nums = array('i',[3,9,5,2,6]) # 'i' is for the integers-type
        print("Integer Array : ",arr_nums)
        
        print("Accessing elements by using index : ")
        print(arr_nums[0])
        print(arr_nums[1])
        print(arr_nums[2])
        print(arr_nums[3])
        print(arr_nums[4])
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_array()