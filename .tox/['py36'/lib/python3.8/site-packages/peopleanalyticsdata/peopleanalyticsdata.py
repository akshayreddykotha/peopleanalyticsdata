import pkg_resources
import pandas as pd

def charity_donation():
    """Return a dataframe about the charity donation.

    Contains the following fields:
         #   Column           Non-Null Count  Dtype 
        ---  ------           --------------  ----- 
         0   n_donations      354 non-null    int64 
         1   total_donations  354 non-null    int64 
         2   time_donating    354 non-null    int64 
         3   recent_donation  354 non-null    int64 
         4   last_donation    354 non-null    int64 
         5   gender           354 non-null    object
         6   reside           354 non-null    object
         7   age              354 non-null    int64 

    """
    stream = pkg_resources.resource_stream(__name__, 'data/charity_donation.csv')
    return pd.read_csv(stream)

def employee_survey():
    """Return a dataframe about the employee survey.

    Contains the following fields:
         #   Column     Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   Happiness  2833 non-null   int64
         1   Ben1       2833 non-null   int64
         2   Ben2       2833 non-null   int64
         3   Ben3       2833 non-null   int64
         4   Work1      2833 non-null   int64
         5   Work2      2833 non-null   int64
         6   Work3      2833 non-null   int64
         7   Man1       2833 non-null   int64
         8   Man2       2833 non-null   int64
         9   Man3       2833 non-null   int64
         10  Car1       2833 non-null   int64
         11  Car2       2833 non-null   int64
         12  Car3       2833 non-null   int64
         13  Car4       2833 non-null   int64

    """
    stream = pkg_resources.resource_stream(__name__, 'data/employee_survey.csv')
    return pd.read_csv(stream)
