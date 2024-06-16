from datetime import datetime


def get_days_from_today(date=input("Print date in format: YYYY-MM-DD \n")):
    now = datetime.now()
    date_to_timedate = datetime.strptime(date, "%Y-%m-%d")
    result = now - date_to_timedate

    print(result.days)
    return result.days


get_days_from_today()

# get_days_from_today("2012-04-30")
