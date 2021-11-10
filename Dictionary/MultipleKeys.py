'''
@Author: Pavan Nakate
@Date: 2021-11-10 10:04
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : MultipleKeys : check multiple keys exists 
'''
def keys_exists():
    """
    Description:
        This Function check multiple keys exists 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
        print("Checking All Keys : ",dict_num.keys() == {'A','B','C'})
        print("Checking multiple Keys : ",dict_num.keys() >= {'A','B','C','D','E'})

    except Exception as e:
        print(e)

if __name__ == "__main__":
    keys_exists()