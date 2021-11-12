'''
@Author: Pavan Nakate
@Date: 2021-11-12 11:02
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RepeatedItems  
'''
def repeated_items():
    """
    Description:
        This Function print the repeated items 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,4,5,1,0,7,5,7,4,9,8)
        print("Tuple : ",num_tuple)
        #using count method to check the no. of occurence
        print("Repeated Items are : ",end=" ")
        for num in num_tuple:
            if num_tuple.count(num) >= 2:
                print(num,end=" ")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    repeated_items()
