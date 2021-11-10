'''
@Author: Pavan Nakate
@Date: 2021-11-10 09:36
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DictTable : Print the dictionary in table format 
'''
def print_table():
    """
    Description:
        This Function Print the dictionary in table format 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
        for row in zip(*([key] + (value) for key, value in sorted(dict_num.items()))):
            print(*row)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_table()