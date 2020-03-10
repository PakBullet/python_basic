from datetime import datetime, timedelta
birthday = input('When is your birthday date (dd/mm/yyy)? ')
birthday_date = datetime.strptime(birthday, ('%d/%m/%Y'))
print('Birthday date is ' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day befor Birthday is : ' + str(birthday_eve))
