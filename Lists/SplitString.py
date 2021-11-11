'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:51
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SplitString : split string into list and print it  
'''
def split_str():
    """
    Description:
        This Function split string into list and print it
    Parameter:
        None
    Return:
        None
    """
    try:
        name = "RX-100"
        char_list = list(name)

        print("Converted list : ",char_list)
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    split_str()