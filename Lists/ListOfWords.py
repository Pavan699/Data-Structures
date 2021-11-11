'''
@Author: Pavan Nakate
@Date: 2021-11-11 08:34
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ListOfWords : find list of words having length greter than n(user input) from the list  
'''
def find_name():
    """
    Description:
        This Function find the word having length greter then n
        where n is user input
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of names
        names_list = ['abcde','xyz','DD','samiksha','kanak']
        print("Original list : ",names_list)
        length = int(input("Enter the length of word : "))
        count_list = []
        for name in names_list:
            if len(name) > length:
               count_list.append(name)
        
        print(f"List of names having length greter than {length} is : ",count_list)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    find_name()