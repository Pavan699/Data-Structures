'''
@Author: Pavan Nakate
@Date: 2021-11-09 11:00
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-09 11:00
@Title : ColorList : Print the last and first color from the list
'''
def color_print():
    """
    Description:
        This Function converts the str(comma-seprate nums) into list and tuples
    Parameter:
        None
    Return:
        None
    """
    try:
        color_list = ["Red","Green","White","Black"]
        print("First Color is : ",color_list[0])
        print("Last Color is : ",color_list[-1])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    color_print()