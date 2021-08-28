import pandas as pd
import numpy as np
import time

pd.set_option('expand_frame_repr', False)
pd.set_option('display.colheader_justify', 'center')

CITY_DATA = {   'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv'}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']


"""Loading Data According to Filters"""
def load_data(city, month, day):
    #filename = './Project/' + CITY_DATA[city.lower()]
    filename = './' + CITY_DATA[city.lower()]

    #Exception handling incase files are unable to be read
    try:
        df = pd.read_csv(filename)
    except:
        print('\nOops, an error occurred.')
        print('Looks like the .csv could not be found')
        print('Please ensure that the .csv file and the Python script is in the same directory, and that the .csv files are correctly named:')
        print(', '.join(CITY_DATA.values()))
        print('\nProgram will terminate automatically')
        quit()
    #Exception handling incase files are unable to be read

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month_num = months.index(month.capitalize()) + 1

        df = df[df['Month'] == month_num]

    if day != 'all':
        df = df[df['Day of Week'] == day.capitalize()]

    return df
"""Loading Data According to Filters"""


"""Get User Inputs for Filters"""
def get_filter(cat):
    while True:
        if cat == 'city':
            user_input = input('Please enter the city name for which to filter (Chicago, New York City or Washington):\n')
        elif cat == 'month':
            user_input = input('\nPlease enter the the month for which to filter, use "all" to see all months:\n')
        elif cat == 'day':
            user_input = input('\nPlease enter the the day for which to filter, use "all" to see all days:\n')

        if user_input.upper() == 'EXIT':
            print('\nProgram terminated')
            quit()

        if (cat == 'city') and (user_input.lower() not in CITY_DATA.keys()):
            print('\nYou have entered an invalid city, please try again.')
            print('Availible options are: "Chicago, "New York City" or "Washington"\n')
            continue

        if (cat == 'month') and (user_input.capitalize() not in months):
            print('\nYou have entered an invalid month, please try again.')
            print('Availible options are:')
            print(', '.join(months))
            continue

        if (cat == 'day') and (user_input.capitalize() not in days):
            print('\nYou have entered an invalid day, please try again.')
            print('Availible options are:')
            print(', '.join(days))
            continue

        if cat == 'city':
            print(('\nYou have chosen {} as your city.\n').format(user_input.capitalize()))
        else:
            print(('\nYou have chosen to filer according to {}\n').format(user_input.capitalize()))

        confirmation = input('Is this correct (Y/N)?\n')
        if confirmation.upper() == 'EXIT':
            print('\nProgram terminated')
            quit()
        elif confirmation.upper() == 'Y':
            break
        #End of loop

    return user_input
"""Get User Inputs for Filters"""


"""Main Code"""
while True:
    print('\nWelcome to the bike-share database. At any point if you want to exit you can tipe "exit".\n')

    #Get user input
    chosen_city = get_filter('city')
    chosen_month = get_filter('month')
    chosen_day = get_filter('day')
    #Get user input

    print('\nThis model will display data under the following conditions:')
    print('Data will be show for {}'.format(chosen_city.capitalize()))
    if chosen_month.lower() != 'all':
        print('For the month of {}'.format(chosen_month.capitalize()))
    else:
        print('For all months')
    if chosen_day.lower() != 'all':
        print("Filtered to {}'s\n".format(chosen_day.capitalize()))
    else:
        print('Filtered to all days\n')

    df = load_data(chosen_city, chosen_month, chosen_day)

    #Print raw data
    start_print = 0
    end_print = 5
    while True:
        if start_print == 0:
            user_input = input('Do you want to view raw data (Y/N)?\n').upper()
        else:
            user_input = input('\nDo you want to view next 5 rows (Y/N)?\n').upper()

        if user_input.upper() == 'Y':
            print(df.iloc[start_print:end_print, 1:])
            start_print += 5
            end_print += 5
        elif user_input.upper() == 'N':
            break

        if user_input.upper() == 'EXIT':
            print('\nProgram terminated')
            quit()
    #Print raw data


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Most frequent month
    if chosen_month.lower() == 'all':
        frq_month = int(df['Start Time'].dt.month.mode())
        print('Most frequent month for which service is used is: {}'.format(months[frq_month - 1]))
    #Most frequent month

    #Most frequent day
    if chosen_day.lower() == 'all':
        frq_day = int(df['Start Time'].dt.dayofweek.mode())
        print('Most frequent day for which service is used is: {}'.format(days[frq_day]))
    #Most frequent day

    #Print formatted time for most frequent riding time
    frq_start = int(df['Start Time'].dt.hour.mode())

    if frq_start < 10:
        print('Most Frequent Riding Hour: 0{}:00 to 0{}:00'.format(frq_start, frq_start+1))
    else:
        print('Most Frequent Riding Hour: {}:00 to {}:00'.format(frq_start, frq_start+1))
    #Print formatted time for most frequent riding time

    #Number of riders during time period
    number = df['Start Time'][df['Start Time'].dt.hour == frq_start].count()
    print('Total number of rides during this time = ', number, '\n')
    #Number of riders during time period

    #Popular Start Stations
    pop_start = df['Start Station'].value_counts().idxmax()
    start_count = df.groupby(df['Start Station'])['Start Station'].count().max()
    print('The most popular start station is {} with {} times used'.format(pop_start, start_count))
    #Popular Start Stations

    #Popular End Stations
    pop_start = df['End Station'].value_counts().idxmax()
    start_count = df.groupby(df['End Station'])['End Station'].count().max()
    print('The most popular end station is {} with {} times used'.format(pop_start, start_count))
    #Popular End Stations

    #Popular Route
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']

    pop_route = df['Route'].value_counts().idxmax()
    route_count = df.groupby(df['Route'])['Route'].count().max()

    print('The most popular route is {} with a total of {} tripes'.format(pop_route, route_count) + '\n')
    #Popular Route

    #Travel Times
    print('Average travel time is: {0:.2f} minutes'.format((df['Trip Duration'].mean()/60)))
    print('Total travel time is: {0:.2f} days'.format((df['Trip Duration'].sum())/60/60/24) + '\n')
    #Travel Times

    #User Count
    print('Summary of users by type of users:')
    print(df.groupby(df['User Type'])['User Type'].count().to_string(header=False) + '\n')
    #User Count

    if chosen_city.lower() != 'washington':
        #Gender Count
        print('Summary of users by Gender:')
        print(df.groupby(df['Gender'])['Gender'].count().to_string(header=False) + '\n')
        #Gender Count

        print('Earliest birth year (oldest user) is born in: {0:.0f}'.format((np.nanmin(df['Birth Year']))))
        print('Most recent birth year (youngest user) is born in: {0:.0f}'.format((np.nanmax(df['Birth Year']))))
        print('Most common birth year is: {}\n'.format(int(df['Birth Year'].mode())))

    print("\nThis took {0:.2f} seconds.".format(time.time() - start_time))
    print('-'*40)

    user_input = input('Would you like to try again? (Y/N)\n')
    if (user_input.upper() == 'N') or (user_input.upper() == 'EXIT'):
        print('\nProgram Terminated')
        break
"""Main Code"""
