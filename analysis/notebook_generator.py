# # analysis/notebook_generator.py
# import os
# import nbformat as nbf

# class NotebookGenerator:
#     def __init__(self, company):
#         self.company = company
    
#     def create_notebook(self):
#         ticker = self.company.ticker
#         nb = nbf.v4.new_notebook()

#         # Add the title
#         nb.cells.append(nbf.v4.new_markdown_cell(f"# Company Analysis: {ticker}"))

#         # Stock Price Section
#         nb.cells.append(nbf.v4.new_markdown_cell('## Stock Price and Rolling P/E Ratio'))
        
#         # Add the code cell to call the plot function
#         nb.cells.append(nbf.v4.new_code_cell(f"""
#         # Plot the rolling P/E ratio and stock price for {ticker}
#         {self.company.plot_rolling_PE()}
#                 """))
        
#         # Profitability Section
#         nb.cells.append(nbf.v4.new_markdown_cell("## 1. Profitability"))
#         nb.cells.append(nbf.v4.new_code_cell(f"""
#             financials = {self.company.get_financials()}
#             financials.loc[['Gross Profit', 'Operating Income', 'Net Income']]
#         """))

#         # Financial Position Section
#         nb.cells.append(nbf.v4.new_markdown_cell("## 2. Financial Position"))
#         nb.cells.append(nbf.v4.new_code_cell(f"""
#             balance_sheet = {self.company.get_balance_sheet()}
#             balance_sheet
#         """))

#         # Cash Flow Section
#         nb.cells.append(nbf.v4.new_markdown_cell("## 3. Cash Flow Analysis"))
#         nb.cells.append(nbf.v4.new_code_cell(f"""
#             cashflow = {self.company.get_cashflow()}
#             cashflow
#         """))

#         # Market Sentiment Section
#         nb.cells.append(nbf.v4.new_markdown_cell("## 4. Market Sentiment"))
#         nb.cells.append(nbf.v4.new_code_cell(f"""
#             recommendations = {self.company.get_recommendations()}
#             recommendations.tail(10)
#         """))

#         # Save the notebook using os.path.join
#         notebook_path = os.path.join("analysis_notebooks", f"company_analysis_{ticker}.ipynb")
#         with open(notebook_path, 'w') as f:
#             nbf.write(nb, f)
#         return notebook_path




import os
import nbformat as nbf

class NotebookGenerator:
    def __init__(self, company):
        self.company = company
    
    def create_notebook(self):
        ticker = self.company.ticker
        nb = nbf.v4.new_notebook()

        # Add the title
        nb.cells.append(nbf.v4.new_markdown_cell(f"# Company Analysis: {ticker}"))

        # Define the `company` object at the start of the notebook, including sys.path modification
        notebook_dir = os.path.abspath(os.path.join(os.getcwd(), "analysis"))
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Modify the system path to include the 'analysis' directory
import sys
sys.path.append(r"{notebook_dir}")

# Define the Company object for {ticker}
from company import Company
company = Company("{ticker}")
        """))

        # Stock Price and Rolling P/E Ratio Section
        nb.cells.append(nbf.v4.new_markdown_cell('## Stock Price and Rolling P/E Ratio'))
        
        # Add the code cell to call the plot function
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Plot the rolling P/E ratio and stock price for {ticker}
company.plot_rolling_PE()
        """))

        # Profitability Section
        nb.cells.append(nbf.v4.new_markdown_cell("## 1. Profitability"))
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Display key profitability metrics for {ticker}
financials = company.get_financials()
financials.loc[['Gross Profit', 'Operating Income', 'Net Income']]
        """))

        # Financial Position Section
        nb.cells.append(nbf.v4.new_markdown_cell("## 2. Financial Position"))
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Display the balance sheet for {ticker}
balance_sheet = company.get_balance_sheet()
balance_sheet
        """))

        # Cash Flow Section
        nb.cells.append(nbf.v4.new_markdown_cell("## 3. Cash Flow Analysis"))
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Display the cash flow statement for {ticker}
cashflow = company.get_cashflow()
cashflow
        """))

        # Market Sentiment Section
        nb.cells.append(nbf.v4.new_markdown_cell("## 4. Market Sentiment"))
        nb.cells.append(nbf.v4.new_code_cell(f"""
# Display the latest market sentiment (analyst recommendations) for {ticker}
recommendations = company.get_recommendations()
recommendations.tail(10)
        """))

        # Save the notebook
        notebook_path = os.path.join("analysis_notebooks", f"company_analysis_{ticker}.ipynb")
        with open(notebook_path, 'w') as f:
            nbf.write(nb, f)
        return notebook_path


