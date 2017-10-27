import csv
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

text = """
Hi {}!

This is a sample email message.

Luis"""

def read_data():
    """Read data from .csv file

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

def send_mail():
    """Log in to email service and send mail to recipient specified"""

    # Connect to email service
    server_name = input("Enter email server (e.g. smtp.gmail.com): ")
    print("Connecting...")
    server = smtplib.SMTP(server_name, 587)
    server.ehlo()
    server.starttls()

    # Log in
    print("Login to email...")
    email_address = input("Email address: ")
    password = getpass("Password: ")
    server.login(email_address, password)

    # Compose email
    print("Compose new message...")
    msg = MIMEMultipart()
    msg['Subject'] = input("Email subject: ")
    msg['From'] = email_address
    msg['To'] = input("Email recipient: ")
    msg.attach(MIMEText(text.format(msg['To']), ('plain')))

    # Send email
    server.send_message(msg)
    print("Sent email!")
    server.quit()

if __name__ == "__main__":
    print("This program sends emails to recipients extracted from .csv files.")
    send_mail()
    # read_data()
