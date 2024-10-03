# main.py
from analysis.company import Company
from analysis.notebook_generator import NotebookGenerator
from analysis.pdf_converter import PDFConverter

def main():
    ticker = input("Enter the company ticker symbol: ").upper()

    # Instantiate the Company object
    company = Company(ticker)

    # Generate the notebook
    notebook_generator = NotebookGenerator(company)
    notebook_path = notebook_generator.create_notebook()

    # Convert the notebook to PDF
    pdf_converter = PDFConverter()
    pdf_converter.convert_to_pdf(notebook_path)

    print(f"Company analysis for {ticker} saved as PDF!")

if __name__ == "__main__":
    main()
