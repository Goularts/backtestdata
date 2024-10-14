import os
import pandas as pd
import glob
import sys
from pathlib import Path

df = pd.read_parquet(r"latency.parquet")

df['log_info'] = df['log_info'].apply(lambda x: 'Order Done' if 'Order' in x else x)

pivot_df = df.drop(columns=['log']).pivot_table(
    index=['arquivo_origem', 'client_info', 'tradetime', 'date', 'grupo'],
    columns='log_info',
    values='latency_info',
    aggfunc='first'
).reset_index()

pivot_df.to_parquet('latency_agg.parquet')

datetime_columns = ['tradetime', 'First Received', 'Algo analysis', 'Algo analysis Done', 'Order Done','Zeroing Check', 'Zeroing Check Done']
for col in datetime_columns:
    pivot_df[col] = pd.to_datetime(pivot_df[col], errors='coerce')
datetime_columns.pop(0)

# ------- Price data received latency
pivot_df['price_latency'] = pivot_df['First Received'] - pivot_df['tradetime']
tradeTime_ReceivedAlgo = pivot_df[pivot_df['First Received'].notnull() & pivot_df['tradetime'].notnull()]['price_latency'].mean()

# ------- Full process max latency
pivot_df['max_timestamp'] = pivot_df[datetime_columns].max(axis=1) 
pivot_df['full_process'] = pivot_df['max_timestamp'] - pivot_df['tradetime']
tradeTime_FullProcess = pivot_df[pivot_df['max_timestamp'].notnull() & pivot_df['tradetime'].notnull()]['full_process'].mean()

# ------- Full algo process with order latency (from price receiving)
tradeTime_FullProcessOrderDone = pivot_df[pivot_df['Order Done'].notnull() & pivot_df['tradetime'].notnull()]['full_process'].mean()

# ------- Only algo process with order latency
pivot_df['min_timestamp'] = pivot_df[datetime_columns].min(axis=1) 
pivot_df['algo_latency'] = pivot_df['max_timestamp'] - pivot_df['min_timestamp']
algoProcessing = pivot_df[pivot_df['tradetime'].notnull()]['algo_latency'].mean()
algoProcessingOrderDone = pivot_df[pivot_df['Order Done'].notnull() & pivot_df['tradetime'].notnull()]['algo_latency'].mean()

latency_results = {
    'Description': [
        'Average latency between real time price and first received to algo analysis', 
        'Average latency between real time price and full algo processing', 
        'Average latency between real time price and full algo processing (with order only)', 
        'Average latency full algo processing',        
        'Average latency full algo processing (with order only)',
        'There is no latency between sending the order fullfilling it',
    ],
    'Latency Value': [
        tradeTime_ReceivedAlgo,
        tradeTime_FullProcess,
        tradeTime_FullProcessOrderDone,
        algoProcessing,
        algoProcessingOrderDone,
        0.0,
    ]
}

latency_df = pd.DataFrame(latency_results)
latency_df.to_csv('latency_results.csv', index=False)