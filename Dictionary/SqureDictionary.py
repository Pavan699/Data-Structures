'''
@Author: Pavan Nakate
@Date: 2021-11-10 06:39
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SqureDictionary : Print dict where key is number and value is its squre
'''
def squr_dict():
    """
    Description:
        This Function Print dict where key is number and value is its squre.
        Range is user input. 
    Parameter:
        None
    Return:
        None
    """
    try:
        #empty dict to store
        dict_squr = {}
        range_num = int(input("Enter the number : "))

        for i in range(1,range_num+1):
            dict_squr[i] = i*i #adding the key and its squre
        
        print(dict_squr)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    squr_dict()