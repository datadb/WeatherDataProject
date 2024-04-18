import pandas as pd
from datetime import datetime
import requests

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://raw.githubusercontent.com/datadb/WeatherDataProject/main/data/GlobalLandTemperaturesByCountry.csv'
    
    weather_dtypes = {
        'AverageTemperature': float,
        'AverageTemperatureUncertainty': float,
        'Country': str
    }

    parse_dates = ['dt']
    
    df = pd.read_csv(url, sep=',', dtype=weather_dtypes, parse_dates=parse_dates)
    
    # # Convert 'dt' column to datetime and then to string format with just the date
    # df['dt'] = pd.to_datetime(df['dt'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
    
    # # Convert the string format back to datetime
    # df['dt'] = pd.to_datetime(df['dt'], format='%Y-%m-%d')
    # print (df.dtypes)
    return df

#  print (df.dtypes)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

