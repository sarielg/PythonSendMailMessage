def SendMailMessage(user_login, password_login ,smtp_server, smtp_port, sender, recipient, subject, content, cc=None, bcc=None, attachment=None):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path
    mail = smtplib.SMTP(smtp_server, smtp_port)
    mail.ehlo()
    mail.starttls()
    login_status=mail.login(user_login,password_login)
    DeliveryNotification=str(login_status).replace("(235, b'2.7.0 " ,"").replace("')","")
    msg = MIMEMultipart()
    msg['From'] = sender
    if cc:
        send_to_email_cc_multi =  cc
        send_to_email_cc =  ', '.join(send_to_email_cc_multi)
        msg['Cc']=send_to_email_cc
    if bcc:
        send_to_email_bcc_multi =  bcc
        send_to_email_bcc =  ', '.join(send_to_email_bcc_multi)
        msg['Bcc']=send_to_email_bcc
    if attachment:
        file_location=attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)
    send_to_email_multi =  recipient
    send_to_email =  ', '.join(send_to_email_multi)
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    text = msg.as_string()
    mail.sendmail(sender, send_to_email, text)
    mail.close()
    return DeliveryNotification
