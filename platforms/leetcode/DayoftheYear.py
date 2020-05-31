# https://leetcode.com/problems/day-of-the-year/
class Solution:
    def dayOfYear(self, date: str) -> int:
        ndays = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        year, month, date = map(int, date.split('-'))
        days = date
        if month > 2 and self.leapYear(year): days += 1
        for i in range(1, month): days += ndays[i]
        return days

    def leapYear(self, year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False
