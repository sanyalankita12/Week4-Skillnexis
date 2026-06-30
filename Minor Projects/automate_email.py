import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL")
sender_password = os.getenv("EMAIL_PASSWORD")

receiver_email = input("Enter receiver's email: ")

subject = "Test Email"
body = "Hello! This email was sent using Python."

message = f"""Subject: {subject}

{body}
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.sendmail(sender_email, receiver_email, message)

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    server.quit()