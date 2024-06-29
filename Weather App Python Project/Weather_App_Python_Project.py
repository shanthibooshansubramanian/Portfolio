import requests
import json
import time
import tabulate


from tabulate import tabulate

print('Welcome to Weather Now! Access current weather data for over 200,000 cities.\n'
      "\nFor a precise forecast, please enter the 5 digit U.S. Zip Code for you location \n"
      "or the city's name, comma, and 2-letter country code, as highlighted below.\n"
      'Selections made without a country code may return inaccurate results / cities.\n'
      "Examples...London, GB / New York, US / Madrid, ES...Let's Begin!\n")


def main():
    """Main function for the program, allows user to input a zip code or city to receive Latitude and Longitude coordinates"""
    url_coord = 'http://api.openweathermap.org/geo/1.0/zip'
    url_coord01 = 'http://api.openweathermap.org/geo/1.0/direct'
    option = input("\nHow is the weather? Please select one of the following to know more?\n"
                     "Enter 1  to lookup by US City and US State\n"
                      "Enter 2 to lookup by Zip Code\n").strip()
    while not (option == '1' or option == '2'):
        option = input("You did not enter a valid selection, 1 or 2 are options.\n"
                           "Please enter 1 or 2 to continue \n").strip()
    if option == '1':
        locationcity = str(input('Please enter US City:')).lower().strip()
        locationstate = str(input('Please enter US State:')).lower().strip()
        url_coord = url_coord01
        location = locationcity + ',' + locationstate + ',US'
    else:
        location = input('Please enter Zipcode:').strip()
    option_1 = str(
        input('Please enter like to view temps in F - Fahrenheit, C- Celsius, or K - Kelvin:')).upper().strip()
    while not (option_1 == 'F' or option_1 == 'C' or option_1 == 'K'):
        option_1 = str(input('You did not enter a valid selection, Please enter the valid value.\n'
                             'F, C or K ')).upper().strip()

    while True:
        try:
            coordinates(location, url_coord, option_1)
            print('')
            more_weather()
            break
        except LookupError:
            print('')
            more_weather()
            break


def coordinates(location, url_coord, option_1):
    """Makes a GET request to the url for current weather, verifies connection is made, parses and displays the data"""
    if location.isdigit() is True:
        query_params = {'zip': location, 'APPID': 'e0658f792164bea0f30488a83ec7f9c9'}
    else:
        query_params = {'q': location, 'APPID': 'e0658f792164bea0f30488a83ec7f9c9'}
    response = requests.get(url_coord, params=query_params, timeout=(5, 14))
    try_web(response, location)
    if response.status_code == 200:
        coord_parsed = json.loads(response.text)
        if location.isdigit() is True:
            latitude = coord_parsed['lat']
            longitude = coord_parsed['lon']
        else:
            latitude = coord_parsed[0]['lat']
            longitude = coord_parsed[0]['lon']
        url_weather = 'https://api.openweathermap.org/data/2.5/weather'
        weather_current(latitude, longitude, url_weather, option_1)


def weather_current(latitude, longitude, url_weather, option_1):
    """Makes a GET request to the url for current weather, verifies connection is made, parses and displays the data"""
    query_params = {'lat': latitude, 'lon': longitude, 'APPID': 'e0658f792164bea0f30488a83ec7f9c9'}
    response = requests.get(url_weather, params=query_params, timeout=(5, 14))
    #if response.status_code == 200:
        #print('Connected weather details found')
    current_parsed = json.loads(response.text)
    current_formatted(current_parsed, option_1)


def convert_temp(temp, option_1):
    """Converts Kelvin temperatures to Fahrenheit and Celsius"""
    if option_1 == 'F':
        f_degree = round((((temp - 273.15) * 9) / 5) + 32)
        return f'{f_degree}{chr(176)}F'
    elif option_1 == 'C':
        c_degree = round(temp - 273.15)
        return f'{c_degree}{chr(176)}C'
    else:
        return f'{temp}{chr(176)}K'


def try_web(response, location):
    """Try Except block to test the request was successful, additionally checking if the city or
    zip code entered is valid by using 404 status code"""
    try:
        response.raise_for_status()
        if response.status_code == 404 or len(json.loads(response.text)) == 0:
            if location.isdigit() is True:
                print(f"The zip code entered '{location}' was not found or is not valid.")
            else:
                if location.__contains__(','):
                    print(f"The city and state entered was not found.")
                else:
                    print(f"The city and state entered  was not found.")
        else:
            #print('Even we do not have access to single digit zip codes.')
            print('Successfully fetched Weather Records.')
    except requests.ConnectionError as error1:
        print('Error Connecting')
        print(error1)
    except requests.Timeout as error2:
        print('Timeout Error')
        print(error2)
    except requests.RequestException as error3:
        print('Something Else Went Wrong')
        #print(error3)


def current_formatted(parsed, option_1):
    """Decodes the JSON data, formats the time variables to match proper time zones, then formats the printable
    output of the current weather"""
    city = str(json.dumps(parsed['name'])).replace('"', '')
    country = str(json.dumps(parsed['sys']['country'])).replace('"', '')
    timezone = int(json.dumps(parsed['timezone']))
    epoch_time = int(json.dumps(parsed['dt']))
    true_time = epoch_time + timezone
    current_time = time.strftime("%A, %b %d, %Y %I:%M %p (local time)", time.gmtime(true_time))
    temp = float(json.dumps(parsed['main']['temp']))
    temp_min = float(json.dumps(parsed['main']['temp_min']))
    temp_max = float(json.dumps(parsed['main']['temp_max']))
    pressure = float(json.dumps(parsed['main']['pressure']))
    humidity = int(json.dumps(parsed['main']['humidity']))
    conditions = str(json.dumps(parsed['weather'][0]['description'])).replace('"', '').title()
    print(f'Weather Report for {city}, {country} on {current_time}:\n')
    # make a list of lists to print in a tabular form
    table = [['Current Temperature',convert_temp(temp, option_1)],
             ['Minimum Temperature',convert_temp(temp_min, option_1)],
             ['maximum Temperature',convert_temp(temp_max, option_1)],
             ['pressure:',str(pressure)+'hPa'],
             ['Humidity:',str(humidity)+'%'],
             ['Current Conditions:',conditions]
            ]
    print(tabulate(table, tablefmt= 'fancy_grid'))  # output in a table format

def more_weather():
    """Allows the user to look up another location or exit the program"""
    option = str(input('Would you like to enter another location, Yes or No? ')).lower().strip()
    # while loop for a yes selection or to exit the program (and to catch input errors)
    while not (option == 'yes' or option == 'no'):
        option = str(input('You did not enter a valid selection.\n'
                           'Please enter Yes to search another location or No to exit: ')).lower().strip()
    if option == 'yes':
        print('')
        main()
    if option == 'no':
        print('Thank you for using our service. Goodbye')


main()
