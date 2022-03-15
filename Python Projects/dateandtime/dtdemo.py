import time,datetime
epochseconds = time.time()
print(epochseconds)

t = time.ctime(epochseconds)
print(t)

dt = datetime.datetime.now()
print(f'Current Date: {dt.day}/{dt.month}/{dt.year}')
print(f'Current Time: {dt.hour}:{dt.minute}:{dt.second}')
