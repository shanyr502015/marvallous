import smtplib
import time
from email.message import EmailMessage

email_address = "shanyr502015@gmail.com"
email_password = "hsavrdjahmiczepq"

def send_hello():
    msg = EmailMessage()
    msg['Subject'] = "Automation Test"
    msg['From'] = email_address
    msg['To'] = email_address
    msg.set_content("Hello World")

    try:
            # Switching to Port 587 and adding starttls()
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls() # Secure the connection
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
            print(f"Email sent at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error: {e}")

# The Testing Loop
print("Starting test... Press Ctrl+C to stop.")
try:
    while True:
        send_hello()
        time.sleep(10) # Wait for 10 seconds
except KeyboardInterrupt:
    print("\nTest stopped by user.")