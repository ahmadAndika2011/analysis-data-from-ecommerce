from numpy import ma
import yfinance as yf
import numpy as np
import pandas as pd

data = yf.download("AMZN", start="2023-01-01", end="2024-01-01")
value_close = np.array(data["Close"])
data_close = []
for i in value_close:
    data_close.append(i[0])
data_close = np.array(data_close)


# ? mean
mean_data = 0
for i in data_close:
    mean_data += i
mean_data /= len(data_close)
mean_data = mean_data
print(f"Mean : {mean_data}\n")

# ? median
for i in range(len(data_close)):
    for j in range(0, len(data_close) - i - 1):
        if data_close[j] > data_close[j+1]:
            data_close[j], data_close[j+1] = data_close[j+1], data_close[j]

length_data = len(data_close)
if length_data % 2 == 1:
    median_data = data_close[length_data//2]
else:
    list_length_data = [(length_data // 2) - 1, length_data//2]
    median_data = (data_close[list_length_data[0]] +
                   data_close[list_length_data[1]]) / len(list_length_data)

print(f"Median : {median_data}\n")


# ? daily return
daily_return = []
for i in range(0, len(data_close)):
    if i == 0:
        daily_return.append(0)
    else:
        daily_return.append(
            (data_close[i] - data_close[i-1]) / data_close[i-1] * 100)

daily_return = np.array(daily_return)
print(f"Daily return : {daily_return}\n")

# ? standar deviasi
selisih = data_close - mean_data
kuadrat_selisih = selisih**2

length_kuadrat = len(kuadrat_selisih)
total_of_kuadrat = 0
for value in kuadrat_selisih:
    total_of_kuadrat += value

variance_data = total_of_kuadrat / length_kuadrat

std = variance_data ** 0.5
print(f"Standar deviasi : {std}\n")

# ? Moving average
moving_average = []
for i in range(len(data_close)):
    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
        moving_average.append(0)
    else:
        ma_7 = (data_close[i] + data_close[i-1] + data_close[i-2] +
                data_close[i-3] + data_close[i-4] +
                data_close[i-5] + data_close[i-6])
        moving_average.append(ma_7 / 7)

moving_average = np.array(moving_average)
print(f"Moving average 7 days : {moving_average}\n")

# ? best day
data = [3, 200, 20, 1]
point = []
best_day = None
for i in range(0, len(data_close)):
    point = []  # reset kembali
    for j in range(0, len(data_close)):
        if data_close[i] > data_close[j]:
            point.append(data_close[i])
            if len(point) == (len(data_close)-1):
                best_day = data_close[i]

print(f"Hari dengan Kenaikan tertinggi : {best_day}\n")
