import csv

def process_csv(file_name):
    """Reads a CSV file, sorts rows by the first column, reorders columns, and writes results to a new file."""
    output_file = "sorted_" + file_name
    
    with open(file_name, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        rows = list(reader)
        
        # Extract header and data separately
        header = rows[0]
        data = rows[1:]
        
        # Sort data rows based on the first column (numerical order)
        data.sort(key=lambda row: int(row[0]))  # Sort rows based on the first column
        
        # Write header to the new file
        writer.writerow(header)
        
        # Reorder columns and write sorted data to the new file
        for row in data:
            if len(row) < 3:
                continue  # Skip malformed rows
            
            # Reorder columns: move the third column to the first place
            reordered_row = [row[0], row[1], row[2]]
            writer.writerow(reordered_row)

def main():
    process_csv('nowecleaned_processed_cleaned_result1.csv')  # Replace with your actual CSV file name

if __name__ == "__main__":
    main()