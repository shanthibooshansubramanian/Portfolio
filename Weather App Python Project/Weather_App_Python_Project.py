#  import all the required packages for your program
import requests
import re
import ast
import json


api_key = '3bd0b7e1dfb61496bf609b3a1109361a'    # API Key for the weather app

def weatherFromZip(zipcode):                    # Method for looking up weather through zipcode

    zip = (zipcode.strip(''))
    # Build the url with Zip code and country - US
    url = 'http://api.openweathermap.org/geo/1.0/zip?zip='+zip+'&appid='+api_key

    try:                                        # Try-Except block to catch exceptions on API Request
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            coord_zip = json.loads(response.text)
            latitude = coord_zip['lat']
            longitude = coord_zip['lon']
            weather_data(latitude, longitude)
    except requests.exceptions.InvalidURL:
        print('InvalidURL:There is technical issue with the URL. Please contact the developer.')

    except requests.exceptions.URLRequired:
        print('URLRequired: There is technical issue with the URL. Please contact the developer.')
    except requests.exceptions.ConnectionError:
        print('Connection Error: There is an issue with the connection. Please try again later.')
    except requests.exceptions.RequestException:
        if response is None:
            print('\nThe request could not be served. Please try again later.')
        else:
            content = ast.literal_eval(response.content.decode('UTF-8'))
            print('\nYour request has failed. Reason --> ' + content["message"])
    except:
        print('\nSomething is broken. Please try again later.')

def weatherFromCity(cityname, statecode):   # Method for looking up weather through City name and State code

    cn = cityname.strip()
    sc = (statecode.strip('')).rstrip('.')
    # Build the url with city name, state code and country - US
    url = 'http://api.openweathermap.org/geo/1.0/direct?q='+cn+'%2C'+sc+'%2C'+'US&appid='+api_key

    try:                                    # Try-Except block to catch exceptions on API Request
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            coord_city = json.loads(response.text)
            latitude = coord_city[0]['lat']
            longitude = coord_city[0]['lon']
            weather_data(latitude, longitude)
    except requests.exceptions.InvalidURL:
        print('InvalidURL:There is technical issue with the URL. Please contact the developer.')
    except requests.exceptions.URLRequired:
        print('URLRequired: There is technical issue with the URL. Please contact the developer.')
    except requests.exceptions.ConnectionError:
        print('Connection Error: There is an issue with the connection. Please try again later.')
    except requests.exceptions.RequestException as e:
        if response is None:
            print('\nThe request could not be served. Please try again later.')
        else:
            content = ast.literal_eval(response.content.decode('UTF-8'))
            print('\nYour request has failed. Reason --> ' + content["message"])
    except:
        print('\nSomething is broken. Please try again later.')


def weather_data(latitude, longitude):
    latitude = latitude
    longitude = longitude
    url_weather = 'https://api.openweathermap.org/data/2.5/weather'
    url = {'lat': latitude, 'lon': longitude, 'appid': api_key}
    response = requests.get(url_weather, params=url)
    response.raise_for_status()
    tempconversion(response.json())     # calling the tempconversion() method to format the results

def tempconversion(jsonresponse):           # Method for formatting the results, convert temp to F, C. The default response is in Kelvin
    innerdict = jsonresponse['main']
    current_k = innerdict['temp']
    min_k = innerdict['temp_min']
    max_k = innerdict['temp_max']
    pressure = innerdict['pressure']
    humidity = innerdict['humidity']
    cloud = ((jsonresponse['weather'])[0])['description']
    city = jsonresponse['name']
    country = (jsonresponse['sys'])['country']

    degree = input('\nEnter F for Fahrenheit, C for Celsius, K for Kelvin: ').upper()
    while True:
        if degree not in ['C','F','K']:
            degree = input('\nPlease provide a valid degree - F, C, K, or Q to quit: ').upper()

        if degree == 'F':
            convert_current = round((float(current_k) - 273.15) * (9/5) + 32,2)
            convert_min = round((float(min_k) - 273.15) * (9/5) + 32,2)
            convert_max = round((float(max_k) - 273.15) * (9/5) + 32,2)
            break
        elif degree == 'C':
            convert_current = round((float(current_k) - 273.15),2)
            convert_min = round((float(min_k) - 273.15),2)
            convert_max = round((float(max_k) - 273.15),2)
            break
        elif degree == 'K':
            convert_current = round(float(current_k),2)
            convert_min = round(float(min_k),2)
            convert_max = round(float(max_k),2)
            break
        elif degree == 'Q':
            return
    # dictionary of all the details required for final print
    print_list = {'degree': degree, 'temp': convert_current, 'min': convert_min, 'max': convert_max, 'pressure': pressure, 'humidity': humidity, 'cloud': cloud, 'city': city, 'country': country}
    pretty_print(print_list)            # Final print method


def pretty_print(print_list):           # Final print method for printing all the weather details for user

    degree_sign = u"\N{DEGREE SIGN}"    # set the degree sign
    print('\n')
    print('*' * 60)
    print('Current Weather Conditions in',print_list['degree']+degree_sign)
    print('City - ', print_list['city']+', '+print_list['country'])


    print('Current Temperature', str(print_list['temp'])+degree_sign)
    print(f'Low Temperature', str(print_list['min'])+degree_sign)
    print(f'High Temperature', str(print_list['max'])+degree_sign)
    print(f'Pressure', str(print_list['pressure'])+' hPa')
    print(f'Humidity', str(print_list['humidity'])+'%')
    print(f'Cloud Cover', print_list['cloud'])

    print('*' * 60)

def main():
    print('*'*60)
    print('\nWelcome to \'Whether the Weather\' app!')      # Welcome
    while True:
        try:                        # User to choose lookup via zip code or city name
            userchoice = int(input("\nHow is the weather? Please select one of the following to know more?  \n"
                                   "Enter 1 to lookup by Zip Code\n"
                                   "Enter 2 to lookup by City\n"
                                   "Enter 3 to Exit\n"))
            if userchoice == 1:
                while True:
                    zip = input('\nPlease enter a valid Zip Code or type Q to go to Menu: ').upper()
                    if zip == 'Q':
                        break
                    else:
                        zip_pattern = re.compile('^[0-9]{5}(?:-[0-9]{4})?$')    # regex to validate zip code is in valid format
                        matching = zip_pattern.match(zip.strip())
                        if matching:
                            weatherFromZip(zip)                                 # calling weatherFromZip method
                        else:
                            print('\nInvalid Zip Code. Try Again.')
            elif userchoice == 2:
                while True:
                    cityname = input('\nPlease enter a valid City Name or type Q to go to Menu: ').upper()
                    if cityname == 'Q':
                        break
                    else:
                        statecode = input('Please enter the State Code: ').upper()
                        weatherFromCity(cityname, statecode)                    # calling weatherFromCity method
            elif userchoice == 3:
                break
            else:
                print('\nInvalid Response. Please select from the options provided! ')
        except:
            print('\nInvalid Response. Please select from the options provided!')

    print('\nThank you for using our \'Whether the Weather\' app!')             # Thank you.


if __name__ == "__main__":                                                      # calling main
     main()
