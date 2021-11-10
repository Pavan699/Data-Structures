'''
@Author: Pavan Nakate
@Date: 2021-11-10 05:10
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : AscendDescend : Print the values in ascending nad descending form 
'''
import operator
def ascend_descend():
    """
    Description:
        This Function Prints the values in ascending and descending form 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_num = {0:10,9:20,5:73,6:34,8:11}
        print("Original Dictionary : ",dict_num)
        #Ascending Order
        ascend_ord = dict(sorted(dict_num.items(), key=operator.itemgetter(1)))
        print("Ascending Order : ",ascend_ord)
        #Descending Order
        descend_ord = dict(sorted(dict_num.items(), key=operator.itemgetter(1), reverse=True))
        print("Descending Order : ",descend_ord)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    ascend_descend()