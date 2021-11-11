'''
@Author: Pavan Nakate
@Date: 2021-11-11 10:47
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemovePresentItem : Remove the item if it is present
'''
def create_set():
    """
    Description:
        This Function remove the item if it is present
    Parameter:
        None
    Return:
        None
    """
    try:
        # Name set
        str_set = {'Pavan','DD','KD','Rushi'}
        print("Original Set : ",str_set)
        name_input = input("Enter name to remove : ")
        if name_input in str_set: #checkong name is present or not
            str_set.remove(name_input)
            print("Element is removed from set : ",str_set) 
        else:
            print("Element is not present in list")
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_set()