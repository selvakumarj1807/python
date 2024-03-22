print("Date time package in python : ")
print("------------------------------")


print("** date format **")
print("-----------------")
print("")

import datetime as dt

current_date = dt.datetime.now()

print('Current Date  : ',current_date)

format_date = current_date.strftime("%A %B %d %Y")

formatted_date = current_date.strftime("%d / %B / %Y")

print('Date Format 1 : ',format_date)

print('Date Format 2 : ',formatted_date)
