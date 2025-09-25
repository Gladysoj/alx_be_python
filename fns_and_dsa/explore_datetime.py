import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

    def calculate_future_date(days_to_add):
        today = datetime.date.today()
        future_date = today + datetime.timedelta(days_to_add)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))

        def main():
            print("Date and Time Explorer")
            display_current_datetime()
            days = int(input("Enter number of days to add: "))
            calculate_future_date(days)

            if __name__ == "__main__":
                main()