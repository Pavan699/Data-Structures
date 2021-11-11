'''
@Author: Pavan Nakate
@Date: 2021-11-11 08:49
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CommonItem : print item if it is present in both the lists 
'''
def common_item():
    """
    Description:
        This Function print item if it is present in both the lists
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers1 = [1,2,3,4,5,9,7]
        numbers2 = [6,7,8,9,0,4,1]
        print("list 1 : ",numbers1)
        print("list 2 : ",numbers2)
        print("Common items are : ",end=" ")
        for i in numbers1:
            for j in numbers2:
                if i == j:
                    print(i,end=" ")
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    common_item()