'''
@Author: Pavan Nakate
@Date: 2021-11-11 10:02
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CreateSet : Create a set 
'''
def create_set():
    """
    Description:
        This Function create a set 
    Parameter:
        None
    Return:
        None
    """
    try:
        #You can define set in two types
        num_set = set([1,2,3,4,5])
        #{} repesents the set
        str_set = {'Pavan','DD','KD','Rushi'}
        print("Number set : ",num_set) 
        print("String set : ",str_set)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_set()