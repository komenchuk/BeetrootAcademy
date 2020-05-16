"""
Imports practice

Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.
"""

from datetime import date


def main():
    today = date.today()
    print(f'Today\'s date is: {today}')


if __name__ == "__main__":
    main()
