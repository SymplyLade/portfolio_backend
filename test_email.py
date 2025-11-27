import smtplib
from email.mime.text import MIMEText
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT

msg = MIMEText("This is a test email from FastAPI")
msg["Subject"] = "Test Email"
msg["From"] = SMTP_EMAIL
msg["To"] = SMTP_EMAIL 
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.set_debuglevel(1)
    server.starttls()
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())
    server.quit()
  
except Exception as e:
    print(f"Error: {e}")
