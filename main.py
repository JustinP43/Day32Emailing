import smtplib
import datetime as dt
import random
import pandas

EMAIL = "justin.passmore@yahoo.com"
PASSWORD = "zyrgocobiccffqoo"
now = dt.datetime.now()

data = pandas.read_csv("./files/birthdays.csv").to_dict(orient="records")

for record in data:
    birthday_month = int(record["month"])
    birthday_day = int(record["day"])
    
    if birthday_month == now.month and birthday_day == now.day:
        with open(f"./files/letter_templates/letter_{str(random.randint(1,3))}.txt","r") as file:
            letter_contents = file.read()
            letter_contents = letter_contents.replace("[NAME]",record["name"])
        
        with smtplib.SMTP("smtp.mail.yahoo.com",587) as smtp:
            smtp.starttls()
            smtp.login(user=EMAIL,password=PASSWORD)
            smtp.sendmail(
                from_addr = EMAIL, 
                to_addrs = record["email"],
                msg = f"Subject: Happy Birthday!\n\n{letter_contents}"
                )


#print(data)

#if weekday == 0:
#    with open("./files/quotes.txt","r") as file:
#        quotes = file.readlines()
#        quote = random.choice(quotes)
#    
#    
#    with smtplib.SMTP("smtp.mail.yahoo.com",587) as smtp:
#        smtp.starttls()
#        smtp.login(user=EMAIL,password=PASSWORD)
#        
#        smtp.sendmail(
#            from_addr = EMAIL, 
#            to_addrs = "jmp6885@aol.com", 
#            msg = f"Subject: Monday Motivation\n\n{quote}"
#            )

