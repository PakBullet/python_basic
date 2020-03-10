# #to get date and time
# #We need to use datetime library
# from datetime import datetime, date , timedelta
# today = datetime.now()
# #the now function return datetime  objct
# print("Hi Ijaz Sial          Today is " + str(today))

# # timedelta is used to define a period of time
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print("Yesterday was:" + str(yesterday))

                                      # for display sperat day month years
# from datetime import datetime
# current_date = datetime.now()
# print("Day: " + str(current_date.day))
# print("month: " + str(current_date.month))
# print("Year: "  +  str(current_date.year))
# print("Hour: " + str(current_date.hour))


#store date birthday etc

from datetime import datetime
birthday = input("Please enter birthday date (dd/mm/yy)")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print("Birthday " + str(birthday_date))
from datetime import datetime

birthday = input('when is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))