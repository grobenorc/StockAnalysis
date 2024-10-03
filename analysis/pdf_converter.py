# analysis/pdf_converter.py
import os
import subprocess

class PDFConverter:
    def convert_to_pdf(self, notebook_path):
        # Use the full path to the Jupyter executable from Anaconda
        jupyter_path = r"C:\Users\claes\anaconda3\Scripts\jupyter.exe"
        
        # Extract the output directory
        output_dir = os.path.join('reports')  # Define the output directory

        # Construct the command to convert the notebook to PDF using webpdf
        command = [jupyter_path, 'nbconvert', '--to', 'webpdf', '--execute', notebook_path, '--output-dir', output_dir]
        
        print(f"Running command: {' '.join(command)}")  # Debug statement
        
        try:
            # Run the command using subprocess
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            print(result.stdout)  # Print standard output
            print(result.stderr)  # Print any error messages

            # Extract the file name without the extension and change the output directory
            pdf_file = os.path.join(output_dir, os.path.basename(notebook_path).replace('.ipynb', '.pdf'))

            # Ensure the directory exists
            os.makedirs(output_dir, exist_ok=True)

            print(f"PDF saved as {pdf_file}")

        except subprocess.CalledProcessError as e:
            print("Error: Failed to convert notebook to PDF.")
            print(f"Return code: {e.returncode}")
            print(f"Output: {e.output}")
            print(f"Error output: {e.stderr}")


