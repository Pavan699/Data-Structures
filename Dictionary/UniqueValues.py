# Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''
@Author: Pavan Nakate
@Date: 2021-11-10 06:23
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : UniqueValue : printing unique values from dictionary 
'''
def unique_values():
    """
    Description:
        This Function to print unique values 
    Parameter:
        None
    Return:
        None
    """
    try:
        sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print(sample_data) 
        # YouTube method
        unique_val = set(val for dic in sample_data for val in dic.values())  
        print("Unique Values : ",unique_val)
        # logic 
        u_val = [] # list
        for dict_kv in sample_data:
            for k in dict_kv:
                u_val.append(dict_kv[k])
        print("Unique Values : ",set(u_val)) #coverting into a set 
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    unique_values()