'''
@Author: Pavan Nakate
@Date: 2021-11-09 08:42
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ListAllFiles : Print all the files in directory
'''
import os
def print_all_files():
    """
    Description:
        This function Print all the files in directory
    Parameter:
        None
    Return:
        None
    """
    try:
        print("List of file in current directory : ")
        for i in os.listdir():
            print(i)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_all_files()