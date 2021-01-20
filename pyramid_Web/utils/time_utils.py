from datetime import datetime, timedelta


def today18h():
    today = datetime.today()
    midnight = datetime(today.year, today.month, today.day)
    return midnight + timedelta(hours=18)
