# backtestdata
Project: Trading Latency and Backtest Analysis
Multiple scripts and datasets used to analyze trading latencies, perform backtests, and measure the effects of slippage on real data.

1. backtest_samples.py
Generates the samples of 10 weeks for analysis.
Output: weeks_sample.csv

2. latency_analysis.py
Processes and analyzes latency from log data.
Output: latency_results.csv

3. realData_backtest.py
Compares real operation data against backtest results.
Real data with match operations from backtest - realdataBT.csv
Backtest 10 weeks sample — backtest_sample.csv.
Output:
realdataBT_comp.csv.
backtest_results.csv.
