'''
@Author: Pavan Nakate
@Date: 2021-11-10 06:23
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Iteratedictionary : printing Dictionary by using loop 
'''
def loop_dict():
    """
    Description:
        This Function to print dictionary by using loop 
    Parameter:
        None
    Return:
        None
    """
    try:
        dict_name = {1:'DD',2:'Pavan',3:'Kedar',4:'Rajesh',5:'Smaiksha',6:'Rakhi'} 
        print("Without Using items() function : ")   
        for d in dict_name:
           print("Key : ",d," => Value : ",dict_name[d])

        print("Using items() function : ")  
        for k,v in dict_name.items():
            print("Key : ",k," => Value : ",v)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    loop_dict()