from datetime import datetime


def get_days_from_today(date=input("Print date in format: YYYY-MM-DD \n")):
    now = datetime.now()
    date_to_timedate = datetime.strptime(date, "%Y-%m-%d")
    if date_to_timedate:
        result = now - date_to_timedate
        return print(result.days)
    else:
        print("Please check your date, it should be in format: YYYY-MM-DD")

get_days_from_today()

# get_days_from_today("2012-04-30")
