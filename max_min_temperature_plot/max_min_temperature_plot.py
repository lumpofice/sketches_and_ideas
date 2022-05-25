import csv
import matplotlib.pyplot as plt
from datetime import datetime

#Choose your csv file
file = input('Paste the path of your desired date/temperature file: ')

def get_visual(file):
    """This function uses a csv file, bearing temperatures and dates
at which those temperatures were recorded, to plot maximum and minimum
temperature values (by date) within the same visual. Once the file is
read, a header with column values and their associated indices will be
printed for the purposes of informing the user which data is desired for
plotting."""
    with open(file) as f:
        reader = csv.reader(f)
        header = next(reader)
        #View your index choices
        for i, j in enumerate(header):
            print(i, j)
        #Choose your indices
        date_index = int(input('Choose your date index: '))
        highs_index = int(input('Choose your highs index: '))
        lows_index = int(input('Choose your lows index: '))
        dates = []
        highs = []
        lows = []
        for x in reader:
            date = datetime.strptime(x[date_index], '%Y-%m-%d')
            try:
                high = int(x[highs_index])
                low = int(x[lows_index])
            except ValueError:
                print(f'For this date, {date}, we do not have all the data.')
            else:
                dates.append(date)
                highs.append(int(x[highs_index]))
                lows.append(int(x[lows_index]))
        fig, ax = plt.subplots()
        ax.plot(dates, highs)
        ax.plot(dates, lows)
        fig.autofmt_xdate()
        plt.show()
        
get_visual(file)