import smtplib
import csv
from email.message import EmailMessage

def sendEmail(reciever, name):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('csclub@sbschools.org', '?21robles')
    # creating the server that can trust u, and having
    # it log into whatever google account there is a certain
    # security setting that MUST be turned off before you
    # use this, or this code  will not work

    email = EmailMessage()
    email['From'] = 'csclub@sbschools.org'
    email['To'] = reciever
    email['Subject'] = 'Sponsorship for HackSB'
    # setting specifics for the email
    # who its from
    # the recipient
    # the subject
    # i think u can also cc and bcc

    email.set_content('message')
    # the name parameter in this function is to address
    # the company name in each automated email, assuming
    # column 0 contains all company names and column 1
    # contains all emails. The name parameter will be used
    # in the email content, where ever u want

    server.send_message(email)
    # server finally sends email


with open('[CSV_NAME].csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        reciever = line[1]
        name = line[0]
        sendEmail(reciever, name)

    # loops thru CSV (csv must have a particular format) and sets reciever and name of company ur emailing.
    # then function i made above will be called to create the email with ur specific message and it will send.