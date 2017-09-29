import csv
import smtplib
from getpass import getpass

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

def login():
    """
    Connect and log in to email service
    """
    server_name = input("Enter email server (e.g. smtp.gmail.com): ")
    print("Connecting...")
    server = smtplib.SMTP(server_name, 587)
    server.ehlo()
    server.starttls()

    email_address = input("Login to email.\nEmail address: ")
    password = getpass("Password: ")
    print("Logging in...")
    server.login(email_address, password)

if __name__ == "__main__":
    login()
    read_data()
