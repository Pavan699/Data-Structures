'''
@Author: Pavan Nakate
@Date: 2021-11-10 09:23
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : StringToDict : print the letter as key and its frequency as value 
'''
def str_dict():
    """
    Description:
        This Function prints the letter as key and its frequency as value 
        By getting user input(word)
    Parameter:
        None
    Return:
        None
    """
    try:
        word = input("Enter a word : ")
        strdict = {}
        
        for x in word:
            keys = strdict.keys()
            #condition 
            if x in keys:
                strdict[x] += 1
            else:
                strdict[x] = 1

        print("Dictionary : ",strdict)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    str_dict()