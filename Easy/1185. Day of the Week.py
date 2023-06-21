import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        date = datetime.datetime(day=day, month=month, year=year)
        return week[date.weekday()]


day = 15
month = 8
year = 1993
result = Solution().dayOfTheWeek(day, month, year)
print(result)
