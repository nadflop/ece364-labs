#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from enum import Enum
from math import sqrt as sqrt
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class TimeSpan:

    def __init__(self, weeks: int, days: int, hours: int):
        if weeks < 0:
            raise ValueError("The argument cannot be negative")
        if days < 0:
            raise ValueError("The argument cannot be negative")
        if hours < 0:
            raise ValueError("The argument cannot be negative")
        if hours < 24 and days < 7:
            self.hours = hours
            self.days = days
            self.weeks = weeks
        elif hours >= 24:
            days += (hours//24)
            hours = hours % 24
            self.hours = hours
            if days >= 7:
                weeks += days//7
                days = days % 7
            self.days = days
            self.weeks = weeks
        else:
            self.hours = hours
            weeks += days//7
            days = days % 7
            self.days = days
            self.weeks = weeks

    def __str__(self):
        return f"{format(self.weeks, '02d')}W {self.days}D {format(self.hours, '02d')}H"

    def getTotalHours(self):
        total = (self.weeks * (7*24)) + (self.days * 24) + self.hours
        return total

    def __add__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        newDays = self.days + other.days
        newHours = self.hours + other.hours
        newWeeks =self.weeks + other.weeks
        t = TimeSpan(days=newDays,hours=newHours,weeks=newWeeks)
        return t

    def __mul__(self, other):
        if isinstance(other, int) == False and isinstance(other,float) == False:
            raise TypeError("An integer or float is expected")
        if other < 0:
            raise ValueError("Integer/float must be greater than 0")
        newDays = round(self.days * other)
        newHours = round(self.hours * other)
        newWeeks = round(self.weeks * other)
        t = TimeSpan(days=newDays,hours=newHours,weeks=newWeeks)
        return t

    def __eq__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days == other.days and self.hours == other.hours and self.weeks == other.weeks:
            return True
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days != other.days or self.hours != other.hours or self.weeks != other.weeks:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days > other.days and self.hours > other.hours and self.weeks > other.weeks:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days < other.days and self.hours < other.hours and self.weeks < other.weeks:
            return True
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days >= other.days and self.hours >= other.hours and self.weeks >= other.weeks:
            return True
        else:
            return False

    def __le__(self, other):
        if isinstance(other, TimeSpan) == False:
            raise TypeError("TimeSpan instance is expected")
        if self.days <= other.days and self.hours <= other.hours and self.weeks <= other.weeks:
            return True
        else:
            return False

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...