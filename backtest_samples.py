import pandas as pd
import numpy as np
import holidays
from datetime import datetime, timedelta
import random

def weekSamples(years_period=2, n_samples=10):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years_period * 365)

    brazil_holidays = holidays.Brazil()
    weekdays = pd.bdate_range(start=start_date, end=end_date)
    weekdays = [day for day in weekdays if day not in brazil_holidays]

    df_weekdays = pd.DataFrame(weekdays, columns=['date'])
    df_weekdays['year'] = df_weekdays['date'].dt.year
    df_weekdays['week'] = df_weekdays['date'].dt.isocalendar().week
    df_weekdays['weekday'] = df_weekdays['date'].dt.weekday

    df_weekdays = df_weekdays[df_weekdays['weekday'] < 5]
    unique_weeks = df_weekdays[['year', 'week']].drop_duplicates().reset_index(drop=True)
    unique_weeks = unique_weeks.sample(frac=1, random_state=random.randint(0, 10000)).reset_index(drop=True)
    sampled_weeks = unique_weeks.sample(n=n_samples, random_state=random.randint(0, 10000))
    sampled_weekdays = df_weekdays.merge(sampled_weeks, on=['year', 'week'])
    sampled_weekdays['week_id'] = sampled_weekdays['year'].astype(str) + '_W' + sampled_weekdays['week'].astype(str)
    return sampled_weekdays[['date', 'week_id']]

samples = weekSamples(n_samples=10)
# samples.to_csv('weeks_sample.csv', index=False)
