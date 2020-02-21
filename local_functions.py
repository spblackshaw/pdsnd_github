#local_functions.py
import pandas as pd

select_dict = {'City':['washington', 'new york city', 'chicago'],
'Month':['january', 'february', 'march', 'april', 'may', 'june', 'all'],
'Weekday':['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']}


def view_data(pd_frame):
    """
    Takes a pandas dataframe as argument and asks user whether they want to view the data.
    5 rows are shown each time the user presses 'Y'; function exits on any other key press.

    Args:
        (str) pd_frame - name of pandas data frame
    """
    iter_count = int(pd_frame.shape[0] / 5)
    counter = 0
    for i in range(iter_count):
        view_rows = input("\n\nWould you like to view the raw data? (Select 'Y' to continue, or any other key to skip): ").lower()
        if view_rows == 'y':
            print(pd_frame.iloc[counter:counter + 5])
            counter += 5
        else:
            break


def input_list(ulist):
    """ Cleans a list of input selection options for presentation to user:

        Remove 'All' option
        Converts list to string
        Adds 'or' for grammatical sense
        Use Proper Case on items
    """

    filter_all = [x for x in ulist if x != 'all']
    list_str = ', '.join(filter_all).title()
    output = ' or '.join(list_str.rsplit(', ', 1))
    return output
       

def user_input(dict_key, option_dict, select_all=None):
    """
    Takes list of items and item type to be passed as a filter item.
    Asks user to select item type from list or use default of all to ignore filter. 

    Args:
        (str) item - description of items in list.
        (str) option_list - list of item choice for user to select from.
        (str) select_all - if passed then output will default to 'all'.
    
    Returns:
        (str) selection - item that user has selected for filter, or 'all'.
    """
    option_list = option_dict[dict_key]
    select_list = input_list(option_list)
    input_str = "Please select a(n) " + dict_key + " from " + select_list
    if select_all != None:
        input_str = input_str + "; or select 'All' for no filter: "
    else:
        input_str = input_str + ": "

    while True:
        try:
            user_select = input(input_str).lower()
            if user_select in option_list:
                print(user_select.title(), "Selected: \n")
                break
        except:
            print(input_str)    
    return user_select


def month_int(month_name):
    """ Convert month name to integer """

    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 
    'july', 'august', 'september', 'october', 'november', 'december']
    month_int = month_list.index(month_name) + 1
    return month_int


def seconds_concise(duration):
    """ returns amount of seconds as appropriate; year, week, day, hour, minutes """

    seconds_dict = {'year' : 31449600,
                    'week' : 604800,
                    'day' : 86400,
                    'hour' : 3600}
    #if duration is greater than seconds_dict item then use that item
    for key, value in seconds_dict.items():
        if duration >= value:
            output = '%.1f'%(duration / value) + ' ' + key + '(s)'
            break
        else:
            output = '%.1f'%(duration / 60) + ' minute(s)'
    return output


def hour_convert(hour):
    """ adds conversion for 24 hour clock for the uninitiated """

    if hour > 12:
        hour_adj = hour - 12
        output = str(hour) + ' (' + str(hour_adj) + 'pm)'
    else:
        output = str(hour)     
    return output


def main():

    df = pd.read_csv('chicago.csv')
    month = 'april'
    day = 'monday'

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':     
        # filter by month to create the new dataframe
        df = df[df['month'] == month_int(month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
    
    #print(df.iloc[0:4])
    #view_data(df)
    print(df)
           
if __name__ == "__main__":
	main()