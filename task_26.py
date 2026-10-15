from datetime import datetime, timedelta

def get_date(msg):
    while True:
        try:
            return datetime.strptime(input(msg), "%d-%m-%Y")
        except ValueError:
            print("Invalid date! Use DD-MM-YYYY.")

while True:
    print("\nDate and Time Utility")
    print("1. Calculate Age")
    print("2. Days Between Dates")
    print("3. Working Days Between Dates")
    print("4. Format Current Date and Time")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        dob = get_date("Enter DOB (DD-MM-YYYY): ")
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        print("Age:", age, "years")

    elif ch == "2":
        d1 = get_date("Enter first date: ")
        d2 = get_date("Enter second date: ")
        print("Days:", abs((d2 - d1).days))

    elif ch == "3":
        start = get_date("Enter start date: ")
        end = get_date("Enter end date: ")
        if start > end:
            start, end = end, start

        count = 0
        while start <= end:
            if start.weekday() < 5:
                count += 1
            start += timedelta(days=1)
        print("Working Days:", count)

    elif ch == "4":
        now = datetime.now()
        print("Date:", now.strftime("%d-%m-%Y"))
        print("Time:", now.strftime("%H:%M:%S"))
        print("Day :", now.strftime("%A"))

    elif ch == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
