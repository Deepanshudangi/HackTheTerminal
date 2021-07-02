import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

# Before using this code first give permission to allow less secure apps


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('happyagrawal120@gmail.com', '//password//')
    email = EmailMessage()
    email['From'] = 'happyagrawal120@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

# Give your list of names and their respective Emails here

email_list = {
    'parth':'agrawalparth564@gmail.com',
    'pranav':'agrawalpranav71@gmail.com',
    'papa':'parthagrawal35976@gmail.com'
}

def get_email_info():
    talk('To whom you want to send mail')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your mail')
    subject = get_info()
    talk('Tell the message of your mail')
    message = get_info()

    send_email(receiver, subject, message)

    talk('Hey man. Your mail is sent')
    talk('Do you want to send more mails')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()

