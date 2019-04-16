import smtplib, os, imghdr
from email.message import EmailMessage

contacts = ['liugong.feng@aliyun.com', 'liugong.feng@outlook.com', 'gonphou@gmail.com']

EMAIL_ADDRESS =  os.environ.get('QEmail')
EMAIL_PASSWORD = os.environ.get('QEmailPassword')

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)    # 'liugong.feng@aliyun.com'
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


# files = ['resume.pdf']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         # file_type = imghdr.what(f.name)
#         file_name = f.name
#     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    
