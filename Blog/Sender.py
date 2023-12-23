import smtplib as smtp


try:
    email_sender = "rajabovtemurbek04@gmail.com"
    email_getter = "dpython074@gmail.com"
    smtp_server = smtp.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()

    smtp_server.login(email_sender, "tdwh cgjw wuav hwal")
    smtp_server.sendmail(email_sender, email_getter, "Hello Google")

except Exception as err:
    print(f"Unexpected {err}, {type(err)}")



