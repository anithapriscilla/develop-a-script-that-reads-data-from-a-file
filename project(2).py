import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to analyze data
def analyze_data(file_path):
    df = pd.read_csv("C:\\Users\\ASUS\\Desktop\\data.csv")
    
    # Basic analysis
    summary = df.describe()  # Summary statistics
    total_rows = len(df)
    total_columns = len(df.columns)
    
    return summary, total_rows, total_columns

# Function to generate PDF report
def generate_pdf(report_path, summary, total_rows, total_columns):
    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Automated Data Analysis Report")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Total Rows: {total_rows}")
    c.drawString(100, height - 120, f"Total Columns: {total_columns}")

    c.drawString(100, height - 160, "Summary Statistics:")
    text = c.beginText(100, height - 180)
    text.setFont("Helvetica", 10)

    for line in summary.to_string().split("\n"):
        text.textLine(line)
    
    c.drawText(text)
    c.save()
    print(f"Report saved as: {report_path}")

# Main function
def main():
    input_file = "C:\\Users\\ASUS\\Desktop\\data.csv"  # Change to your CSV file
    output_pdf = "report.pdf"

    summary, total_rows, total_columns = analyze_data(input_file)
    generate_pdf(output_pdf, summary, total_rows, total_columns)

if __name__ == "__main__":
    main()
