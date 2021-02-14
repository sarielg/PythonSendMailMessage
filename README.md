# SendMailMessage
Python SendMailMessage Function of sending an email similar to Power Shell SendMailMessage 
you can take this function and call it from your script or from your moudle.

Example To Call The Function:

user_login = 'user_mail_login'

password_login = 'password_mail_login'

smtp_server ='ExchangeServer'

smtp_port = 'ExchangePort'

sender='Email@Domain'

recipient='Email@Domain','Email@Domain'

subject='this is the mail subject'

content="this is the mail content .... blbaalbalbalba"

cc='Email@Domain'   # carbon copy ,Defualt Value is None

bcc='Email@Domain'  # blind carbon copy ,Defualt Value is None

attachment= "C:\\Users\\You\\Desktop\\attach.txt" # path to the file ,Defualt Value is None

myMessage = SendMailMessage(user_login, password_login ,smtp_server, smtp_port, sender, recipient, subject, content, cc=None, bcc=None, attachment=None)

print(myMessage)

output: "Authentication successful"

