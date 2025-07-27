from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    f_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f_current_date)

def calculate_future_date(num_of_days):
    future_date = current_date + timedelta(days=num_of_days)
    f_future_date = future_date.strftime("%Y-%m-%d")
    print(f_future_date)

display_current_datetime()

num_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(num_of_days)
