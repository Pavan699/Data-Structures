'''
@Author: Pavan Nakate
@Date: 2021-11-09 10:03
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-09 10:03
@Title : ConvertListTuple : convert the string into list and tuples
'''
def convert_str():
    """
    Description:
        This Function converts the str(comma-seprate nums) into list and tuples
    Parameter:
        None
    Return:
        None
    """ 
    try:
        # Comma-Seprate numbers in the form of string
        data = "3,7,5,9,23,14,24"
        print("Original data : ",data)
        #using slpit to convert into list
        list_data = data.split(',')
        print("List Format : ",list_data)
        print("Type of list_data : ",type(list_data))
        #using tuple function to convert into tuple
        tuple_data = tuple(data.split(','))
        print("Tuple Format :",tuple_data)
        print("Type of tuple_data : ",type(tuple_data))

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    convert_str()