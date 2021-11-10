'''
@Author: Pavan Nakate
@Date: 2021-11-10 04:56
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : AddKeyValue : Add a key to the dictionary 
'''
def add_key_value():
    """
    Description:
        This Function add the new key to the dictionary 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {0:10,1:20}
        print("Before adding : ",dict_num)
        #adding key and its value
        dict_num[3] = 30
        print("After adding : ",dict_num)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    add_key_value()