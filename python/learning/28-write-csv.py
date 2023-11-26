import csv
 
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sahil', 'EP', '2', '9.1']]
 
filename = "university_records.csv"
 
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    print(fields)
    for row in csvreader:
        print(row)