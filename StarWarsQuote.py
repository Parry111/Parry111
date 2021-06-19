import pandas as pd 
import random
import smtplib

lines = open("StarWarsQuotes.txt").read().splitlines()
myline =random.choice(lines)

df = pd.read_csv('emails.csv')

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("dailyclonewarsquotes@gmail.com", "jedimasteranakin")
    msg = myline + "\nHello Jedi's of the new Rebublic\nHow would you rate our service, please let us know.\nWe don't need your negativity Alessandro\nAlso, we are starting a new Jedi order RSPC if interested"
    subject = 'Daily Quote'
    body = 'Subject: {}\n\n{}'.format(subject,msg)

    for i in range(len(df)):
        print(df.iloc[i,0])
        server.sendmail("dailyclonewarsquotes@gmail.com", df.iloc[i,0], body)

    server.quit()
    print('Success')
except:
    print('Fail')