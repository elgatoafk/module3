def get_days_from_today(input_date: str) -> int:
    """Get days from today

    :input_date: str - date in ISO format
    :return: int - days from today to the current date

    Function takes date that we need to compare in string format. It is then turned into datetime object.
    The result is calculated by subtracting input date from the current date, which is defined by datetime.today() function.
    """
    from datetime import datetime

    input_date = datetime.fromisoformat(input_date)
    current_date = datetime.today()
    date_subsctract = current_date - input_date
    return date_subsctract.days
