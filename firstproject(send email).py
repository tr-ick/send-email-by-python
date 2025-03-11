from mailer import Mailer
my_mail = "write your email here your email"
mypass = "enter your password for your email"
send_to = "Write the email you want to send to "
my_subject = "write the subject of your email"
my_message = "Write the message you want to send"
mail = Mailer(email=my_mail, password=mypass)
mail.send(receiver=send_to ,subject=my_subject , message=my_message)