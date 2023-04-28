import credentialsSMTP
import re
from urllib.request import urlopen
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

port = 465

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

url = "https://cestina-pro-cizince.cz/trvaly-pobyt/a2/online-prihlaska/"
page = urlopen(url)
html = page.read().decode("utf-8")
html = re.findall('Obsazeno',html)

if len(html) != 21: 
    print("\nSending Mail..........")
    text = """\
    Free slot avaliable:
    """
    html = """\
    <html>
    <body>
    <p>
        Free slot avaliable!<br>
        
    </p>
    </body>
    </html>
    """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    s = smtplib.SMTP_SSL(smtp_server, port)
    s.set_debuglevel(1)
    s.login(login,password)
    response = s.sendmail(sender_email, receiver_email, message.as_string())
    print("List of Failed Recipients : {}".format(response))
    print('Sent') 
else:
    print('Obsazeno!')     