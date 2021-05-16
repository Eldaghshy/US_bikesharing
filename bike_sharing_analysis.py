#First, I started by importing the needed libraries for making the program.
import time
import pandas as pd
import numpy as np

#city_data is a dictionary that contains the names of the cities as keys and their files I have in store in my working directory as values.

city_data = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

#choices here is an empty dictionary that will be used in order to use the choice that's made in get_filters(),
#to let the program understand which file and city we will be referring to, in order to analyze it.

choices = {}

#get_filters() is a function I created to take the choices of the user and return as output for the other functions ,
#its lines maybe are too long but very efficient and error free.

def get_filters():
    #First, a welcome message for the user to let the user know what they are exploring.
    print('Hello! Let\'s explore some US bikeshare data!')

    #I made a variable named loopy in order to use as a condition for while loop, So that as long as loopy=0 the loop won't stop.
        #the purpose of that is the function won't rest until it gets a valid user input.

    loopy=0

    #city is an empty string which will store the choice the user will make and will be returned as an output of this function.

    city=""

    #I assigned the keys of choices to be equal to the output of user input put in country_choice in the next code chunk.
    choices["1"],choices["2"],choices["3"]= city_data.keys()

    while loopy == 0:

        #I made country_choice to take user input of the wanted State to analyze and the choice will be in numbers making it case insensitive.

        country_choice=input('''\nWhich state would you like to explore?\n
1: Chicago
2: New York City
3: Washington
\nYour choice: ''')


        #First I check within the next code lines if the user input is as one of the keys of choices dictionary so that the choices
        #of the user are constrained to be on these choices only

        #otherwise the else block will be run making loopy=0 and will loop over country_choice until the condition of valid input is met.

        if country_choice in choices.keys():

            #When the condition is met, I iterate over the choices keys and values through .items().

            #choice is for choices keys, value is for choices values.

            for choice,value in choices.items():

                #During iteration it will check over every key in choices to see if it matches with choice key,
                #if not it will pass the current key and will go for the next one, until the condition is met.

                if country_choice == choice:

                    #When the condition is met what happens is that value gets added to city empty string,
                    #which will be returned as output from my get_filters function and lastly loopy will be 1 breaking the while loop
                    #after satisfying all the conditions required for a valid input.

                    city+=value
                    loopy=1
                else:
                    continue
        else:

            #Here when the input was invalid the program prints a message to let the user have insight of having wrong input.
            #And loopy keeps the loop ongoing looking for a valid input from the user.

            print("\nYou have entered invalid input, please try again! ")
            loopy=0

    #I use loopy again but this time as loopy=1 now, I will make the next while loop condition is loopy being =1
    #the loop will resume to run.

    while loopy==1:

        #In filters I made it ask the user if he/she wants the filtering process depending on day, month or both or none.

        #none means that the user will see all the days with all months.

        filters=input('''"\nWould you like to filter by day , month or both or none?"
1: Month
2: Day
3: Both
4: None
\nYour choice: ''')
        #I made if conditions which will take your choice and start to process it according to the user's choice.

        # No filters as it will be none.

        if filters == '4':
            month,day="all","all"
            #loopy =2 to break the while loop.
            loopy=2

        # Month filter.

        elif filters == '1':

            #Here since it will be filtered by the month only day will be stated as all and stored as the output returned by the function.

            day= "all"
            #I made while loop to run over the try/expect blocks till a valid input is entered by the user
            #,otherwise this block will keep running asking for a valid input.
            while True:
                #In try block I put the months choices so that they user can choose from them and the choice will be integer using int().
                try:
                    month=int(input('''\nWhich month would you like to look for?
1: January
2: February
3: March
4: April
5: May
6: June
\nYour choice: '''))

                    #Then I added if condition to make sure that if the choice is within the range of 1 to 6 as 7 in range is excluded.

                    if month in range(1,7):

                        #As soon as the condition is met the loop will break and then it will go for

                        #loopy being equal 2 as it is outside of try/expect block.

                        break

                    #If the choice wasn't in range of these numbers the else block will keep looping as loopy will be equal one
                    #telling the program to keep running and let the user have the message warning the user that he/she has put wrong input.

                    else:

                        print("\nYou have entered invalid input, please try again!")

                #The purpose of expect here is to be able to deal with keyboard interruption or any problem of that sort as I made the output
                #must be an int the error will be value error making it set loopy = 1 and make the code block in try run again
                #asking the user to put valid input.

                except ValueError:
                    print("\nYou have entered invalid input, please try again!")

            loopy=2

        # Day filter.

        elif filters =='2':

            #In try block I put the week days choices so that they user can choose from them and the choice will be integer using int().

            while True:

                try:
                    day=int(input('''\n Which day would you like to look for?
1: Monday
2: Tuesday
3: Wednesday
4: Thursday
5: Friday
6: Saturday
7: Sunday
\nYour choice: '''))

                    #Then I added if condition to make sure that if the choice made is within the range of 1 to 7 as 8 in range is excluded.

                    if day in range(1,8):

                        #When the conidtion is met the loop will break getting to loopy =2 breaking the whole loop.

                        break

                    #If the choice wasn't in range of these numbers the else block will keep looping as loopy will be equal one
                    #telling the program to keep running and let the user have the message warning the user that he/she has put wrong input.

                    else:

                        print("\nYou have entered invalid input, please try again!")

                #The purpose of expect here is to be able to deal with keyboard interruption or any problem of that sort as I made the output
                #must be an int the error will be value error making and make the code block in try run again asking the user to put valid input.

                except ValueError:
                    loopy=1
                    print("\nYou have entered invalid input, please try again!")
            #Since it is day filter, month will be all.
            month="all"
            #loopy=2 to break the while loop.
            loopy=2

        # Month and day filters

        elif filters =="3":

            #Here I made the while loop to run over the try/expect blocks specifically.

            while True:

                #In try block, I aimed that it takes 2 inputs from the user since that is the user's filtering preference.

                try:
                    day=int(input('''\nWhich day would you like to look for?
1: Monday
2: Tuesday
3: Wednesday
4: Thursday
5: Friday
6: Saturday
7: Sunday
\nYour choice: '''))
                    month=int(input('''\nWhich month would you like to look for?
1: January
2: February
3: March
4: April
5: May
6: June
\nYour choice: '''))

                    #After storing these choices in day and month, I put a condition if day input in between 1 to 7 since 8 is excluded in ranges,
                    #And month being in between 1 to 6 as 7 is excluded in range.
                        #As a result the loop will break using break statement.

                    if day in range(1,8) and month in range(1,7):
                        break

                    #If the condition stated above one or both of them isn't met we will go for else block which will inform the user that,
                    #the input was invalid.

                    else:
                        print("\nYou have entered invalid input in either the month or the day, please try again!")

                #The purpose of expect here is to be able to deal with keyboard interruption or any problem of that sort as I made the output
                #must be an int the error will be value error making and make the code block in try run again asking the user to put valid input.

                except ValueError:
                    print("\nYou have entered invalid input, please try again!")
            #loopy=2 to break the whole while loop.
            loopy=2

        #Here it refers to the starting while loop that takes the filtering preference choices if the user choice isn't in one of
        #the 4 conditional blocks then it will tell the user your input is invalid turning loopy =1 and make the loop keep running.

        else:
            loopy=1
            print("You have entered invalid input, please try again!")

    #As a result we returned the city and either of the month and the day depending on the choices of the user.

    return city, month,day
    print('-'*40)

