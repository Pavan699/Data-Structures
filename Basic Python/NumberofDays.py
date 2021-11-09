'''
@Author: Pavan Nakate
@Date: 2021-11-09 09:37
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : NumberOfDays : print the number of days in between two days
'''
from datetime import date
def num_of_days():
    """
    Description:
        This Function print number of days in between two days
    Parameter:
        None
    Return:
        None
    """
    try:
        first_date = date(2014,7,2)
        second_date = date(2014,7,11)

        days_remain = second_date - first_date
        print("Days are ",days_remain.days)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    num_of_days()