import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

