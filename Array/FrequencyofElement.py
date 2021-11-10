'''
@Author: Pavan Nakate
@Date: 2021-11-10 10:27
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : FrequencyofElement : print the frequency of the elements  
'''
from array import * 
def count_element():
    """
    Description:
        This Function print the frequency of the elements from array
    Parameter:
        None
    Return:
        None
    """
    try:
        #Array 
        arr_nums = array('i',[3,9,5,2,6,1,3,4,5,1,6,9]) 
        num_count = 0
        number = int(input("Enter the Number to check frequency : "))
        for i in arr_nums:
            if i == number:
                num_count += 1
        print(f"Frequency of the element {number} is : ",num_count)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    count_element()