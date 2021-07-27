import pyttsx3  # Importing Text to speech Module
import speech_recognition as rs
import pywhatkit
import datetime
import wikipedia
from gtts import gTTS

r = rs.Recognizer()
engine = pyttsx3.init()
# Changing the audio in Female Voice
audio_change = engine.getProperty('voices')
engine.setProperty('voice', audio_change[1].id)


def listener():
    try:  # Exception handling to handle exceptions at run time

        with rs.Microphone() as user_source:

            # User can say his command after this text arrive
            print("Speak Now......")
            audio = r.listen(user_source)  # Listening the the user iput voice

            my_audio = r.recognize_google(audio)

            my_audio = my_audio.lower()  # converting the audio in lower case

            if 'goku' in my_audio:  # Using Key word to get a specific output
                my_audio = my_audio.replace('alexa', '')
                pyttsx3.speak("Welcome Neeraj Prasad")
    except:  # if error occure with program this block will run
        print("There is problem in recognizing the speech")
    return my_audio


def run_alexa():
    command = listener()
    if 'play' in command:  # PLAY key word is used to play any video on Youtube
        command = command.replace('play', '')
        pyttsx3.speak('Playign '+command)
        pywhatkit.playonyt(command)  # Open Video asked by the user in Browser
    elif 'time' in command:  # TIME key word is used to Get current time
        time = datetime.datetime.now().strftime('%I:%M %p')
        pyttsx3.speak(time)
    elif 'what is' in command:  # WHAT IS key word is used to fetch Data from Google / Wikipedia
        info = wikipedia.summary(command, 2)
        pyttsx3.speak(info)
    elif 'who is ' in command:  # WHO is key word is used to find data about the Person or something on google /Wikipedia
        info = wikipedia.summary(command, 2)
        pyttsx3.speak(info)

    elif 'note down' in command:  # note down key word is used to Write down the data asked by the user into txt file
        print("Writing down")
        writeSomething = command.replace('note down', '')
        info = wikipedia.summary(writeSomething, '2')
        file = open("MyData.txt", 'w')
        file.write(info)  # Writing down data in Text File
        pyttsx3.speak(info)

    elif 'convert in audio' in command:  # CONVERT IN AUDIO key word is used to convert text file into mp3 file
        text_file = open("MyData.txt", 'r')  # Reading the the file
        read_file = gTTS(text_file.read())
        read_file.save('AudioFile.mp3')  # Saving text file into audio

    elif 'search' in command:  # SEARCH command is used to search input in google on open browser
        command = command.replace('search', '')
        pywhatkit.search(command)
        print("searching...")

    elif 'send email' in command:  # send email command is used  to send the email
        subject = input("Subject of email :")  # Enter the subject of the email
        with rs.Microphone() as user_message:
            # User should start speaking the message after this message is appear
            print("Speak Message now....")
            message_audio = r.listen(user_message)
            my_audio = r.recognize_google(message_audio)
            message = my_audio  # Contant of Message in Email

            # User should input the Receiver Email ID
            email_receiver = input("Email Id of receiver : ")
            print("sending Email....")
            pywhatkit.send_mail('samtech2898@gmail.com', '*******', subject,
                                message, email_receiver)


run_alexa()
