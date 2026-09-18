from datetime import datetime
def main():
    day = datetime.now().weekday()
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[day])
    if day <= 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its a Friday")
        print("Just a day left until the weekend")
    else:
        print("Its the weekend!")
    months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = datetime.now().month
    print("It is", months[month-1])
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    month = int(input())
    if month <= 2 or month == 12:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3
    print("It is", seasons[season])
if __name__=="__main__":
    main()
