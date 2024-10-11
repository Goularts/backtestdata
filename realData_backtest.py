import pandas as pd

df = pd.read_csv('realdataBT.csv', delimiter=';')

df = df.iloc[:,:19]

df['Buy_slippage'] = df['BT_Buy_Price'] - df['Buy_Price']
df['Sell_slippage'] = df['BT_Sell_Price'] - df['Sell_Price']
df['Total_Slippage'] = df['Buy_slippage'] + df['Sell_slippage']
df['finDiff'] = df['BT_Operation_Result'] - df['Operation_Result']

df.to_csv('realdataBT_comp.csv', index=False)

bt = pd.read_csv('backtest_sample.csv', delimiter=';')
bt['Result_ticks_slippage'] = bt['Interval_Result_ticks'] + df['Total_Slippage'].mean()
tick_rate = 0.2
bt['Operation_Result_slippage'] = bt['Result_ticks_slippage'] * tick_rate

backtest_results = {
    'Description': [
        'Average slippage on real operation - buy',
        'Average slippage on real operation - sell',
        'Average slippage on real operation - total',
        'Backtest financial total', 
        'Backtest financial total with average slippage', 
    ],
    'backtest Value': [
        df['Buy_slippage'].mean(),
        df['Sell_slippage'].mean(),
        df['Total_Slippage'].mean(),
        round(bt['Operation_Result'].astype(float).sum(), 2),
        round(bt['Operation_Result_slippage'].astype(float).sum(), 2),
    ]
}

backtest_df = pd.DataFrame(backtest_results)
backtest_df.to_csv('backtest_results.csv', index=False)



