'''
@Author: Pavan Nakate
@Date: 2021-11-10 06:49
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CountOfTrue : Print the count of True in the given dictionary 
'''
def true_count():
    """
    Description:
        This Function print the count of True in the given dictionary 
    Parameter:
        None
    Return:
        None
    """
    try:
        sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        count = 0
        for d in sample_data:
            if d['success'] == True:
                count += 1

        print("Count of value 'True' is : ",count)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    true_count()