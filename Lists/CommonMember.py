'''
@Author: Pavan Nakate
@Date: 2021-11-11 08:49
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CommonMember : return True if both list having one common member 
'''
def common_member():
    """
    Description:
        This Function return True if both list having one common member
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers1 = [1,2,3,4,5]
        numbers2 = [6,7,8,9,0,4]
        print("list 1 : ",numbers1)
        print("list 2 : ",numbers2)
        
        for i in numbers1:
            for j in numbers2:
                if i == j:
                    print("Member",i,"is common")
                    return True
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(common_member())