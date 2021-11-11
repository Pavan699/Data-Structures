'''
@Author: Pavan Nakate
@Date: 2021-11-11 08:26
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : DifferenceBtn2Lists : print the difference members from two lists  
'''
def difference():
    """
    Description:
        This Function print the difference members from two lists
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers1 = [1,2,3,4,5]
        numbers2 = [6,7,8,9,0,4,2]
        print("List 1 : ",numbers1)
        print("List 2 : ",numbers2)
        print("Difference members in list 1 are : ",end=" ")
        for i in numbers1:
            if not(i in numbers2):
                print(i,end=" ")
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    difference()