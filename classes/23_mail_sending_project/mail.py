# ===============================================
# Program :    Simple Gmail Mail Sender
# Author  :    Shantaram Patil
# Purpose :    Send mail using Python SMTP
# ===============================================
import smtplib
from email.message import EmailMessage
# -----------------------------------------------
# Function    :       Send_mail
# Description :       Sends email using Gmail SMTP server
# -----------------------------------------------
def send_mail(sender, app_password, receiver, subject, body):
    # Step 1 : Create Email object
    msg = EmailMessage()
    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    # Step 3 : Add mail body
    msg.set_content(body)
    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    # Step 5 : Login using Gmail + App password
    smtp.login(sender, app_password)
    # Step 6 : Send the email
    smtp.send_message(msg)
    # Step 7 : Close connection manually
    smtp.quit()

def main():
    # Always use separate temporary/testing account
    sender_email = "shanyr502015@gmail.com"
    # App password generated from Google account
    app_password = "fhmi zxfp yhzl pzcc"
    # Your second email for testing
    receiver_email = "shanyr502016@gmail.com"
    subject = "Test Mail from Python Script"
    # Multi-line string for email body
    body = """Jay Ganesh,

This is a test email sent using SHANTARAM's Python script.

Regards,
SHANTARAM PATIL
"""

    send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Marvellous Mail Sent Successfully")

# -----------------------------------------------
# Program Entry Point
# -----------------------------------------------
if __name__ == "__main__":
    main()