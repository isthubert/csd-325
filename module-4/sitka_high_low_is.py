# Isaac St Hubert Module 4.2 11/09/2025
# This program displays the temperature highs and lows using sitka weather data

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Displays the menu detailing options

print("""
Sitka Weather Data

Menu Options:
Highs (view high temperatures in red)
Lows  (view low temperatures in blue)
Exit  (exit the program)
""")

# Opens and reads weather data file

filename = 'sitka_weather_2018_simple.csv'

# Initializes empty lists for dates, highs, and lows

dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
	
	# Adds and appends the low temperatures data

        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


while True:
    choice = input("\nPlease enter your choice of Highs, Lows, or Exit: ")

    if choice == 'Highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    # Creates and formats the plot for lows data

    elif choice == 'Lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 'Exit':
        print("\nGoodbye and thank you for using my program.")
        sys.exit()
