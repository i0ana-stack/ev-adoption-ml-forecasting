import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data():
    """Load the EV dataset from the Washington State Open Data API."""
    
    url = "https://data.wa.gov/resource/f6w7-q2d2.csv"
    
    return pd.read_csv(url)


def preprocess_data(df):
    """Select relevant variables, remove missing values and duplicates,
    and encode categorical variables.
    """
    
    df = df[[
        'model_year',
        'make',
        'ev_type',
        'cafv_type',
        'electric_range',
        'county'
    ]]

    df = df.dropna()
    df = df.drop_duplicates()

    le = LabelEncoder()

    df['make'] = le.fit_transform(df['make'])
    df['county'] = le.fit_transform(df['county'])
    df['cafv_type'] = le.fit_transform(df['cafv_type'])
    df['ev_type'] = le.fit_transform(df['ev_type'])

    return df