from email.message import EmailMessage
import smtplib
import getpass
if __name__ == "__main__":
    sender = "alokc4141@gmail.com"
    receiver = "alokchhari@gmail.com"
    # Enter your Google App Password securely
    sender_password = getpass.getpass("enter app pasword:-")
    msg = EmailMessage()
    msg["Subject"] = "This is testing"
    msg["From"] = sender
    msg["To"] = receiver
    message = input("Enter your message: ")
    msg.set_content(message)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as setup_email:
            setup_email.ehlo()
            setup_email.starttls()
            setup_email.ehlo()
            setup_email.login(sender, sender_password)
            setup_email.send_message(msg)
        print("Message sent successfully!")
    except smtplib.SMTPException as e:
        print("SMTP error:", e)
    except OSError as e:
        print("Network or connection error:", e)