#Here it takes the output from the previous function and use it to process the data.

def load_data(city,month,day):

    #According to the city choice which will be equal to city_data keys which will be indexed to retrieve the value which is file of the city.

    df = pd.read_csv(city_data[city])

    #converting the Start Time column into date time so that we can prepare it to be analyzed in terms of month,day and hour in the next steps
    #using dt accessor which stands for datetime, to access the date components and save them as columns ["hour","month","day"]

    df["Start Time"] = pd.to_datetime(df['Start Time'])
    df["hour"] = pd.Series(df["Start Time"]).dt.hour
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"]=df["Start Time"].dt.weekday

    # If input was all in month it, all the months will be presented, otherwise the number taken from the first function will
    #be the month we filter.

    if month != 'all':

        # I already filtered the month of choice in the last function. So, I just used it directly.

        df = df[df['month'] == month]

    # If input was all in weekdays it, all the months will be presented.
        #otherwise, we will take the number we took from the previous function and add it as the filter for our weekday.

    if day != 'all':

        #since the weekday score starts by zero and choice started by 1,
            #I added 1 to the numbering of the column to make it compatible with the filter.

        df = df[df['day_of_week']+1 == day]

    #The output of this function will be dataframe read from the file.

    return df

#time_stats is a function which will calculate the most common hour of day for bikesharing along with the most common day and month.

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month, using mode and get the first result using indexing by [0].

    common_month=df['month'].mode()[0]
    print('Most popular month is:',common_month)

    # display the most common day of week, using mode and get the first result using indexing by [0].
    #but the output of common_weekday will be a number so I used that number as the index for the elements in the list I made weekdays.

    common_weekday=df['day_of_week'].mode()[0]
    weekdays=["Monday","Tuesday",'Wednesday','Thursday','Friday','Saturday','Sunday']

    #By using the index out of common_weekday for our list weekdays the name of the day will be printed to the user as a result.

    print('Most popular weekday is:',weekdays[common_weekday])

    # display the most common start hour and used .value_counts() that I searched for some time to give the frequency needed in here.

    df['hour'] = df['Start Time'].dt.hour

    #using popular_hour, I will store the most frequent hour in the dataset according to the filtering and
    #frequency will represent the highest value count of the most common hour presenting it to the user using [0] to pick the highest one.

    popular_hour,frequency = df['hour'].mode()[0],df['hour'].value_counts()[0]

    print('\nMost Popular Start Hour is {} \nits count={}.'.format(popular_hour,frequency))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#station_stats is a function to show the most popular stations like the start station and end station along with the most common trip.

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #I made common start to show the mode or the most frequent starting station and used freq_end to show the frequency of that station

    common_start,freq_start = df['Start Station'].mode()[0],df['Start Station'].value_counts()[0]

    #I made common start to show the mode or the most frequent starting station and used freq_end to show the frequency of that station.

    common_end,freq_end = df['End Station'].mode()[0],df['End Station'].value_counts()[0]

    #I created start_to_end column which will have the start station added to it the end station in order to have full trip in a column.

    df['start_to_end']=df['Start Station']+ " to " + df['Start Station']

    #Using the column I just created, I will look for the mode as the common_track and its value as frequency saved as freq_track.

    common_track,freq_track= df["start_to_end"].mode()[0],df["start_to_end"].value_counts()[0]

    #The print messages will show the user the most common start,end stations and trip with their count too.

    print("\nThe most popular start station is {} \nits counts={} ".format(common_start,freq_start))
    print("\nThe most popular end station is {}  \nits counts={} ".format(common_end,freq_end))
    print("\nThe most popular track is {} \nits counts={} ".format(common_track,freq_track))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#trip_duration_stats is a function to calculate the sum of trips and their mean from the Trip duration column.

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time by summing them up.

    total_travel=df["Trip Duration"].sum()

    # display mean travel time using mean().

    average_travel=df["Trip Duration"].mean()

    #The messages that will be print to the user showing the sum of the trips and their mean.

    print("\nIn this dataset, the total time of travel is {} and the average is {}.".format(round(total_travel),round(average_travel)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#user_stats is a function that shows the number of customers and subscribers in bikeshare and even some info about them like gender,
#date of birth.

#The purpose of adding city as an argument is just to mention that Washington has no recording for gender or year of birth
#so that we can exclude them without making any errors or problems in the program.

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #subs_count,customer are counting the number of subscribers and customers respectively.

    subs_count,customer=df["User Type"].value_counts()[0],df["User Type"].value_counts()[1]
    print("The number of Subscribers:",subs_count)
    print("The number of Customers:",customer)

    #I made a condition if the city output from get_filters isn't Washington the values of gender and date of birth will be processed.

    if city != "Washington":

        #Since, I saw that males has higher count so I indexed them by [0] and females by [1] to store them in male,female variables.

        male,female=df["Gender"].value_counts()[0],df["Gender"].value_counts()[1]
        print("\nThere are {} Males and {} Female in {} dataset.".format(male,female,city))

        #earliest refers to the older person in the filtered dataset
        #and most_recent refers to the youngest person in the dataset printing their date of birth.

        earliest,most_recent=df["Birth Year"].min(),df["Birth Year"].max()

        #Here I store the most common year of birth of people in the bikeshare.

        most_common=df["Birth Year"].mode()[0]

        #In the next line the info I collected gets viewed to the user to let them know about such info.

        print('''\nThe earliest user was born in {} and the most recent user was born in {},
Meanwhile most users were born in {}.'''.format(round(earliest),round(most_recent),round(most_common)))
    else:
        print("Washington data has no records for neither gender nor year of birth, only the user type data will be displayed.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#data_displayer is a function that aims to know if the user wants to see 5 rows from the dataset to explore it or not.

def data_displayer(df):

    #It all starts with a while loop which have try/expect block.

    while True:

        #the try block aims to have user input showing user's preference to see the data or not.

        try:
            view_data = int(input("""Would you like to view 5 rows of individual trip data??
1: Yes
2: No
\nYour choice: """))

            #start_loc is variable to be changed in the while to increase the index of rows everytime the process is done.
            #and then we add 5 to it in the range of the dataframe to make the while loop iterate each 5 rows each time.

            start_loc = 0

            #as long as it is equal 1 then the code will run going to take start_loc in a range
            #as index and put the end as start_loc+5 to have 5 rows to be seen by the user.

            if view_data != 2:
                print(df.iloc[start_loc:start_loc+5])
                print(df["day_of_week"].iloc[start_loc:start_loc+5])
                start_loc += 5

                #Then the value of start_loc increases by 5 so that when it loops against it prints the next 5 rows until the user chooses no in the view_data.

                #The purpose of letting this while loop getting inside the other is that the first input message doesn't come again, to be run
                #once if it was correct to run and then go for this next block keep running it, until the user is satisfied with data he/she saw.

                while True:

                #I use try/expect to let only the valid choices run which 1 or 2, otherwise the program will recognize the input as invalid one asking
                #for a valid input.

                    try:

                        #In the try block I used view_display to take the user preference to see the dataset or not.

                        view_display = int(input("""Do you wish to want to see another 5 rows?
            1: Yes
            2: No
            \nYour choice: """))

                        #if the choice is 2 the program will break to go for the next code chunk.

                        if view_display == 2:
                            break

                        #if the answer is Yes it will do as view_data code chunk which will run going to take start_loc in a range
                        #as index and put the end as start_loc+5 to have 5 rows to be seen by the user.

                        elif view_display == 1:
                            print(df.iloc[start_loc:start_loc+5])
                            start_loc += 5

                            #The continue just to keep the code running in loop until the choice break through choosing no in view_display.

                            continue

                        #I used else to make the view_display in any case to be equal ValueError so that it can go for expect code block.

                        else:
                            view_display= ValueError

                    #In expect block it will consider any input other than 1 or 2 as invalid stating the question again.

                    except ValueError:
                            print("You have entered invalid input, please try again!")


                break

            #Here to break the loop as the user doesn't want to see any rows.

            elif view_data == 2:
                break

            #I used else to consider any other input as ValueError to run in the expect code block.

            else:
                view_data=ValueError

        #I made the expect statement print a message showing that the input is invalid to let the user put a valid one.

        except ValueError :
            print("You have entered invalid input, please try again!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        data_displayer(df)
        restart = input('''\nWould you like to restart?
1: Yes
2: No
\nYour choice:''')
        if restart != '1':
            break

if __name__ == "__main__":
	main()
