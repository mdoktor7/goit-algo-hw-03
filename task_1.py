from datetime import datetime
date = input("Interested date is: ")
try:
    def get_days_from_today(date):
        date_formated = datetime.strptime(date, "%Y-%m-%d")
        date_now = datetime.today()
        get_days_from_today = date_now.toordinal() - date_formated.toordinal()
        return int(get_days_from_today)
    if get_days_from_today(date) >= 0:
         print(f"{get_days_from_today(date)} days have passed since the date {date}")
    else:
         print(f"{abs(get_days_from_today(date))} days before the date {date}")
except ValueError:
    print(f"Please input date {date} in format Year-Month-Day")