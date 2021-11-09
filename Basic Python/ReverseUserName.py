'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:03
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ReverseUserName : print the user name in thr reverse
'''
def reverse_name():
    """
    Description:
        This Function takes the user names and Print it in reverse order
    Parameter:
        None
    Return:
        None
    """ 
    try:
        #user inputs
        first_name = input("Enter the First name : ")
        last_name = input("Enter the Last name : ")

        print("Full Name is : ",first_name,last_name)
        print("Reverse Name is : ",last_name[-1::-1],first_name[-1::-1])#(start-index:end-index:gap(ignore))
        
    except Exception as e:
        print("Exception is : ",e)

if __name__ == "__main__":
    reverse_name()
