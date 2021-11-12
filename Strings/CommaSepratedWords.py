'''
@Author: Pavan Nakate
@Date: 2021-11-12 07:41
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CommaSeprartedWords : print the words in sorted form and they should be unique  
'''
def sorted_unique():
    """
    Description:
        This Function print the words in sorted form
        and the words are unique
    Parameter:
        None
    Return:
        None
    """
    try:
        list_words = 'red,white,black,red,green,black'
        words = [word for word in list_words.split(",")]
        sort_list = sorted(list(set(words)))
        for w in sort_list:
            print(w,end=" ")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    sorted_unique()
