'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:04
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : FileExists : Print True if file is present or else False
'''
import os
def file_exist():
    """
    Description:
        This Function checks that the file is present or not
    Parameter:
        None
    Return:
        None
    """
    try:

        print(os.path.isfile('Demo.txt'))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    file_exist()