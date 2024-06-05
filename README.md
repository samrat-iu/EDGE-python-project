# Weather App

This is a simple weather application built with Python that shows the current weather for any city. It uses the OpenWeatherMap API to get weather data and displays it in a window using `tkinter`.

## Features

- Get current weather information for any city.
- Shows city name, temperature, and weather description.
- Handles errors for network issues and incorrect city names.

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.x
- `requests` library

You also need an API key from OpenWeatherMap.

## Installation

1. **Clone the Repository**

    First, download or clone this repository to your local machine:

    ```bash
    git clone https://github.com/<your-username>/weather_app.git
    cd weather_app
    ```

2. **Install the Requests Library**

    If you don't have the `requests` library, install it using pip:

    ```bash
    pip install requests
    ```

3. **Add Your API Key**

    Open the `weather_app.py` file and replace `'30d4741c779ba94c470ca1f63045390a'` with your own OpenWeatherMap API key.

## How to Use

Run the `weather_app.py` script to start the application:

```bash
python weather_app.py
