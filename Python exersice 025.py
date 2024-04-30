second = int(input('Enter the second'))
day = second // 86400
second = second % 86400
hour = second// 3600 
second = second % 3600
minute = second // 60
second = second % 60
print(day, hour, minute, second)
