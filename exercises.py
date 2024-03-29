"""Module providing a function for getting random values."""
import random
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_days_from_today(input_date: str) -> int | None:
    """Get days from today

    :param input_date: str - date in ISO format
    :return: int - days from today to the input date

    Function takes date in string format. It is turned into datetime object.
    The result is calculated by subtracting input date from the current date,
    which is defined by datetime.today() function.
    """

    try:
        input_date = datetime.fromisoformat(input_date)
    except ValueError:
        print("Incorrect input format, please enter date in format YYYY-MM-DD")
        return None
    current_date = datetime.now()
    date_subsctract = current_date - input_date
    return date_subsctract.days


def get_numbers_ticket(minimal: int, maximal: int, quantity: int) -> list:
    """Get number for ticket

    :param minimal: int - minimum number, cannot be less than 1
    :param maximal: int - maximum number, cannot be more than 1000
    :param quantity: int - quantity of numbers, must be more
    than minimum and less than maximum
    :return: list - sorted list of random unique numbers

    Function generates a set quantity of random unique numbers in range
    from min to max, returns it in a sorted list.
    """

    ticket_numbers = set()
    try:
        if (
            (minimal < 1 or maximal > 1000)
            or (quantity < minimal or quantity > maximal)
            or (max <= min)
        ):  # if any of these conditions returns True, the function returns an empty list
            return []
    except ValueError:
        return []  # if arguments are of a wrong type, empty list is returned

    while len(ticket_numbers) < quantity:
        ticket_numbers.add(random.randint(minimal, maximal))
    return list(sorted(ticket_numbers))


def normalize_phone(phone_number: str) -> str:
    """Normalize phone number

    :param phone_number: str - phone number as provided by user
    :return: str  - normalized phone number in a uniform format

    Function removes all other symbols, besides numbers and "+" using regex.
    If number lacks country code, the country code is added.
    The resulting string is returned in format +38XXXXXXXXXX
    """

    phone_number = re.sub(r"[^\+\d]", "", phone_number)
    if re.search(r"^\+", phone_number):
        return phone_number
    if re.search(r"^380", phone_number):
        return f"+{phone_number}"
    return f"+38{phone_number}"


def get_upcoming_birthdays(users: list[dict] = None) -> list[dict]:
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
    today = datetime.now().date()
    intermediate = []

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
        user.pop("congratulation_date")  # повертаємо словникам початковий вигляд +-

    for user in intermediate.copy():
        if user["congratulation_date"] - today > timedelta(days=6):
            intermediate.remove(user)
        elif today - user["congratulation_date"] < timedelta(days=-6):
            intermediate.remove(user)
        user["congratulation_date"] = user["congratulation_date"].strftime("%Y.%m.%d")
    return intermediate
