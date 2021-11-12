'''
@Author: Pavan Nakate
@Date: 2021-11-12 07:29
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : LongestLength : returns the length of longest string  
'''
def longest_length():
    """
    Description:
        This Function returns the length of longest string
    Parameter:
        None
    Return:
        longest length
    """
    try:
        stringList = ["Pavan", "Rahul", "DD" , "Murlikrishna"]
        longest_word = []

        for string in stringList:
            longest_word.append(len(string))
        
        return max(longest_word)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(longest_length())
