import csv

# Nazwy plików
input_file = "new_kwadrat2_po.csv"
output_file = "cleaned_result1.csv"

# Wczytaj plik CSV
with open(input_file, newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader, None)  
    data = [row for row in reader if row]  

if not data:
    print(" Błąd: Plik CSV nie zawiera żadnych danych!")
    exit(1)


cleaned_data = [["image", "binary_value"]] 
for row in data:
    if len(row) < 2:  
        continue
    image_name = row[0]  
    binary_string = "".join(row[1:])  
    cleaned_data.append([image_name, binary_string])

with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_data)

print(f"✅ Przetworzony plik zapisany jako {output_file}")