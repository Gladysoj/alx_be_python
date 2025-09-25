from datetime import datetime, date, timedelta

def display_current_datetime():
    """
    Save the current date/time in `current_date` and print in 
    YYYY-MM-DD HH:MM:SS: format.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

    def calculate_future_date(days_to_add):
        """
        Save today's date in `today`, compute `future_date` by adding
        days_to_add, and print the future date in YYYY-MM-DD format.

        """
        today = date.today()
        future_date = today + timedelta(days=days_to_add)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))

        def main():
            print("Date and Time Explorer")
            display_current_datetime()
            days = int(input("Enter number of days to add to the current date: "))
            calculate_future_date(days)

            if __name__ == "__main__":
                main()