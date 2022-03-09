import datetime
from pandas import DataFrame as df
import pandas as pd
from matplotlib import pyplot, style
def values():
    answer = int(input("Press 1 to enter Income\nPress 2 to enter Expense\n --> "))
    if answer == 1:
        date = str(input('Enter Date (YYYY,MM,DD) (optional) \n: --> '))
        try:
            year,month,day=map(int,date.split(','))
            print(day)
            date = datetime.date(year,month,day)
        except :
            date = datetime.date.today()
        while True:
            income = int(input("Enter your income for today if any \n: --> "))
            particular = str(input("Enter Description (Optional) \n: --> "))
            tracker(date,income,0,particular)
            period = str(input("Enter 1 to change period \nEnter 2 to go back \nEnter 3 to Quit \nEnter any key to keep going \n: --> "))
            if period == "1":
                date = str(input('Enter Date (YYYY,MM,DD) (optional) \n: --> '))
                try:
                    year,month,day=map(int,date.split(','))
                    print(day)
                    date = datetime.date(year,month,day)
                except :
                    date = datetime.date.today()
            elif period == "2":
                values()
            elif period == "3":
                exit()
            else :
                pass

    elif answer == 2:
        date = str(input('Enter Date (YYYY,MM,DD) (optional) \n: --> '))
        try:
            year,month,day=map(int,date.split(','))
            print(day)
            date = datetime.date(year,month,day)
        except :
            date = datetime.date.today()
        while True:
            expense = int(input("Enter your expense for today if any \n: --> "))
            particular = str(input("Enter Description (Optional) \n: --> "))
            tracker(date,0,expense,particular)
            period = str(input("Enter 1 to change period \nEnter 2 to go back \nEnter 3 to Quit \nEnter any key to keep going \n: --> "))
            if period == "1":
                date = str(input('Enter Date (YYYY,MM,DD) (optional) \n: --> '))
                try:
                    year,month,day=map(int,date.split(','))
                    print(day)
                    date = datetime.date(year,month,day)
                except :
                    date = datetime.date.today()
            elif period == "2":
                values()
            elif period == "3":
                exit()
            else :
                pass
    else :
        print("Please select a valid input!")
        values()