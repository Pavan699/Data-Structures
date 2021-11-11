'''
@Author: Pavan Nakate
@Date: 2021-11-11 10:29
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : AddElementInSet : Add new item(member)
'''
def create_set():
    """
    Description:
        This Function add new item(member) using add() function
    Parameter:
        None
    Return:
        None
    """
    try:
        # Name set
        str_set = {'Pavan','DD','KD','Rushi'}
        print("Before adding : ",str_set)
        str_set.add('Keshav') # add element at any position
        print("After adding : ",str_set)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_set()