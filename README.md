# BikeShare Database Analysis
Project Creation Date: 2021/07/18;
Project Last Updated: 2021/08/21

## Project Purpose

The purpose of this project is to provide an interactive means of analysing data provided for the bikeshare services in three different cities, Chicago, New York City and Washington.

I hope you enjoy this application!!

## How to Use The Application

This section will detail how to correctly set-up the application to function, how to run the application and finally how to interact with the application.

### Setup

First of all you will need to ensure that you have the correct files on your local machine.

- Copy the three `.csv` files onto a new folder on your local machine (see "**Files Required**" section below)
- Copy the `'BikeShare Project.py'` application into the **same** folder as the .csv files.

### Running the Application
The application can be launched by simply double-clicking it within the folder. If this does not work the below steps can be followed.

The application can be activated from a terminal window (command prompt, bash, whichever you prefer).

- Using the terminal window of your choice, brows to the folder containing the `.csv` and `.py` files that you copied `$ cd <folder directory>`.
- Run the `.py` application with the following command: `$ python 'BikeShare Project.py'` (note the quotations).

If all the above stapes are followed correctly the application will launch within the terminal window and will start by prompting question to the user.

### Interacting with the Application

Interactive prompt's will be displayed constantly, read carefully and respond to whatever is asked. The application is not case sensitive therefore it would not matter whether upper or lower case is used to respond.

If an incorrect input is given, the application will inform the user and will prompt the user to try again. The message will also display available options.

>You have entered an invalid city, please try again.
>
>Available options are: "Chicago, "New York City" or "Washington"
>
>Please enter the city name for which to filter (Chicago, New York City or Washington)

At any point in time if you would like to exit the application and return to the normal terminal you can simply type `exit` and the application will stop. The following message will be displayed:
> Program terminated.

## Analyses Performed on Data

The application will first require the user to select one of the 3 possible cities (Chicago, New York City or Washington) in order to filter the data. Once the user has selected a city the application will continue to prompt the user for further inputs to add additional filters. These filters will be for the following:
- Filter data for a specific month or for all months.
- Filter data for a specific day or for all days.

After selecting any of the filters the application will confirm the user's input and will ask if it is correct, answering `N` will take the user back to that particular step for the user to enter a different option.

Once all filter inputs has been completed the application will display the chosen filters for the data set.

>This model will display data under the following conditions:
>
>Data will be show for Washington
>
>For all months
>
>Filtered to all days

Once the application has gathered all the required filters the application will ask the user if the user would like to preview some of the raw data before showing the results. If the user inputs `Y` to this prompt the application will display the first 5 lines of raw data in the data set. The user then has the option to display the next 5 lines or to continue to the calculated output of the application.

The following information will be calculated:
- Most frequent month for which service is used is.
  - Only if all months was selected in the filter
- Most frequent day for which service is used is.
  - Only if all days were selected in the filter.
- Most Frequent Riding Hour.
- Total number of rides during this time.
- The most popular start station and the number of times used.
- The most popular end station and the number of times used.
- The most popular route and the number of trips for that route.
- Average travel time is in minutes.
- Total travel time is in days.
- Summary of users by type of users.
- Summary of users by gender.


- The following three statistics is not available for Washington and will therefore not be displayed if Washington is selected during the filtering process.
  - Earliest birth year (oldest user) in data set.
  - Most recent birth year (youngest user) in data set.
  - Most common birth year in data set.

After displaying the calculated output the application will prompt the user to try again, if `Y` the application will start from the beginning, else the application will be stopped and will return the user to his normal terminal window.

## Files Required

- .csv files
  - chigago.csv
  - new_york_city.csv
  - washington.csv
- BikeShare Project.py

## Known Bugs

All current known bugs will result in the application crashing and returning the user to the normal terminal window. Below is a list of known bugs and whether they have been attended to.

- Spelling error in calculated output
  - tripes instead of trips.
- Application crashes when incorrect input is given on final prompt to restart the application.
- Application does not clear the terminal window when launched.
- No exception handling for incorrect input at prompt for next 5 rows.

## Credits

Credit for the creation of this application must be given to Udacity for supplying the relevant raw data and knowledge in order for me to have created this application.
