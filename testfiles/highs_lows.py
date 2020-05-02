import csv
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from datetime import datetime

# print(datetime.strptime('2020-5-2','%Y-%m-%d'))

# filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'  #death valley 温度数据少一行，做异常处理

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    highs,lows,dates = [],[],[]
    for row in reader:
        try:
            date = datetime.strptime(row[2],'%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
    # print(highs, '\n', lows, '\n', dates)

plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
#设置填充颜色及透明度
plt.fill_between(dates, highs,lows,facecolor='blue', alpha = 0.1)

plt.title('Daily high and low temperatures - 2018 \nDeath Valley,CA', fontsize = 20)
# fig = plt.figure(dpi=128, figsize=(10,6))
plt.xlabel('', fontsize = 12)
plt.ylabel('Temp(F)', fontsize = 12)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.gcf().autofmt_xdate()   #自动旋转日期标记
# fig.autofmt_xdate()
plt.show()