import csv
import matplotlib.pyplot as plt
from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True

logging.debug('Start of program' + f'\n')

#Choose your csv file
file = input('Paste the path of your desired date/temperature file.'
    ' One has been provided for you, if you wish to observe a demonstration'
    ' of this program: ')

if not file:
    print('You did not choose a file. Goodbye.')

else:

    def get_visual(file):
        """This function uses a csv file, bearing temperatures and dates
    at which those temperatures were recorded, to plot maximum and minimum
    temperature values, by date, within the same visual. Once the file is
    read, a header with column values and their associated indices will be
    printed for the purposes of informing the user which data is desired for
    plotting."""
        
        with open(file) as f:
            reader = csv.reader(f)
            
            # This statement takes in the column names
            header = next(reader)
            
            #This statement will allow you to view your index choices
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
                
                # The statement below we collect the high and low data for
                # row x from their respective indices 
                try:
                    high = int(x[highs_index])
                    low = int(x[lows_index])
                    
                # The statement below takes care of situations in which data
                # is missing
                except ValueError:
                    logging.debug(f'For this date, {date}, we do not have all'
                          ' the data.' + f'\n')
                
                # When the exception is not triggered, we are free to plot
                # the data, using the below statements
                else:
                    dates.append(date)
                    highs.append(int(x[highs_index]))
                    lows.append(int(x[lows_index]))
                    
            fig, ax = plt.subplots(figsize=(15, 10))
            ax.plot(dates, highs, label='Maxes')
            ax.plot(dates, lows, label='Mins')
            plt.xlabel('Date', fontsize=15)
            plt.xticks(fontsize=15)
            plt.ylabel('Temperature', fontsize=15)
            plt.yticks(fontsize=20)
            plt.legend(prop={'size': 17})
            fig.autofmt_xdate()
            fig.suptitle('Max and Min Temperatures by Date', fontsize=15)
            plt.show()
        
    get_visual(file)