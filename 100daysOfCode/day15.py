import time
timestamp = time.strftime('%H')

print(timestamp)

if int(timestamp)<12 :
    print('Good morning Sir')
elif int(timestamp)>15 and int(timestamp)<=17:
    print('Good Evening Sir')   
elif int(timestamp)>17 and int(timestamp)<=23:
    print('Good Night')
elif int(timestamp)>12:
    print('Good Afternoon Sir')

