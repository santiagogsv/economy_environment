import csv

# Function to sum values in a row
def sum_row(row):
    return sum(int(value) for value in row[1:])  # Sum values from the second column onwards

# Read CSV file and calculate sums
rows_with_sums = []
with open('./data/indicator_count_by_year.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # Check if the row is not empty
            rows_with_sums.append((row[0], sum_row(row)))  # Append indicator name and sum of values

# Sort rows by sum of values
sorted_rows = sorted(rows_with_sums, key=lambda x: x[1], reverse=True)

# Print sorted rows
for row in sorted_rows:
    print(row[0], row[1])  # Print indicator name and sum of values
