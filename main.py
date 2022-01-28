# Sends an email from a gmail account, and provides the option to include a file to attach to the email. If the file_path parameter is an emtpy string, no file will be attached.
import mimetypes
import smtplib
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender, password, recipient, body, subject, file_path):
    # Make file_path = "" if you don't want to send an attachment.
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if file_path != "":
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type, mime_subtype = mime_type.split('/')
        with open(file_path, 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=file_path.split("\\")[-1])

    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, password)
    mail_server.send_message(message)
    mail_server.quit()


def send_email_better(sender, password, recipient, body, subject, file_path):
    data = MIMEMultipart()
    data["From"] = sender
    data["To"] = recipient
    data["Subject"] = subject
    data.attach(MIMEText(body, 'plain'))
    if file_path != "":
        attachment = open(file_path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % file_path.split("\\")[-1])
        data.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)
    text = data.as_string()
    s.sendmail(sender, recipient, text)
    s.quit()
    return


send_email_better("mrtaquito04@gmail.com", "Gmail1215!", "8052984009@txt.att.net", "Yo Yo Yo!!! I can text you mommy!!!", "Can you see this?", "")

