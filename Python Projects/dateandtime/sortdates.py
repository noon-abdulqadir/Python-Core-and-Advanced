from datetime import date
import time

startTime = time.perf_counter()

d1=date(2016,8,12)
d2=date(2016,7,12)
d3=date(2018,8,12)

ldates = [d1, d2, d3]
ldates.sort()

time.sleep(3)

for d in ldates:
    print(d)


endTime = time.perf_counter()

print("Execution Time",endTime-startTime)

