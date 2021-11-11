'''
@Author: Pavan Nakate
@Date: 2021-11-11 09:33
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : AppendLists : append one list into another  
'''
def append_list():
    """
    Description:
        This Function append one list into another
    Parameter:
        None
    Return:
        None
    """
    try:
        #list of numbers
        numbers = [1,2,3,4,5]
        print("Numbers : ",numbers)
        #list of color
        colors = ['Red', 'Green', 'White', 'Black']
        print("Colors : ",colors)
        #Appending one list into another
        combo = numbers + colors
        print("Final List : ",combo)
        
               
    except Exception as e:
        print(e)

if __name__ == "__main__":
    append_list()