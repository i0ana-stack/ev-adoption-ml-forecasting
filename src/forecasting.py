import pandas as pd
from prophet import Prophet


def prepare_forecast_data(df):
    """Aggregate EV records by model year for forecasting."""

    forecast_df = df.groupby('model_year').size().reset_index()

    forecast_df.columns = ['Year', 'Count']

    forecast_df['ds'] = pd.to_datetime(
        forecast_df['Year'],
        format='%Y'
    )

    forecast_df['y'] = forecast_df['Count']

    return forecast_df[['ds', 'y']]


def generate_forecast(forecast_df, periods=5):
    """Train a Prophet model and generate future forecasts."""

    model = Prophet()

    model.fit(forecast_df)

    future = model.make_future_dataframe(
        periods=periods,
        freq='YE'
    )

    forecast = model.predict(future)

    return model, forecast