'''
@Author: Pavan Nakate
@Date: 2021-11-12 06:03
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : FrequencyOfCharacters : prints the number of count of each character  
'''
def frequency_of_char():
    """
    Description:
        This Function prints the number of count of each character
        count() function is used
    Parameter:
        None
    Return:
        None
    """
    try:
        name = "Pavan"
        char_frequency = {}
        print("Frequency of the charaters is : ",end= " ")
        for char in name:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        print(char_frequency)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    frequency_of_char()
