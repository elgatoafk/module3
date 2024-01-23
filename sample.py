def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Get upcoming birthdays

    :param users: list[dict] - list of dictionaries, with names and birthdays
    :result: list[dict] - list of dictionaries of colleagues that you
    need to congratulate in the next 7 days including today (birthdays on weekends
    are moved to the next Monday)

    Function checks if the congratulation date is in the next seven days.
    If it is on weekend, date is adjusted using nested weekend_adjuster()
    function. The resulting list is once again checked for the condition,
    object that does not fit is removed from the list.

    """
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta

    today = datetime.today().date()
    today.year
    intermediate = list()

    def weekend_adjuster(congratulation_date: datetime) -> datetime:
        """Weekend adjuster

        :param congratulation_date: datetime - date on which colleague
        receives congratulations
        :result: datetime - congratulation date with adjustment
        made for weekends (moved to nearest Monday)

        Function checks if the congratulation date is a weekday or a weekend.
        For weekends, date is moved to Monday, for weekdays,
        date is returned without changes.
        """
        if congratulation_date.weekday() < 5:
            return congratulation_date
        elif congratulation_date.weekday() == 5:
            return congratulation_date + timedelta(days=2)
        else:
            return congratulation_date + timedelta(days=1)

    for user in users:
        user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user.update({"congratulation_date": user["birthday"].replace(year=today.year)})
        if user["congratulation_date"] < today:
            if (
                user["congratulation_date"] + relativedelta(years=1) - today
            ) <= timedelta(days=6):
                print((user["congratulation_date"] + relativedelta(years=1) - today))
                intermediate.append(
                    {
                        "name": user["name"],
                        "congratulation_date": weekend_adjuster(
                            (user["congratulation_date"] + relativedelta(years=1))
                        ),
                    }
                )

            # else do nothing
        elif user["congratulation_date"] - today <= timedelta(days=6):
            intermediate.append(
                {
                    "name": user["name"],
                    "congratulation_date": weekend_adjuster(
                        (user["congratulation_date"])
                    ),
                }
            )
        user.pop("congratulation_date")  # повертаємо словнику початковий вигляд +-

    for user in intermediate:
        if user["congratulation_date"] - today > timedelta(days=6):
            intermediate.remove(user)
        elif today - user["congratulation_date"] < timedelta(days=-6):
            intermediate.remove(user)
    return intermediate
