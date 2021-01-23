import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_week = now.weekday()


with open("quotes.txt", encoding="utf8") as quotes_file:
    data = quotes_file.readlines()
    quotes_list = [quote for quote in data]
    quote = random.choice(quotes_list)
    random_quote = "".join(quote)


my_email = "your email"
password = "your password"
receiver = "email receiver"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
    if day_of_week == 0 or day_of_week == 4:
        connection.sendmail(
            my_email,
            receiver,
            fmt.format(my_email, receiver, "Quote of the day", random_quote).encode('utf-8')
        )
