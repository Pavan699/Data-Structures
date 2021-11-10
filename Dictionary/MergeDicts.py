'''
@Author: Pavan Nakate
@Date: 2021-11-10 05:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : MergeDicts : adding all three dicts in one dict 
'''
def merge_dicts():
    """
    Description:
        This Function add all dictionaries in one 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict1 = {1:10,2:20}
        print(dict1)
        dict2 = {3:30,4:40}
        print(dict2)
        dict3 = {5:50,6:60}
        print(dict3)
        one_dict = {}

        for d in (dict1,dict2,dict3):
            one_dict.update(d)
        print("Merged Dictionary : ",one_dict)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    merge_dicts()