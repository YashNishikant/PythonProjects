import smtplib
import csv
from email.message import EmailMessage

def sendEmail(reciever, name):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('10016796@sbstudents.org', 'Nest09!#')
    # creating the server that can trust u, and having
    # it log into whatever google account there is a certain
    # security setting that MUST be turned off before you
    # use this, or this code  will not work

    email = EmailMessage()
    email['From'] = '10016796@sbschools.org'
    email['To'] = reciever
    email['Subject'] = 'test'
    # setting specifics for the email
    # who its from
    # the recipient
    # the subject
    # i think u can also cc and bcc

    email.set_content("Hello " + name + ", " +
                      "\n\nWe are the executive board of South Brunswick High School's Computer Science Club in New Jersey, a team of hardworking and passionate students who have spent numerous hours planning our annual hackathon, HackSB. This year, we are proud to announce that HackSB will be in person and will take place on May 13th, 2023. It will be a free, 12-hour hackathon at the South Brunswick High School."
                      "\n\nThrough our hackathon, we're hoping to foster a sense of community and collaboration. SBHS students have taken courses in topics such as Java Programming, Mobile Applications, and Virtual Reality, and HackSB gives numerous students the opportunity to display these skills in addition to their ingenuity, commitment, and resourcefulness. As such, we're incredibly excited to be hosting this event. However, HackSB is not possible without sponsorships from companies like you, which help provide food, prizes, and other essential items. Because of this, we would greatly appreciate your help to fund HackSB. Otherwise, we'd love for you to send us hardware, swag, prizes, and any other items we could hand out to participants. Any support would go a long way toward inspiring more students. "
                      "\n\nFor any further inquiries, please email us at csclub@sbschools.org."
                      "\n\nWe're eager to hear back from you and excited by the prospect of working with you in the future. "
                      "\n\nThanks, "
                      "\nThe HackSB Team");
    # the name parameter in this function is to address
    # the company name in each automated email, assuming
    # column 0 contains all company names and column 1
    # contains all emails. The name parameter will be used
    # in the email content, where ever u want

    server.send_message(email)
    # server finally sends email


with open('C:\\github\\PythonProjects\\EmailBot\\testing.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        reciever = line[1]
        name = line[0]
        sendEmail(reciever, name)

    # loops thru CSV (csv must have a particular format) and sets reciever and name of company ur emailing.
    # then function i made above will be called to create the email with ur specific message and it will send.