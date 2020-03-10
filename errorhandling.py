# x = 42
# y = 3333
# try:
#     print(x /y)
# except ZeroDivisionError as e:
#    print('something went wrong')
# except:
#     print('Some thing rally went wrong')
# finally:
#     print('This always run on success or failure')

x = 45
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Zero division not allowed')
else:
    print('Some thing went wrong')
finally:
    print('This is our final cleanup code')