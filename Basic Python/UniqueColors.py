'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:28
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : UniqueColor : print the unique colors
'''
def color_print():
    """
    Description:
        This Function prints the unique colors
    Parameter:
        None
    Return:
        None
    """
    try:
        color_list_one = {"Red","White","Black"}
        color_list_two = {"Red","Green","Yellow"}
        print(color_list_one.difference(color_list_two))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    color_print()