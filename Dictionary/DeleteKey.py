'''
@Author: Pavan Nakate
@Date: 2021-11-10 06:49
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DeleteKey : Delete a key to the dictionary 
'''
def delete_key():
    """
    Description:
        This Function delete the key from the dictionary 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {0:10,1:20,3:30,4:40,5:50}
        print("Original dict : ",dict_num)
        
        #Using pop method to delete key as 1
        del_key = dict_num.pop(1)

        print("After deleting : ",dict_num)
        print("Poped Key is : ",del_key)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    delete_key()