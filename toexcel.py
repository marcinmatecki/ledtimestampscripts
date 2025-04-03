import csv
import pandas as pd

def process_csv(file_name):
    """Reads a CSV file and stores the data in a list of rows."""
    rows = []

    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        for row in reader:
            if len(row) < 3:
                continue  # Skip malformed rows
            
            # Convert 'image' and 'Decoded Gray Value' columns to integers
            try:
                row[0] = int(row[0])  # Convert image to integer
                row[2] = int(row[2])  # Convert Decoded Gray Value to integer
            except ValueError:
                continue  # If conversion fails, skip this row
            
            rows.append(row)  # Add row to list

    return rows

def save_to_excel(data, output_file):
    """Saves the data to an Excel file."""
    # Convert the list of rows into a pandas DataFrame
    df = pd.DataFrame(data, columns=["image", "binary_value", "Decoded Gray Value"])
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

def main():
    input_file = 'sorted_nowecleaned_processed_cleaned_result1.csv'  # Replace with your actual CSV file name
    output_file = 'output_file.xlsx'  # Name for the Excel file to be saved

    # Process the CSV file
    data = process_csv(input_file)

    # Save the data to an Excel file
    save_to_excel(data, output_file)
    print(f"Data has been successfully saved to {output_file}")

if __name__ == "__main__":
    main()