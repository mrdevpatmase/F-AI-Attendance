import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env into environment

def send_attendence_email():
    df = pd.read_csv(f"Attendance_{datetime.now().strftime('%Y-%m-%d')}.csv")
    df.to_excel(f"Attendance_{datetime.now().strftime('%Y-%m-%d')}.xlsx", index=False)

    file_path = f"Attendance_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            file_data = file.read()

        email_message = EmailMessage()
        email_message["Subject"] = "Attendance Report"
        email_message["From"] = "devpatmasep@gmail.com"
        email_message["To"] = "devpatmase1@gmail.com"
        email_message.set_content("Please find the attendance report attached.")
        email_message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_path)
        
        email_address = os.getenv("EMAIL_ADDRESS")
        email_password = os.getenv("EMAIL_PASSWORD")
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            print("Connecting to the SMTP server...")
            smtp.login(email_address, email_password)
            print("Login successful.")
            print("Sending email...")
            smtp.send_message(email_message)
    else:
        print("File not found.")

# ✅ Only runs if this file is executed directly
if __name__ == "__main__":
    send_attendence_email()
