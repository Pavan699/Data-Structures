'''
@Author: Pavan Nakate
@Date: 2021-11-12 08:31
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : LowerCaseString  
'''
def lower_case():
    """
    Description:
        This Function prints the string in lower case from n
        where n is user input 
    Parameter:
        None
    Return:
        None
    """
    try:
        string = "RESTART THE MACHINE"
        print("Original String : ",string)
        n = int(input("Enter a range to lowercase: "))
        print("Lower case :", string[:n].lower()+ string[n:])
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    lower_case()
