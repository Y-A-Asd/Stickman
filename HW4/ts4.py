import time


class Birthday:
    def __init__(self,days,month,year):
        self.days = days
        self.month = month
        self.year = year
        self.now = time.gmtime()
        self.pers = time.strptime((f'{self.year}-{self.month}-{self.days}'), '%Y-%m-%d')
#///////////////////time.struct_time(tm_year=2023, tm_mon=9, tm_mday=13, tm_hour=16, tm_min=48, tm_sec=36, tm_wday=2, tm_yday=256, tm_isdst=0)

    def age_in_years(self):
        age = self.now.tm_year - self.pers.tm_year
        if self.pers.tm_mon > self.now.tm_mon or (self.pers.tm_mon == self.now.tm_mon and self.pers.tm_mday > self.now.tm_mday):
            age -= 1
        print(f"Your age is: {age} years")
    # def age_in_years(self):
    #
    #     # print("\nyear:", pers.tm_year)
    #     # print("mounth:", pers.tm_mon)
    #     # print("day:", pers.tm_mday)
    #     # print("\nyear:", now.tm_year)
    #     # print("month:", now.tm_mon)
    #     # print("day:", now.tm_mday)
    #     age = self.now.tm_year - self.pers.tm_year
    #     if self.pers.tm_mon > self.now.tm_mon:
    #         age = age - 1
    #     print(f"your age is : {age}")
    # def age_in_hours(self):
    #     y = self.now.tm_year - self.pers.tm_year
    #     m = self.now.tm_mon - self.pers.tm_mon
    #     d = self.now.tm_mday - self.pers.tm_mday
    #     y_h = y * 365 * 24 + m * 30 * 24 + d * 24
    #     print(f"your age in hours is : {y_h}")
    def age_in_hours(self):
        birth_time = time.mktime(self.pers)
        current_time = time.mktime(self.now)
        age_seconds = current_time - birth_time
        age_hours = age_seconds / 3600  # 3600 seconds in an hour
        print(f"Your age in hours is: {age_hours} hours")
#///////////////////////////////////////////  چقدر مونده به تولد
    def rem(self):

        month = self.pers.tm_mon - self.now.tm_mon
        day = self.pers.tm_mday - self.now.tm_mday
        if month < 0:
            month = 12 + month
        if day < 0:
            day = 30 + day
        print(f"your birth date is at {month} months and {day} days")


    # def rem(self):
    #     current_time = time.localtime()
    #     next_birthday_year = current_time.tm_year
    #     birth_date = time.struct_time(
    #         (next_birthday_year, self.month, self.day, self.hour, self.minute, self.second, 0, 0, 0))
    #
    #     if time.mktime(current_time) > time.mktime(birth_date):
    #         next_birthday_year += 1
    #         birth_date = time.struct_time(
    #             (next_birthday_year, self.month, self.day, self.hour, self.minute, self.second, 0, 0, 0))
    #
    #     remaining_seconds = time.mktime(birth_date) - time.mktime(current_time)
    #     remaining_hours = remaining_seconds / (60 * 60)
    #     return remaining_hours

joun1= Birthday('10','12','2019')
joun1.age_in_years()
joun1.age_in_hours()
joun1.rem()

joun= Birthday('12','8','2022')
joun.age_in_years()
joun.age_in_hours()
joun.rem()
