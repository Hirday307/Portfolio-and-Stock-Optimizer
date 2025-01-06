# Portfolio and Stock Optimizer

Welcome to the **Portfolio and Stock Optimizer**! This project provides tools to analyze, manage, and optimize stock portfolios with various features like historical data visualization, stock performance prediction, elasticity comparison, and transaction management.

## Features

1. **Add a New Stock**:

   - Record details of a newly purchased stock, including date, value, and number of shares.

2. **Buy or Sell Stocks**:

   - Update stock records with new transactions, including shares bought or sold.

3. **View All Records**:

   - View historical transactions and stock details in a tabular format.

4. **Get a Briefing**:

   - Generate insights about a stock's performance, such as ROI, highest and lowest values, and trends.

5. **Compare Elasticity of Two Companies**:

   - Analyze the correlation between two stocks over a user-defined time period to determine their elasticity or cross-elasticity.

6. **Predict Future Performance**:

   - Predict the next day's stock price using Exponential Moving Average (EMA) and visualize moving averages.

7. **Data Visualization**:

   - Generate graphs for stock price trends and comparisons using Matplotlib.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/portfolio-and-stock-optimizer.git
   cd portfolio-and-stock-optimizer
   ```

2. **Install Dependencies**:
   Make sure you have Python installed on your system. Install the required libraries:

   ```bash
   pip install matplotlib pandas yfinance
   ```

3. **Run the Application**:
   Execute the main script:

   ```bash
   python personal_portfolio_optimizer.py
   ```

---

## Usage

1. **Run the Program**:

   ```bash
   python personal_portfolio_optimizer.py
   ```

2. Follow the menu prompts to select options like adding stocks, viewing records, or generating reports.

3. Ensure the stock files are saved in the specified directory: `/stock_history/`.

---

## Project Structure

```
portfolio-and-stock-optimizer/
|── personal_portfolio_optimizer.py   # Main application script
|── stock_history/                   # Directory to store stock JSON files
```

---

## Example Outputs

### Briefing:

- First Exchange Date: 2023-01-01
- Highest Value: $150 (Date: 2023-03-15)
- ROI: 10.5%

### Graphs:

- Stock value trends over time.
- Comparison of two stocks with correlation values.

### Prediction:

- Predicted stock price for the next day using EMA.

---

## Requirements

- Python 3.7+
- Libraries:
  - `matplotlib`
  - `pandas`
  - `yfinance`
  - `json`
  - `datetime`

---

## Future Improvements

- Add support for more advanced machine learning models for stock prediction.
- Implement a GUI for easier user interaction.
- Add support for portfolio diversification recommendations.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

---

## Contributions

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

---

## Author

Developed by **Hirdayjeet Singh Bhandal**.
