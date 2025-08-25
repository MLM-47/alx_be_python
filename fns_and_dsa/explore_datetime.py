from datetime import datetime, timedelta
def display_current_datetime ():
    current_date = datetime.now()
    formated = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formated

def calculate_future_date ():
    current_date = datetime.now()
    number_of_days = input(f"Current date and time: {display_current_datetime()}.\n Enter the number of days to add to the current date: ")
    days = timedelta(days=int(number_of_days))
    future_date = current_date+days
    formated = future_date.strftime("%Y-%m-%d")
    print(formated)

calculate_future_date()