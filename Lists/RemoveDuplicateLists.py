'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:14
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : RemoveDuplicateLists : remove the duplicate lists from the given list  
'''
def remove_duplicates():
    """
    Description:
        This Function remove the duplicate lists from the given list
    Parameter:
        None
    Return:
        None
    """
    try:
        #list
        sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("Original list : ",sample_list)
        for l in sample_list:
            if sample_list.count(l) == 2:
                sample_list.remove(l)       

        print("List : ",sample_list)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    remove_duplicates()