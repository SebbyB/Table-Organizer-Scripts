import csv

# Function to generate the accession numbers
def generate_accession_numbers(start_prefix, start_mid, start_end, end_mid, end_end):
    current_mid = start_mid
    current_end = start_end
    while current_mid <= end_mid:
        while current_end <= 999999 and (current_mid < end_mid or current_end <= end_end):
            yield f"{start_prefix}-{current_mid:03d}-{current_end:06d}"
            current_end += 1
        current_mid += 1
        current_end = 1  # Reset the end part for the next mid value

# Function to write accession numbers to a CSV file
def write_to_csv(file_name, start_prefix, start_mid, start_end, end_mid, end_end):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Accession Number', 'Formatted Accession'])  # Write the header row
        row_number = 1  # Start from row 1 for the Excel formula
        for accession_number in generate_accession_numbers(start_prefix, start_mid, start_end, end_mid, end_end):
            formatted_accession = f'=CHAR(34) & A{row_number} & CHAR(34)'
            writer.writerow([accession_number, formatted_accession])
            row_number += 1

# Get user input for the ranges and output file name
start_prefix = input("Enter the prefix (e.g., 24): ")
start_mid = int(input("Enter the starting middle part (e.g., 1): "))
start_end = int(input("Enter the starting end part (e.g., 1): "))
end_mid = int(input("Enter the ending middle part (e.g., 355): "))
end_end = int(input("Enter the ending end part (e.g., 999999): "))
output_file = input("Enter the output file name (e.g., accession_numbers.csv): ")

# Write the accession numbers to the CSV file
write_to_csv(output_file, start_prefix, start_mid, start_end, end_mid, end_end)

print(f"CSV file '{output_file}' has been generated successfully.")
