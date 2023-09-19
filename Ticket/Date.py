import datetime
class Date:
    @staticmethod
    def date(dlist: list):
        dlist = list(map(int, dlist))
        return datetime.date(dlist[0], dlist[1], dlist[2])
    @staticmethod
    def today():
        return datetime.date.today()