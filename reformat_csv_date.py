import csv
from datetime import datetime

# The path to your input CSV file and output CSV file
input_csv_path = 'data/Provo_Airport_Precipitation.csv'
output_csv_path = 'output.csv'

# Open the input CSV file for reading and the output CSV file for writing
with open(input_csv_path, mode='r', newline='') as infile, open(output_csv_path, mode='w', newline='') as outfile:
    # Create a CSV reader and writer
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames  # Copy fieldnames from input
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write the header to the output file
    writer.writeheader()
    
    # Iterate over each row in the input CSV
    for row in reader:
        # Parse the date from the current format (month/day/year)
        original_date = datetime.strptime(row['DATE'], '%m/%d/%Y')
        
        # Convert the date to the desired format (year/month/day)
        new_date = original_date.strftime('%Y/%m/%d')
        
        # Update the row with the new date format
        row['DATE'] = new_date
        
        # Write the updated row to the output CSV
        writer.writerow(row)