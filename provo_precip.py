"""Working with CSV stored data"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/provo_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Emumerate() returns both the index and value of each item as you loop through the list.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and precipitation quantity from this file.
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp_d = float(row[3])
        dates.append(current_date)
        prcp.append(prcp_d)

print(prcp)

# Plot the precipitation amount.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, prcp, c='blue', linewidth=1)

# Format plot.
ax.set_title("Daily precipitation, 1994", fontsize=24)
ax.set_xlabel('Date', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (in)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=10)

plt.show()