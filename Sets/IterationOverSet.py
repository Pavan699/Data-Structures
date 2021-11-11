'''
@Author: Pavan Nakate
@Date: 2021-11-11 10:15
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : IterationOverSet : Print set using Iteration
'''
def create_set():
    """
    Description:
        This Function print set using Iteration 
    Parameter:
        None
    Return:
        None
    """
    try:
        # Name set
        str_set = {'Pavan','DD','KD','Rushi'}
        for name in str_set:
            print(name) # it will print randomly not in perticuler index format
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_set()