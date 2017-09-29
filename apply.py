import csv

def read_data():
    """
    Read data from .csv file

    Assumptions for .csv file columns:
    row 0: headers
    column 0: company name
    """
    filename = input("Enter filename (e.g. file.csv): ")
    with open(filename, newline='') as csvfile:
        i = 0
        next(csvfile) # skip first line (headers)
        rows = csv.reader(csvfile) # read lines
        for row in rows:
            print("{}: {}".format(i, row[0]))
            i += 1

read_data()
