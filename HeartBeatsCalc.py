# the formula for calculating your maximum heart rate in beats per minute is 220 minus your age in years.
# Your target heart rate is a range that is 50-85% of your maximum heart rate. Create a class called Rates.
# The class attributes should include the person's first name, last name, year of birth and the current year.
# Your class should have a constructor that receives this data as parameters. For each attribute provide
# a property with set and get accessors. the class also should include a  property that calculates and returns
# the person's age (in years), a property that calculates and returns the person's maximum heart rate and properties that
# calculate and return the person's minimum and maximum target heart rates.
# an app that prompts for the person's information, instantiates an object of class Rates and displays the information
# from that object, including the person's first name, last name, and year of birth. then calculates and displays
# the person's age in years, maximum heart rate and target-heart-rate range.
#########################################Answer################################################
import re

from datetime import date


class Rates:
    """
    class Rates calculate age, max heart rate, target heart range givem name, birthyear, currentyear
    """

    def __init__(self, firstName, lastName, yearOfBirth, currentYear):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__yearOfBirth = yearOfBirth
        self.__currentYear = currentYear

    # way1: manual define getter and setter
    def getFirstName(self):
        """
        FirstName getter
        :return: self.__firstName
        """
        return self.__firstName

    def setFirstName(self, firstName):
        """
        FirstName setter
        :param str firstName: person's first name
        :return: None
        """
        self.__firstName = firstName

    # firstName property-encapsulation
    firstName = property(getFirstName, setFirstName)

    # way2: use decorator
    @property  # same as getter
    def lastName(self):
        """
        lastName Property-getter
        :return: self.__lastName
        """
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName):
        """
        lastName Property-setter
        :param str lastName: person's last name
        :return: None
        """
        self.__lastName = lastName

    @property
    def yearOfBirth(self):
        return self.__yearOfBirth

    @yearOfBirth.setter
    def yearOfBirth(self, value):
        self.__yearOfBirth = value

    @property
    def currentYear(self):
        return self.__currentYear

    @currentYear.setter
    def currentYear(self, value):
        self.__currentYear = value

    @property
    def age(self) -> int:
        return self.currentYear - self.yearOfBirth

    @property
    def maxHeartRate(self) -> int:
        return 220 - self.age

    @property
    def minTargetHeartRate(self) -> float:
        return 0.5 * self.maxHeartRate

    @property
    def maxTargetHeartRate(self) -> float:
        return 0.85 * self.maxHeartRate

    def __repr__(self):
        return (
            f"First Name: {self.firstName:<20s}Last Name: {self.lastName:<20s}Year of Birth: {self.yearOfBirth:<20d}Age: {self.age:<20d}\n"
            f"Maximum Heart Rate: {(str(self.maxHeartRate) + ' beats/minute'):<42s} Target Heart Range: {self.minTargetHeartRate:.0f} - {self.maxTargetHeartRate:.0f} beats/minute")


def main():
    while True:
        try:
            firstName, lastName = input(
                "Please enter your first name and last name seperated by comma(all letters(space,'-' allowed), min 1 char,max 20 chars):").strip().split(
                ',')
            for name in (firstName, lastName):
                if not (0 < len(name) <= 20 and name.replace(" ", "").replace("-", "").isalpha()):
                    raise ValueError("Error: Invalid input! "
                                     "First Name and Last Name must be all letters(space and '-' are allowed)"
                                     " and their lengths are 1-20 characters!")
            else:
                break
        except ValueError as v:
            print(v)

    currentYear = date.today().year

    while True:
        try:
            regex = r"^\d{4}$"
            match = re.search(regex, input("Please enter your birth year(YYYY):").strip())
            if match is not None and int(match.group()) <= currentYear:  # match.group() return matched str
                birthYear = int(match.group())
                break
            else:
                raise ValueError(
                    "Error: Invalid input! Birth Year must be a four digit number and smaller than or equal to current year!")
        except ValueError as v:
            print(v)

    rate = Rates(firstName, lastName, birthYear, currentYear)
    print(rate)


main()