import csv
import smtplib
from email.message import EmailMessage

def sendEmail(reciever, name):
    # the "name" parameter in this function is to address the company name in each automated email
    # (assuming column 0 of the CSV contains all company names and column 1 contains all emails.)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('csclub@sbschools.org', '?21robles')
    # creating the server that can trust u, and having
    # it log into whatever google account u want

    # there is a certain security setting that
    # MUST be turned off before you
    # use this, or this code  will not work
    # accounts.google.com > security > Less Secure App Access > On
    # must be an account WITHOUT 2FA

    email = EmailMessage()
    email['From'] = 'csclub@sbschools.org'
    email['To'] = reciever
    email['Subject'] = 'South Brunswick Hackathon Sponsorship'
    # setting specifics for the email
    # -who its from
    # -the recipient
    # -the subject
    # -i think u can also cc and bcc

    email.set_content("message");

    server.send_message(email)
    # server finally sends email


with open('path', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        reciever = line[1]
        name = line[0]
        sendEmail(reciever, name)

    # loops thru CSV (csv must have a particular format) and sets reciever and name of company ur emailing.
    # then function sendEmail() i made above will be called to create the email with ur specific message.