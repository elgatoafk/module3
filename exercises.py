def get_days_from_today(input_date: str) -> int | None:
    """Get days from today

    :param input_date: str - date in ISO format
    :return: int - days from today to the input date

    Function takes date in string format. It is turned into datetime object.
    The result is calculated by subtracting input date from the current date, which is defined by datetime.today() function.
    """
    from datetime import datetime

    try:
        input_date = datetime.fromisoformat(input_date)
    except:
        print("Incorrect input format, please enter date in format YYYY-MM-DD")
        return None
    current_date = datetime.today()
    date_subsctract = current_date - input_date
    return date_subsctract.days


# TODO: add functionality
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    import random

    ticket_numbers = set()

    """Get number for ticket

    :param min: int - minimum number, cannot be less than 1
    :param max: int - maximum number, cannot be more than 1000
    :param quantity: int - quantity of numbers, must be more than minimum and less than maximum
    :return: list - sorted list of random unique numbers

    Function generates a set quantity of random unique numbers in range from min to max, returns it in a sorted list.
    """
    if (min < 1 or max > 1000) or (
        quantity < min or quantity > max
    ):  # if any of these conditions returns True, the function returns an empty list
        return list()
    else:
        while len(ticket_numbers) < quantity:
            ticket_numbers.add(random.randint(min, max))
        ticket_numbers = list(sorted(ticket_numbers))
        return ticket_numbers


def normalize_phone(phone_number: str) -> str:
    """Normalize phone number

    :param phone_number: str - phone number as provided by user
    :return: str  - normalized phone number in a uniform format

    Function removes all other symbols, besides number and "+" using regex. If number lacks country code, the country code is added.
    The resulting string is returned.
    """
    pass


def get_upcoming_birthdays():
    """ """
    pass
