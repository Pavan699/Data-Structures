'''
@Author: Pavan Nakate
@Date: 2021-11-12 11:29
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ItemExists  
'''
def item_exists_tuple():
    """
    Description:
        This Function print True if item exists or else false 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Number Tuple 
        num_tuple = (1,2,3,8,9,0)
        print("Tuple : ",num_tuple)
        num = int(input("Enter Number to check : "))
        if num in num_tuple:
            print(f"Number {num} exists :",True)
        else:
            print(f"Number {num} not exists :",False)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    item_exists_tuple()
