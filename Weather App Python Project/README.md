
# Weather App Python Project

## Project Overview

This Python project utilizes the OpenWeatherMap API to provide current weather information based on user input. It supports weather lookup by Zip Code or City Name and State Code combination. The application also allows users to choose temperature units (Fahrenheit, Celsius, or Kelvin) for displaying weather details.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Model Training and Evaluation](#model-training-and-evaluation)
7. [Results](#results)
8. [Future Work](#future-work)
9. [Contributing](#contributing)
10. [Acknowledgments](#acknowledgments)


## Installation

To run this project, you need to have Python installed. It's recommended to use Anaconda Python for managing the environment and dependencies easily.

1. Install [Anaconda](https://www.anaconda.com/products/individual).
2. Create a new environment:
    ```sh
    conda create -n weather-app python=3.8
    conda activate weather-app
    ```
3. Install the required packages:
    ```sh
    pip install requests
    ```
##  Usage

To use the Weather App:

1. Run the application:
2. Choose from the following options:
    - Enter 1 to lookup weather by Zip Code.
    - Enter 2 to lookup weather by City Name and State Code.
    - Enter 3 to exit the application.
3. Follow the prompts to enter the required information (Zip Code, City Name, State Code).
4. Select temperature units (F, C, K) when prompted to view weather details in Fahrenheit, Celsius, or Kelvin.
5. The application will display current weather conditions including temperature, pressure, humidity, cloud cover, and more.

## Data

The weather data is fetched from the OpenWeatherMap API. It includes real-time information such as temperature, pressure, humidity, and cloud cover for the specified location.

## Source Data

API Key: Replace `<api_key>` in the `weather_app.py` file with your OpenWeatherMap API key. Obtain your API key by signing up at [OpenWeatherMap API](https://openweathermap.org/api).

## Model Training and Evaluation

The project does not involve machine learning model training or evaluation. It focuses on integrating with an external weather API and displaying data.

## Results

The application provides accurate and up-to-date weather information based on user input. It supports multiple units for temperature conversion and displays comprehensive weather details.
- Current temperature in Fahrenheit, Celsius, or Kelvin
- Minimum and maximum temperatures
- Pressure
- Humidity
- Cloud cover description
- City and country name

## Future Work

Future enhancements may include:
- Adding support for more weather parameters.
- Implementing user authentication for API access.
- Enhancing error handling and user input validation.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## Acknowledgments

This code was developed as part of learning by Shanthibooshan Subramanian. If you plan to use it, please provide appropriate citations to the dataset and other pages you might have referred to for your learning process.

Special thanks to the following resources:
- [Python](https://www.python.org/)
- [Analytical Vidhya](https://www.analyticsvidhya.com/)
- [OpenWeatherMap](https://openweathermap.org/)
