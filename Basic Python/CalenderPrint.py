'''
@Author: Pavan Nakate
@Date: 2021-11-09 12:13
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CalenderPrint : print the calender for year and month
'''
import calendar
def print_calender():
    """
    Description:
        This Function print the calender.
        year and month are the inputs
    Parameter:
        None
    Return:
        None
    """
    try:
        year = int(input("Enter the year : "))
        month = int(input("Enter the month : "))
        if year>999 and year<=9999 and month>0 and month<=12:
            my_calender = calendar.month(year,month)
            print(my_calender)
        else:
            print("Invalid data")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_calender()