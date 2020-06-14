import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# initiate months, their indices and days of week
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while(city not in CITY_DATA):
        city = input("Please select a city: (chicago, new york city or washington)\n")
   

    # get user input for month (all, january, february, ... , june)
    month = ""
    while(month not in months):
        month = input("Please input the month for which you need the data: (all, january, february, ... , june)\n")
        if(month=='all'):
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = 0
    while(day not in days):
        day = input("Please enter the day of week for which you need the data: (all, monday, tuesday ... etc)\n")
        if(day=='all'):
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # read city data
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # separate month data
    df['month'] = df['Start Time'].dt.month

    # separate day of week data
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # separate hour data
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if(month != 'all'):
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week
    df = df[df['day_of_week'] == day.title()] if (day != 'all') else df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'].value_counts().idxmax())

    # display the most common day of week
    print(df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    print(df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].value_counts().idxmax())


    # display most commonly used end station
    print(df['End Station'].value_counts().idxmax())


    # display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station','End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal travel time:')
    total_travel_series = df['End Time'] - df['Start Time']
    print(sum(total_travel_series, datetime.timedelta(0,0)))


    # display mean travel time
    print('\nAverage travel time:')
    print(total_travel_series.mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Year Of Birth' in df.columns:
        # earliest
        print(df['Year Of Birth'].min())
        # most recent
        print(df['Year Of Birth'].max())
        # most frequent
        print(df['Year Of Birth'].value_counts().idxmax())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
