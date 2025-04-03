import csv
import re

def clean_filename(filename):
    """Removes the prefix 'klatka_2025-03-26_14-28-13_' and the suffix '.jpg' from the filename."""
    return re.sub(r'^klatka_2025-04-01_15-49-22_|\.jpg$', '', filename)

def process_csv(file_name):
    """Reads a CSV file, cleans filenames, and writes results to a new file."""
    output_file = "nowecleaned_" + file_name
    
    with open(file_name, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if len(row) < 2:
                continue  
            
            row[0] = clean_filename(row[0])  
            writer.writerow(row)  

def main():
    process_csv('processed_cleaned_result1.csv')  

if __name__ == "__main__":
    main()
