import time
import pandas as pd
import numpy as np
import calendar as cal
import local_functions as lf

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\nHello! Let\'s explore some US bikeshare data!\n")
         
    # Get user input for city (chicago, new york city, washington).
    city = lf.user_input('City',lf.select_dict)
    # Get user input for month (all, january, february, ... , june)
    month = lf.user_input('Month',lf.select_dict, 'All')
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = lf.user_input('Weekday',lf.select_dict, 'All')
    
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # add city as column in dataframe
    df['City'] = city

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':     
        # filter by month to create the new dataframe
        df = df[df['month'] == lf.month_int(month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    if df['month'].nunique() == 1:
        popular_month = 'Only ' + cal.month_name[df['month'].mode()[0]] + ' Selected'
    else:
        popular_month = df['month'].mode()[0]
        popular_month = cal.month_name[popular_month]
    # Display the most common day of week
    if df['day_of_week'].nunique() == 1:
        popular_day_of_week = 'Only ' + df['day_of_week'].mode()[0] + ' Selected'
    else:
        popular_day_of_week = df['day_of_week'].mode()[0]                                   
    # Display the most common start hour
    popular_hour = lf.hour_convert(df['hour'].mode()[0])
    print(f'Most Frequent Month: {popular_month}\nMost Frequent Day of Week: '\
        f'{popular_day_of_week}\nMost Frequent Start Hour: {popular_hour}\n')    
    print(f'\nThis took {(time.time() - start_time):.2f} seconds.')                   
    print('-'*40)
    pause = input("Press any key to continue: ")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    # Display most frequent combination of start station and end station trip
    station_combo = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    station_combo_start = station_combo.index[0][0]
    station_combo_end = station_combo.index[0][1]
    print(f'Most Common Starting Station: {popular_start_station}\nMost Common Ending Station: '\
        f'{popular_end_station}\nMost Common Trip: {station_combo_start} - {station_combo_end}\n')    
    print(f'\nThis took {(time.time() - start_time):.2f} seconds.')
    print('-'*40)
    pause = input("Press any key to continue: ")
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    duration = df['Trip Duration'].sum()
    total_travel_time = lf.seconds_concise(duration)

    # Display mean travel time
    avg_duration = df['Trip Duration'].mean()
    avg_trip_time = lf.seconds_concise(avg_duration)
    print(f'Total Travel Time: {total_travel_time}\nAverage Trip Time: {avg_trip_time}\n')
    print(f'\nThis took {(time.time() - start_time):.2f} seconds.')
    print('-'*40)
    pause = input("Press any key to continue: ")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n\n')
    start_time = time.time()

    # Display counts of user types
    customer_count = df[df['User Type'] == 'Customer'].shape[0]
    subscriber_count = df[df['User Type'] == 'Subscriber'].shape[0]
    print(f'User Type Counts:\nCustomer Count = {customer_count}, Subscriber Count = {subscriber_count}')
    
    # Display counts of gender
    if 'Gender' in df.columns:
        female_count = df[df['Gender'] == 'Female'].shape[0]
        male_count = df[df['Gender'] == 'Male'].shape[0]
        gender_null_count = df['Gender'].isna().sum()
        print(f'\nPassenger Counts By Gender: \nFemale Count = {female_count}, Male Count = '\
            f'{male_count}, No Recorded Gender = {gender_null_count}')
    else:
        print('No Gender Statistics in data')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = int(df['Birth Year'].min())
        max_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        year_null_count = df['Gender'].isna().sum()
        year_percent_null = '%.2f'%((year_null_count / len(df.index))* 100)
        print(f'\nAge Statistics: \nEarliest Birth Year: {min_birth_year}\nLatest Birth Year: {max_birth_year}'\
            f'\nMost Common Birth Year: {common_birth_year}\nNo Recorded Birth Date: {year_percent_null}%\n')
    else:
        print("No Birth Date Statistics in Data")
    print(f'\nThis took {(time.time() - start_time):.2f} seconds.')
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        lf.view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()