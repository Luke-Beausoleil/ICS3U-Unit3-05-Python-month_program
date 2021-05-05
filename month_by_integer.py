#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program tells the user the month from an inputted integer


def main():
    # this function receives input and displays the month

    # input
    month = int(input("Enter a month number (1 - 12): "))

    # process & output
    if month == 1:
        print("\nJanuary")
    elif month == 2:
        print("\nFebruary")
    elif month == 3:
        print("\nMarch")
    elif month == 4:
        print("\nApril")
    elif month == 5:
        print("\nMay")
    elif month == 6:
        print("\nJune")
    elif month == 7:
        print("\nJuly")
    elif month == 8:
        print("\nAugust")
    elif month == 9:
        print("\nSeptember")
    elif month == 10:
        print("\nOctober")
    elif month == 11:
        print("\nNovember")
    elif month == 12:
        print("\nDecember")
    else:
        print("\nInvalid input. Enter an integer from 1 - 12.")
    print("\nDone.")


if __name__ == "__main__":
    main()
