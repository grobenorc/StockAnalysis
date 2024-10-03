import yfinance as yf
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

class Company:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    
    def get_financials(self):
        return self.stock.financials

    def get_balance_sheet(self):
        return self.stock.balance_sheet
    
    def get_cashflow(self):
        return self.stock.cashflow
    
    def get_recommendations(self):
        return self.stock.recommendations
    
    def plot_rolling_PE(self):
        # Get the quarterly Basic EPS and convert it to yearly EPS
        BasicEPS_Q = self.stock.quarterly_income_stmt.loc['Basic EPS']
        BasicEPS_Q *= 4  # Quarterly EPS, convert to yearly
        
        # Forward-fill to daily frequency
        BasicEPS_D = BasicEPS_Q.resample('D').ffill().dropna()
        BasicEPS_D.index = BasicEPS_D.index.tz_localize(None)
        
        # Define start and end dates based on EPS data
        StartDateTimeSeries = BasicEPS_D.index.min().strftime('%Y-%m-%d')
        EndDateTimeSeries = date.today().strftime(format='%Y-%m-%d')
        
        # Get the historical stock price for the given date range
        priceDaily = self.stock.history(start=StartDateTimeSeries, end=EndDateTimeSeries)
        priceDaily = priceDaily.resample('D').ffill()['Close']
        priceDaily.index = priceDaily.index.tz_localize(None)
        
        # Combine stock price and EPS data
        comb = pd.concat([priceDaily, BasicEPS_D], axis=1)
        comb.columns = ['Close', 'Basic EPS']
        
        # Calculate the rolling P/E ratio
        comb['PE_Rolling'] = comb.apply(lambda row: row['Close'] / row['Basic EPS'], axis=1)
        
        # Create a figure and axis for plotting
        fig, ax1 = plt.subplots(figsize=(10, 6), dpi=250)
        
        # Plot the stock price and P/E ratio on the primary y-axis
        ax1.plot(comb.index, comb['Close'], label='Stock Price', color='blue')
        ax1.set_ylabel('Stock Price', color='blue')
        
        # Plot the Basic EPS on the secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(comb.index, comb['PE_Rolling'], label='P/E Ratio', color='green')
        ax2.set_ylabel('P/E Ratio', color='green')
        
        # Add vertical lines to indicate earnings report dates
        earnings_dates = self.stock.quarterly_income_stmt.columns
        for edate in earnings_dates:
            if edate >= comb.index.min():
                ax1.axvline(edate, color='red', linestyle='--', lw=1)
        
        # Add title and labels
        ax1.set_title(f"Rolling P/E Ratio and Stock Price for {self.ticker}")
        ax1.set_xlabel('Date')
        
        # Add a legend
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')
        
        # Improve layout and display the plot
        fig.tight_layout()
        plt.show()