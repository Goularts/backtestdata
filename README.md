# BacktestData

## Project: Trading Latency and Backtest Analysis
This project includes multiple scripts and datasets used to analyze trading latencies, perform backtests, and measure the effects of slippage on real data.

### Overview of Scripts

1. **`backtest_samples.py`**: 
   - Generates samples for a 10-week period for analysis.
   - **Output**: `weeks_sample.csv`

2. **`latency_analysis.py`**:
   - Processes and analyzes latency from log data.
   - **Output**: `latency_results.csv`

3. **`realData_backtest.py`**:
   - Compares real operation data against backtest results.
   - **Outputs**: 
     - Real data with matched operations from backtest: `realdataBT.csv`
     - Backtest 10-week sample: `backtest_sample.csv`
     - Comparison result: `realdataBT_comp.csv`
     - Summary of backtest results: `backtest_results.csv`

### Installation

1. **Clone the repository**:
   ```sh
   git clone <URL_OF_REPOSITORY>
   cd BacktestData
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Generate Backtest Samples**:
   ```sh
   python backtest_samples.py
   ```
   - This script will create a sample CSV (`weeks_sample.csv`) for a 10-week period.

2. **Analyze Latency**:
   ```sh
   python latency_analysis.py
   ```
   - Processes log data to analyze latency and produces `latency_results.csv`.

3. **Compare Real Data and Backtest**:
   ```sh
   python realData_backtest.py
   ```
   - Compares real trading data with backtest data and generates comparison results.

### Outputs
- **`weeks_sample.csv`**: Contains 10 weeks of sampled data for backtesting analysis.
- **`latency_results.csv`**: Provides insights into trading latencies.
- **`realdataBT.csv`**: Data from real operations with matches from the backtest.
- **`realdataBT_comp.csv`**: Detailed comparison between real operations and backtest results.
- **`backtest_results.csv`**: Summary of backtest performance over the sampled period.
