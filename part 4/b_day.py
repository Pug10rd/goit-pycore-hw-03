from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    congrats = []
    today = datetime.today().date()
    for user in users:
        b_day = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        b_day_now = datetime(
            year=today.year, month=b_day.month, day=b_day.day).date()
        con_date = ''

        if b_day_now < today:
            con_date = f"{datetime(year=today.year + 1, month=b_day.month, day=b_day.day).date()}"

        else:
            days_difference = (b_day_now - today).days
            if days_difference <= 7:
                if b_day_now.isoweekday() > 5:
                    week_day = b_day_now.isoweekday()

                    match week_day:
                        case 6:
                            con_date = f"{b_day_now + timedelta(days=2)}"
                        case 7:
                            con_date = f"{b_day_now + timedelta(days=1)}"
                        case _:
                            con_date = f'{b_day_now}'
                else:
                    con_date = f'{b_day_now}'
            else:
                pass
                
            person = {
                "name": user["name"],
                "congratulation_date": con_date
                }
            if con_date:
                congrats.append(person)

    return print(f'Список привітань на цьому тижні: {congrats}')


# this dictionary is used for test
users = [
    {"name": "John Doe", "birthday": "2001.06.18"},
    {"name": "Jane Smith", "birthday": "1990.06.25"},
]

get_upcoming_birthdays(users)


